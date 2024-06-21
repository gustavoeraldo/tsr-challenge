from app.v1.services.pix_api import PixApiService
from app.v1.core.exceptions import EntityNotFoundError
from app.v1.entities.bank_account.model.bank_account_model import BankAccountModel
from .bank_account_repository import BankAccountRepository
from .bank_account_schemas import (
    BankAccountCreateInDB,
    BankAccountUpdateSchema,
    BankAccountUpdateInDB,
)


class BankAccountService:
    def __init__(
        self,
        bank_account_repository: BankAccountRepository,
        pix_api_service: PixApiService,
    ):
        self._bank_account_repository = bank_account_repository
        self._pix_api_service = pix_api_service

    async def create(self, data: BankAccountCreateInDB) -> BankAccountModel:
        return self._bank_account_repository.create(data)

    def get_by_id(self, entity_id: int) -> BankAccountModel:
        return self._bank_account_repository.get_by_id(entity_id)

    def get(self, filters: dict):
        return self._bank_account_repository.get(filters)

    async def delete_by_beneficiary_id(self, beneficiary_id: int) -> None:
        bank_account = self.get({"beneficiary_id": beneficiary_id})
        if not bank_account:
            raise EntityNotFoundError("Could find bank account for this beneficiary")

        return self.delete_by_id(bank_account.id)

    def delete_by_id(self, entity_id: int) -> None:
        return self._bank_account_repository.delete_by_id(entity_id)

    async def update_by_beneficiary_id(
        self, beneficiary_id: int, data: BankAccountUpdateSchema
    ):
        bank_account = self.get({"beneficiary_id": beneficiary_id})

        if not bank_account:
            raise EntityNotFoundError("Could find bank account for this beneficiary")

        # Get bank account data from an external API
        if data.pix_key and data.pix_key_type:
            bank_account_data = self._pix_api_service.get_bank_data_by_pix(
                pix_type=data.pix_key_type, pix_key=data.pix_key
            )

            updated_bank_account = BankAccountUpdateInDB(
                **bank_account_data.model_dump()
            )
            return self.update_by_id(bank_account.id, updated_bank_account)

        return bank_account

    def update_by_id(self, entity_id: int, data: BankAccountUpdateInDB):
        return self._bank_account_repository.update_by_id(entity_id, data)
