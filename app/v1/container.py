from dependency_injector import containers, providers

from .database.db import Database
from .config.settings import settings

from app.v1.entities.beneficiary.model.beneficiary_model import BeneficiaryModel
from app.v1.entities.beneficiary.service.beneficiary_service import BeneficiaryService
from app.v1.entities.beneficiary.repository.beneficiary_repository import (
    BeneficiaryRepository,
)

from app.v1.entities.bank_account.model.bank_account_model import BankAccountModel
from app.v1.entities.bank_account.bank_account_repository import BankAccountRepository
from app.v1.entities.bank_account.bank_account_service import BankAccountService

from app.v1.services.pix_api import PixApiService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        modules=["app.v1.entities.beneficiary.service.beneficiary_service"],
    )

    db = providers.Singleton(Database, database_url=settings.DATABASE_URL)

    settings = providers.Object(settings)

    # Bank Account modules
    bank_account_repository = providers.Factory(
        BankAccountRepository,
        model=BankAccountModel,
        session_factory=db.provided.session,
    )

    bank_account_service = providers.Factory(
        BankAccountService,
        bank_account_repository=bank_account_repository,
        pix_api_service=providers.Factory(PixApiService),
    )

    # Beneficiary modules
    beneficiary_repository = providers.Factory(
        BeneficiaryRepository,
        model=BeneficiaryModel,
        session_factory=db.provided.session,
    )

    beneficiary_service = providers.Factory(
        BeneficiaryService,
        repository=beneficiary_repository,
        bank_account_service=bank_account_service,
        pix_api_service=providers.Factory(PixApiService),
    )
