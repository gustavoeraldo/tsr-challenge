from dependency_injector import containers, providers

from .database.db import Database
from .config.settings import settings

from app.v1.entities.beneficiary.model.beneficiary_model import BeneficiaryModel
from app.v1.entities.beneficiary.service.beneficiary_service import BeneficiaryService
from app.v1.entities.beneficiary.repository.beneficiary_repository import (
    BeneficiaryRepository,
)


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        modules=["app.v1.entities.beneficiary.service.beneficiary_service"],
    )

    db = providers.Singleton(Database, database_url=settings.DATABASE_URL)

    settings = providers.Object(settings)

    beneficiary_repository = providers.Factory(
        BeneficiaryRepository,
        model=BeneficiaryModel,
        session_factory=db.provided.session,
    )

    beneficiary_service = providers.Factory(
        BeneficiaryService,
        repository=beneficiary_repository,
    )
