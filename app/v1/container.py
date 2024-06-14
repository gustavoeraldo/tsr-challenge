from dependency_injector import containers, providers

from .database.db import Database
from .config.settings import settings


class Container(containers.DeclarativeContainer):
    db = providers.Singleton(Database, database_url=settings.DATABASE_URL)

    settings = providers.Object(settings)
