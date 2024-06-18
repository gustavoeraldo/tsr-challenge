from app.v1.core.repository import Repository, NotFoundError
from app.v1.entities.bank_account.model.bank_account_model import BankAccountModel
from app.v1.entities.bank_account.bank_account_schemas import (
    BankAccountCreateInDB,
    BankAccountUpdateInDB,
)


class NotFoundBankAccountError(NotFoundError):
    entity_name: str = "Bank Account"


class BankAccountRepository(
    Repository[BankAccountModel, BankAccountCreateInDB, BankAccountUpdateInDB]
):
    def create(self, data: BankAccountCreateInDB) -> BankAccountModel:
        return super().create(data)

    def get(self, filters: dict):
        return super().get(filters)

    def get_by_id(self, entity_id: int) -> BankAccountModel:
        data = super().get_by_id(entity_id)

        if not data:
            raise NotFoundBankAccountError(entity_id)
        return super().get_by_id(entity_id)

    def update_by_id(
        self, entity_id: int, data: BankAccountUpdateInDB
    ) -> BankAccountModel:
        return super().update_by_id(entity_id, data)

    def delete_by_id(self, entity_id: int) -> None:
        obj = self.get_by_id(entity_id)
        return super().delete_by_id(obj)
