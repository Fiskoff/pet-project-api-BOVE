import logging

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from sqladmin import Admin

from app.admin import admin_views
from app.api.routers import routers
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

    admin = Admin(app, db_helper.engine)
    for view in admin_views:
        admin.add_view(view)

    return app


main_app = create_application()


if __name__ == '__main__':
    print("Start FastAPI application")
    run("main:main_app", host=settings.run.host, port=settings.run.port)
