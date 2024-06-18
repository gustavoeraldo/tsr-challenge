from app.v1.core.repository import Repository, NotFoundError
from app.v1.entities.beneficiary.model.beneficiary_model import BeneficiaryModel
from app.v1.entities.beneficiary.schemas.beneficiary_schemas import (
    BeneficiaryCreateInDBSchema,
    BeneficiaryUpdateInDBSchema,
)


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
