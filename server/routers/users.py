from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.models.user import User
from server.schemas.gardener import GardenerCreate
from server.models.gardener import Gardener
from server.utilis.security import get_current_user
from server.core.database import SessionLocal

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_gardener_profile")
def create_gardener_profile(
    gardener: GardenerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.is_gardener:
        raise HTTPException(status_code=400, detail="Você não é um jardineiro!")
    
    # Verifica se o jardineiro já existe
    db_gardener = db.query(Gardener).filter(Gardener.user_id == current_user.id).first()
    if db_gardener:
        raise HTTPException(status_code=400, detail="Perfil de jardineiro já existe!")
    
    # Cria o novo perfil de jardineiro
    new_gardener = Gardener(
        user_id=current_user.id,
        bio=gardener.bio,
        location=gardener.location
    )
    db.add(new_gardener)
    db.commit()
    db.refresh(new_gardener)
    
    return {"message": "Perfil de jardineiro criado com sucesso!"}
