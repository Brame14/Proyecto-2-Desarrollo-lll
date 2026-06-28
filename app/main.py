import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. IMPORTACIONES CORRECCIONES SEGÚN TUS CARPETAS
# Importamos la base de datos y tus controladores (routers)
from app.config.database import engine, Base
from app.controller.auth_controller import router as auth_router
from app.controller.user_controller import router as user_router
from app.controller.donor_controller import router as donor_router
from app.controller.beneficiary_controller import router as beneficiary_router
from app.controller.campaign_controller import router as campaign_router
from app.controller.toy_controller import router as toy_router
from app.controller.delivery_controller import router as delivery_router

# Crear las tablas en la base de datos al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Regalando Sonrisas API",
    description="API REST para gestión de campañas solidarias",
    version="1.0.0"
)


templates = Jinja2Templates(directory="app/Screens")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(donor_router)
app.include_router(beneficiary_router)
app.include_router(campaign_router)
app.include_router(toy_router)
app.include_router(delivery_router)


#  RUTA PARA MOSTRAR LA VISTA DE LOGIN
@app.get("/login", response_class=HTMLResponse)
def get_login_page(request: Request):

    return templates.TemplateResponse("Login.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
def get_dashboard_page(request: Request):
    """
    Sirve la página HTML del menú principal desde la carpeta app/Screens/.
    """
    return templates.TemplateResponse("Menu.html", {"request": request})
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
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",


]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)