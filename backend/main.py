import logging

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from app.admin import admin_views
from app.api.routers import routers
from app.auth.admin_auth import authentication_backend
from core.config import settings
from core.db_helper import db_helper


settings.log.setup_logging()
logger = logging.getLogger(__name__)

def create_application() -> FastAPI:
    app = FastAPI(title="BOVE", version="1.0.0", docs_url="/docs", redoc_url="/redoc")

    router = APIRouter(tags=["root"])
    @router.get("/")
    async def root():
        return {
            "message": "BOVE API",
            "admin":   "/admin",
            "swagger": "/docs",
            "redoc":   "/redoc",
        }

    app.include_router(router)
    for router in routers:
        app.include_router(router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Разрешённые домены - все
        allow_credentials=False,  # True только при указанном разрешённом домене
        allow_methods=["*"],  # Разрешить все методы
        allow_headers=["*"],  # Разрешить все заголовки
    )

    admin = Admin(app, db_helper.engine, authentication_backend=authentication_backend)
    for view in admin_views:
        admin.add_view(view)

    return app


app = create_application()
