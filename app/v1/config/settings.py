import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Settings:
    # API
    API_VERSION: str = os.getenv("API_VERSION")

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Network
    ORIGINS_CORS: str = os.getenv("ORIGINS_CORS")


settings = Settings()
