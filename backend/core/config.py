from os import getenv
from urllib.parse import quote_plus

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

from core.loger_config import LogerConfig


load_dotenv()

class DatabaseENV:
    DB_USER: str = getenv("DB_USER")
    DB_PASSWORD: str = getenv("DB_PASSWORD")
    DB_HOST: str = getenv("DB_HOST")
    DB_PORT: str = getenv("DB_PORT")
    DB_NAME: str = getenv("DB_NAME")


class ServerENV:
    SERVER_HOST: str = getenv("SERVER_HOST")
    SERVER_PORT: int = int(getenv("SERVER_PORT"))


class RunConfig(BaseModel):
    host: str = ServerENV.SERVER_HOST
    port: int = ServerENV.SERVER_PORT


class DataBaseConfig(BaseModel):
    url: str = f"postgresql+asyncpg://{DatabaseENV.DB_USER}:{DatabaseENV.DB_PASSWORD}@{DatabaseENV.DB_HOST}:{DatabaseENV.DB_PORT}/{DatabaseENV.DB_NAME}"
    echo: bool = False
    pool_size: int = 35
    max_overflow: int = 100


class AuthConfig(BaseModel):
    SECRET_KEY: str = getenv("SECRET_KEY")


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DataBaseConfig = DataBaseConfig()
    log: LogerConfig = LogerConfig()
    auth: AuthConfig = AuthConfig()


settings = Settings()