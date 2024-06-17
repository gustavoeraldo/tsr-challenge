from app.v1.core.repository import Repository, NotFoundError
from app.v1.entities.beneficiary.model.beneficiary_model import BeneficiaryModel
from app.v1.entities.beneficiary.schemas.beneficiary_schemas import (
    BeneficiaryCreateInDBSchema,
    BeneficiaryUpdatechema,
)


class NotFoundBeneficiaryError(NotFoundError):
    entity_name: str = "Beneficiary"


class BeneficiaryRepository(
    Repository[BeneficiaryModel, BeneficiaryCreateInDBSchema, BeneficiaryUpdatechema]
):
    def create(self, data: BeneficiaryCreateInDBSchema) -> BeneficiaryModel:
        return super().create(data)

    def get_by_id(self, entity_id: int) -> BeneficiaryModel:
        return super().get_by_id(entity_id)

    def update_by_id(
        self, entity_id: int, data: BeneficiaryUpdatechema
    ) -> BeneficiaryModel:
        return super().update_by_id(entity_id, data)

    def delete_by_id(self, entity_id: int) -> BeneficiaryModel:
        return super().delete_by_id(entity_id)
