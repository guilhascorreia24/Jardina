from fastapi import FastAPI
from server.core.config import FRONTEND_URL
from server.routers import auth,users,services,notifications
from server.core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(services.router)
app.include_router(notifications.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)