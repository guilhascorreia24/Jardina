
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.core.database import SessionLocal
from server.models.availability import Availability
from server.models.favorites import Favorite
from server.utilis.security import get_current_user

router = APIRouter(prefix="/services", tags=["availability"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/favorites/{gardener_id}")
def add_favorite(gardener_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    fav = Favorite(client_id=current_user.id, gardener_id=gardener_id)
    db.add(fav)
    db.commit()
    return {"msg": "Adicionado aos favoritos"}

@router.get("/favorites")
def list_favorites(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    favs = db.query(Favorite).filter(Favorite.client_id == current_user.id).all()
    return favs
