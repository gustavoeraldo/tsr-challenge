from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.v1.core.repository import Repository, NotFoundError, ModelType
from app.v1.entities.beneficiary.model.beneficiary_model import BeneficiaryModel
from ..schemas.beneficiary_mappers import BeneficiaryItemMapper
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

    def get_data_and_bank_account_by_id(self, entity_id: int) -> BeneficiaryItemMapper:
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

            query = query.filter(self.model.id == entity_id)
            _data = query.first()

            if not _data:
                raise NotFoundBeneficiaryError(entity_id)

            _column_to_serialize = beneficiary_columns + bank_account_columns
            data = self._serialize(_data, _column_to_serialize)

            return BeneficiaryItemMapper(**data)

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
            data = self._serialize_list(_data, _column_to_serialize)
            return data, total

    def _filter(self, query: Session, filters: dict, model: ModelType) -> Session:
        for key, value in filters.items():
            if isinstance(value, str):
                query = self._like_filter(query, {key: value}, model)
            elif isinstance(value, list):
                query = self._in_filter(query, {key: value}, model)
            else:
                query = query.filter(getattr(model, key) == value)
        return query

    def _like_filter(
        self, query: Session, filters: dict[str, str], model: ModelType
    ) -> Session:
        for key, value in filters.items():
            if value:
                query = query.filter(
                    func.lower(getattr(model, key)).like(f"%{value.lower()}%")
                )
        return query

    def _in_filter(
        self, query: Session, filters: dict[str, list], model: ModelType
    ) -> Session:
        for key, value in filters.items():
            if value:
                query = query.filter(getattr(model, key).in_(value))
        return query

    def _serialize(self, data: tuple, keys: list) -> dict:
        return dict(zip(keys, data))

    def _serialize_list(self, data: list, keys: list) -> list:
        return [dict(zip(keys, item)) for item in data]
