import os

from .base import *
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, '.env'),
        extra='ignore',
    )
    DEBUG: bool = True
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

settings = Settings()

ALLOWED_HOSTS = ["*"]
DEBUG = settings.DEBUG

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": settings.DB_NAME,
        "USER": settings.DB_USER,
        "PASSWORD": settings.DB_PASSWORD,
        "HOST": settings.DB_HOST,
        "PORT": settings.DB_PORT,
    }
}

