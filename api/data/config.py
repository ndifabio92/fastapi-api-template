import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", True)
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        env_file = ".env"

settings = Settings()