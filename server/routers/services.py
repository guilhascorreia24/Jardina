import asyncio
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.models.gardener import Gardener
from server.models.notification import Notification
from server.models.user import User
from server.schemas.service import ServiceCreate
from server.models.services import Service
from server.utilis.security import get_current_user
from server.core.database import SessionLocal
from server.models.user import User as UserModel
from server.utilis.security import get_current_user
from server.utilis.email import send_email


router = APIRouter(prefix="/services", tags=["services"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_service")
async def create_service(
    service: ServiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_service = Service(
        client_id=current_user.id,
        gardener_id=service.gardener_id,
        description=service.description,
    )
    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    gardener=db.query(Gardener).filter(Gardener.id == service.gardener_id).first()
    user = db.query(User).filter(User.id == gardener.user_id).first()

    if gardener:
        notif = Notification(
            user_id=user.id,
            content=f"Novo serviço solicitado: {service.description}"
        )
        db.add(notif)
        db.commit()

        asyncio.create_task(
            send_email(
                to_email=user.email,
                subject="Novo pedido de serviço",
                content=f"Você recebeu um novo pedido de serviço: {service.description}"
            )
        )
    return {"message": "Serviço solicitado com sucesso!"}


@router.get("/my_pending_services")
def list_pending_services(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.is_gardener:
        raise HTTPException(status_code=403, detail="Apenas jardineiros podem acessar esta rota.")

    gardenerid= db.query(Gardener).filter(Gardener.user_id == current_user.id).first()
    services = db.query(Service).filter(
        Service.gardener_id == gardenerid.id,
        Service.status == "pendente"
    ).all()
    for service in services:
        client = db.query(UserModel).filter(UserModel.id == service.client_id).first()
        service.client_name = client.name if client else "Desconhecido"
    return services

@router.post("/confirm_service/{service_id}")
async def confirm_service_done(
    service_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = db.query(Service).filter(Service.id == service_id).first()

    if not service:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")

    if service.client_id != current_user.id:
        raise HTTPException(status_code=403, detail="Você não é o dono deste serviço")

    if service.status == "concluido":
        raise HTTPException(status_code=400, detail="Este serviço já está concluído")

    service.status = "concluido"
    db.commit()
    db.refresh(service)

    gardener=db.query(Gardener).filter(Gardener.id == service.gardener_id).first()
    user = db.query(User).filter(User.id == gardener.user_id).first()

    if gardener:
        notif = Notification(
            user_id=user.id,
            content=f"O cliente confirmou que o serviço '{service.description}' foi concluído."
        )
        db.add(notif)
        db.commit()

        asyncio.create_task(
            send_email(
                to_email=user.email,
                subject="Serviço confirmado",
                content=f"O serviço '{service.description}' foi concluído com sucesso!"
            )
        )

    return {"message": "Serviço marcado como concluído com sucesso!"}


