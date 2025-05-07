from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.schemas.user import UserCreate
from server.models.user import User
from server.core.database import SessionLocal
from server.utilis.security import hash_password
from fastapi.security import OAuth2PasswordRequestForm
from server.utilis.security import verify_password, create_access_token
from datetime import timedelta
from server.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from jose import JWTError

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        is_gardener=user.is_gardener
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Usuário criado com sucesso"}



@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return {"access_token": access_token, "token_type": "bearer", "is_gardener":user.is_gardener  }