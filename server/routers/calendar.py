from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from server.models import User, Service
from server.core.database import get_db
from server.utilis.google_calendar import get_auth_flow, get_calendar_service, create_event
from datetime import datetime, timedelta
import os

from server.utilis.security import get_current_user

router = APIRouter(prefix="/calendar",tags=["calendar"])

@router.get("/oauth/init")
def start_google_oauth():
    flow = get_auth_flow()
    auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline', include_granted_scopes='true')
    return {"url": auth_url}

@router.get("/oauth/callback")
def google_callback(request: Request, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    code = request.query_params.get("code")
    flow = get_auth_flow()
    flow.fetch_token(code=code)

    credentials = flow.credentials
    current_user.google_refresh_token = credentials.refresh_token
    db.commit()
    return {"msg": "Google Calendar conectado com sucesso."}

@router.get("/sync")
def sync_services_to_calendar(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.google_refresh_token:
        return {"error": "Conta Google não conectada"}

    service = get_calendar_service(current_user.google_refresh_token)

    services = db.query(Service).filter(
        Service.gardener_id == current_user.id,
        Service.status == "pendente"
    ).all()

    for s in services:
        start = datetime.combine(s.date, s.start_time)
        end = start + timedelta(hours=1)
        create_event(service, "Serviço de Jardinagem", s.description, start, end)

    return {"msg": f"{len(services)} eventos sincronizados com o Google Calendar"}
