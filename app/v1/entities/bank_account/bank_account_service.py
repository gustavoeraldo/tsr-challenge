from app.v1.entities.bank_account.model.bank_account_model import BankAccountModel
from .bank_account_repository import BankAccountRepository
from .bank_account_schemas import BankAccountCreateInDB


class BankAccountService:
    def __init__(self, bank_account_repository: BankAccountRepository):
        self._bank_account_repository = bank_account_repository

    async def create(self, data: BankAccountCreateInDB) -> BankAccountModel:
        return self._bank_account_repository.create(data)

    def get_by_id(self, entity_id: int) -> BankAccountModel:
        return self._bank_account_repository.get_by_id(entity_id)

    async def delete_by_id(self, entity_id: int) -> None:
        return self._bank_account_repository.delete_by_id(entity_id)

    def update_by_id(self, entity_id: int, data: dict):
        return self._bank_account_repository.update_by_id(entity_id, data)
