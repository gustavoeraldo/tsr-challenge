from sqlalchemy.orm import Session


from app.v1.core.repository import Repository, NotFoundError, ModelType
from app.v1.entities.beneficiary.model.beneficiary_model import BeneficiaryModel
from app.v1.entities.beneficiary.schemas.beneficiary_schemas import (
    BeneficiaryCreateInDBSchema,
    BeneficiaryUpdateInDBSchema,
)

from app.v1.entities.bank_account.model.bank_account_model import BankAccountModel


class NotFoundBeneficiaryError(NotFoundError):
    entity_name: str = "Beneficiary"


class BeneficiaryRepository(
    Repository[
        BeneficiaryModel, BeneficiaryCreateInDBSchema, BeneficiaryUpdateInDBSchema
    ]
):
    def create(self, data: BeneficiaryCreateInDBSchema) -> BeneficiaryModel:
        return super().create(data)

    def get_by_id(self, entity_id: int) -> BeneficiaryModel:
        data = super().get_by_id(entity_id)

        if not data:
            raise NotFoundBeneficiaryError(entity_id)
        return super().get_by_id(entity_id)

    def update_by_id(
        self, entity_id: int, data: BeneficiaryUpdateInDBSchema
    ) -> BeneficiaryModel:
        return super().update_by_id(entity_id, data)

    def delete_by_id(self, entity_id: int) -> None:
        obj = self.get_by_id(entity_id)
        return super().delete_by_id(obj)

    def get_paginated(
        self,
        beneficiary_filter: dict,
        bank_account_filter: dict,
        page: int,
        per_page: int,
    ) -> tuple:
        with self.session_factory() as session:
            beneficiary_columns = ["id", "name", "cpf_cnpj", "email", "status"]
            bank_account_columns = [
                "pix_key_type",
                "pix_key",
                "bank_name",
                "branch_number",
                "account_number",
                "account_type",
            ]

            query = session.query(
                *(getattr(self.model, attr) for attr in beneficiary_columns),
                *(getattr(BankAccountModel, attr) for attr in bank_account_columns),
            ).join(BankAccountModel, self.model.id == BankAccountModel.beneficiary_id)

            if beneficiary_filter.keys().__len__() > 0:
                query = self._filter(query, beneficiary_filter, self.model)

            if bank_account_filter.keys().__len__() > 0:
                query = self._filter(query, bank_account_filter, BankAccountModel)

            total = query.count()
            _data = query.offset((page - 1) * per_page).limit(per_page).all()

            _column_to_serialize = beneficiary_columns + bank_account_columns
            data = self._serialize_data(_data, _column_to_serialize)
            return data, total

    def _filter(self, query, filters: dict, model: ModelType) -> Session:
        for key, value in filters.items():
            if value:
                query = query.filter(getattr(model, key) == value)
        return query

    def _serialize_data(self, data: list, keys: list) -> list:
        return [dict(zip(keys, item)) for item in data]
