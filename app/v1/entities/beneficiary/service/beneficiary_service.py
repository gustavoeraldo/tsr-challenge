from app.v1.entities.beneficiary.model.beneficiary_model import BeneficiaryModel
from app.v1.entities.beneficiary.repository.beneficiary_repository import (
    BeneficiaryRepository,
)
from app.v1.entities.beneficiary.schemas.beneficiary_schemas import (
    BeneficiaryCreateInDBSchema,
    BeneficiaryFormSchema,
    BeneficiaryUpdateFormSchema,
    BeneficiaryUpdateInDBSchema,
)

from app.v1.entities.bank_account.bank_account_service import BankAccountService
from app.v1.entities.bank_account.bank_account_schemas import (
    BankAccountCreateInDB,
)

from app.v1.services.pix_api import PixApiService


class BeneficiaryService:
    def __init__(
        self,
        repository: BeneficiaryRepository,
        bank_account_service: BankAccountService,
        pix_api_service: PixApiService,
    ):
        self._repository = repository
        self._bank_account_service = bank_account_service
        self._pix_api_service = pix_api_service

    async def create(self, data: BeneficiaryFormSchema):
        # Create a new beneficiary
        beneficiary_data = BeneficiaryCreateInDBSchema(**data.model_dump())
        new_beneficiary = self._create(beneficiary_data)

        # Get bank account data from an external API
        bank_account_data = self._pix_api_service.get_bank_data_by_pix(
            pix_type=data.pix_key_type, pix_key=data.pix_key
        )

        # Create a new bank account for the new beneficiary
        beneficiary_bank_acc = BankAccountCreateInDB(
            **bank_account_data.model_dump(), beneficiary_id=new_beneficiary.id
        )

        try:
            # if bank account creation fails, delete the new beneficiary
            await self._bank_account_service.create(beneficiary_bank_acc)
        except Exception:
            self._repository.delete_by_id(new_beneficiary.id)
            raise Exception("Bank account creation failed")

        # Create a mapper to return the new beneficiary with the bank account data
        return new_beneficiary

    def get_by_id(self, entity_id: int) -> BeneficiaryModel:
        return self._repository.get_by_id(entity_id)

    async def get_paginated(
        self,
        beneficiary_filter: dict,
        bank_account_filter: dict,
        page: int,
        per_page: int,
    ):
        data, total = self._repository.get_paginated(
            beneficiary_filter, bank_account_filter, page, per_page
        )

        return data, total

    async def delete_by_id(self, entity_id: int) -> None:
        return self._repository.delete_by_id(entity_id)

    async def update_by_id(self, entity_id: int, data: BeneficiaryUpdateFormSchema):
        # get the beneficiary by id
        beneficiary = self._repository.get_by_id(entity_id)
        updated_beneficiary = BeneficiaryUpdateInDBSchema()

        # update the beneficiary
        if beneficiary.status == "validado" and data.email:
            # if status is "validado", can only update the field: email
            updated_beneficiary.email = data.email
        else:
            # if status is "rascunho", can update the fields: name, email, cpf_cnpj
            updated_beneficiary = BeneficiaryUpdateInDBSchema(
                **data.model_dump(exclude_none=True, exclude_defaults=True)
            )

        return self._update(entity_id, updated_beneficiary)

    def _create(self, data: BeneficiaryCreateInDBSchema) -> BeneficiaryModel:
        return self._repository.create(data)

    def _update(
        self, entity_id: int, data: BeneficiaryUpdateInDBSchema
    ) -> BeneficiaryModel:
        return self._repository.update_by_id(entity_id, data)
