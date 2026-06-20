from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import Base
from app.config.database import engine

from app.controller.auth_controller import router as auth_router
from app.controller.user_controller import router as user_router
from app.controller.donor_controller import router as donor_router
from app.controller.beneficiary_controller import router as beneficiary_router
from app.controller.campaign_controller import router as campaign_router
from app.controller.toy_controller import router as toy_router
from app.controller.delivery_controller import router as delivery_router

from app.model.user import User
from app.model.donor import Donor
from app.model.beneficiary import Beneficiary
from app.model.campaign import Campaign
from app.model.toy import Toy
from app.model.delivery import Delivery

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Regalando Sonrisas API",
    description="API REST para gestión de campañas solidarias",
    version="1.0.0"
)

# CORS para permitir conexión con frontend HTML/JS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(donor_router)
app.include_router(beneficiary_router)
app.include_router(campaign_router)
app.include_router(toy_router)
app.include_router(delivery_router)


@app.get("/")
def root():
    return {
        "message": "Regalando Sonrisas API Running",
        "status": "OK"
    }


@app.get("/health")
def health_check():
    return {
        "database": "connected",
        "api": "running"
    }