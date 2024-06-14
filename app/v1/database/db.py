from contextlib import contextmanager, AbstractContextManager
from typing import Callable
import logging
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

logger = logging.getLogger(__name__)

Base: DeclarativeMeta = declarative_base()


class Database:
    def __init__(self, database_url: str) -> None:
        self.engine = sqlalchemy.create_engine(
            database_url,
            pool_pre_ping=True,
            pool_size=20,
            pool_recycle=3600,
            max_overflow=20,
            poolclass=sqlalchemy.pool.QueuePool,
        )
        self._session_factory = sqlalchemy.orm.sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine,
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self.engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.error("Session rollback because of an exception")
            session.rollback()
            raise
        finally:
            session.close()
