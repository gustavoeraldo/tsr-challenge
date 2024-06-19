from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Annotated

from app.v1.container import Container
from app.v1.entities.bank_account.bank_account_service import BankAccountService
from app.v1.entities.bank_account.bank_account_schemas import BankAccountFilter
from app.v1.entities.beneficiary.service.beneficiary_service import BeneficiaryService
from app.v1.entities.beneficiary.schemas.beneficiary_schemas import (
    BeneficiaryFormSchema,
    BeneficiaryUpdateFormSchema,
    BeneficiaryBaseFilter,
)

router = APIRouter()


def get_bank_account_service():
    return Container.bank_account_service()


def get_beneficiary_service():
    return Container.beneficiary_service()


@router.post(
    "/beneficiary",
    status_code=status.HTTP_201_CREATED,
)
async def create_beneficiary(
    beneficiary: BeneficiaryFormSchema,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    # Create a new beneficiary
    new_beneficiary = await service.create(beneficiary)

    # Send a request to validate the new beneficiary
    # service.validate_beneficiary(new_beneficiary)
    return new_beneficiary


@router.get("/beneficiary/{beneficiary_id}")
async def get_beneficiary(
    beneficiary_id: int,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    return service.get_by_id(beneficiary_id)


@router.get("/beneficiaries")
async def get_beneficiaries(
    # "Status", "Nome", "Tipo da chave" ou "Valor da chave"
    name: Annotated[str | None, Query(max_length=100)] = None,
    status: Annotated[str | None, Query(max_length=20)] = None,
    pix_key_type: Annotated[str | None, Query(max_length=20)] = None,
    pix_key_value: Annotated[str | None, Query(max_length=100)] = None,
    page: int = 1,
    per_page: int = 10,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):

    beneficiary_filter = BeneficiaryBaseFilter(name=name, status=status)
    bank_account_filter = BankAccountFilter(
        pix_key_type=pix_key_type, pix_key=pix_key_value
    )

    data, total = await service.get_paginated(
        beneficiary_filter=beneficiary_filter.model_dump(
            exclude_unset=True, exclude_none=True, exclude_defaults=True
        ),
        bank_account_filter=bank_account_filter.model_dump(
            exclude_unset=True, exclude_none=True, exclude_defaults=True
        ),
        page=page,
        per_page=per_page,
    )

    return {"total": total, "page": page, "per_page": per_page, "data": data}


@router.patch("/beneficiary/{beneficiary_id}", status_code=status.HTTP_200_OK)
async def update_beneficiary(
    beneficiary_id: int,
    data: BeneficiaryUpdateFormSchema,
    service: BeneficiaryService = Depends(get_beneficiary_service),
    bank_account_service: BankAccountService = Depends(get_bank_account_service),
):
    # Update the beneficiary
    updated_beneficiary = await service.update_by_id(beneficiary_id, data)

    # Update the beneficiary bank account
    await bank_account_service.update_by_beneficiary_id(beneficiary_id, data)
    return updated_beneficiary


@router.delete("/beneficiary/{beneficiary_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_beneficiary(
    beneficiary_id: int,
    service: BeneficiaryService = Depends(get_beneficiary_service),
    bank_account_service: BankAccountService = Depends(get_bank_account_service),
):
    try:
        # Delete the beneficiary bank account
        await bank_account_service.delete_by_beneficiary_id(beneficiary_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    await service.delete_by_id(beneficiary_id)
    return None
