import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Settings:
    # API
    API_VERSION: str = os.getenv("API_VERSION") or "1.0.0"

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL") or "sqlite:///./test.db"

    # Network
    ORIGINS_CORS: str = os.getenv("ORIGINS_CORS") or "*"


settings = Settings()
