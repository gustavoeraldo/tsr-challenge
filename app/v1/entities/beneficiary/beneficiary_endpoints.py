from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import Provide, inject

from app.v1.container import Container
from app.v1.entities.beneficiary.service.beneficiary_service import BeneficiaryService
from app.v1.entities.beneficiary.schemas.beneficiary_schemas import (
    BeneficiaryFormSchema,
    BeneficiaryCreateInDBSchema,
)

router = APIRouter()


def get_beneficiary_service():
    return Container.beneficiary_service()


@router.post("/beneficiary")
@inject
async def create_beneficiary(
    beneficiary: BeneficiaryFormSchema,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    # Create a new beneficiary
    beneficiary_data = BeneficiaryCreateInDBSchema(**beneficiary.model_dump())
    new_beneficiary = await service.create(beneficiary_data)

    # Create bank account for the new beneficiary
    # bank_account = await bank_account_service.create(new_beneficiary)

    # Create a beneficiary return mapper
    return new_beneficiary


@router.get("/beneficiary/{beneficiary_id}")
@inject
async def get_beneficiary(
    beneficiary_id: int,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    return service.get(beneficiary_id)


@router.patch("/beneficiary/{beneficiary_id}")
@inject
async def update_beneficiary(
    beneficiary_id: int,
    beneficiary: BeneficiaryFormSchema,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    return service.update_by_id(beneficiary_id, beneficiary)


@router.delete("/beneficiary/{beneficiary_id}")
@inject
async def delete_beneficiary(
    beneficiary_id: int,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    return service.delete_by_id(beneficiary_id)
