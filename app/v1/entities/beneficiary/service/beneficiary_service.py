from app.v1.entities.beneficiary.repository.beneficiary_repository import (
    BeneficiaryRepository,
)
from app.v1.entities.beneficiary.schemas.beneficiary_schemas import (
    BeneficiaryCreateInDBSchema,
)

# from app.v1.entities.beneficiary.model.beneficiary_model import BeneficiaryModel


class BeneficiaryService:
    def __init__(self, repository: BeneficiaryRepository):
        self._repository = repository

    async def create(self, data: BeneficiaryCreateInDBSchema):
        return self._repository.create(data)

    def get_by_id(self, entity_id: int):
        return self._repository.get_by_id(entity_id)

    def delete_by_id(self, entity_id: int):
        return self._repository.delete_by_id(entity_id)

    def update_by_id(self, entity_id: int, data: dict):
        return self._repository.update_by_id(entity_id, data)
