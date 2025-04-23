from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.utilis.security import get_current_user
from server.models.notification import Notification
from server.schemas.notification import NotificationOut
from server.core.database import SessionLocal

router = APIRouter(prefix="/notifications", tags=["notifications"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[NotificationOut])
def get_my_notifications(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    print(current_user.id)
    return db.query(Notification).filter(Notification.user_id == current_user.id).all()

@router.post("/mark_as_read/{notification_id}")
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    notification = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.user_id == current_user.id
    ).first()

    if notification:
        notification.is_read = True
        db.commit()
        return {"message": "Notificação marcada como lida."}
    return {"message": "Notificação não encontrada."}
