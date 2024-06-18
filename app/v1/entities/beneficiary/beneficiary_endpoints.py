from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject

from app.v1.container import Container
from app.v1.entities.beneficiary.service.beneficiary_service import BeneficiaryService
from app.v1.entities.beneficiary.schemas.beneficiary_schemas import (
    BeneficiaryFormSchema,
    BeneficiaryCreateInDBSchema,
)

router = APIRouter()


def get_beneficiary_service():
    return Container.beneficiary_service()


@router.post(
    "/beneficiary",
    status_code=status.HTTP_201_CREATED,
)
@inject
async def create_beneficiary(
    beneficiary: BeneficiaryFormSchema,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    # Create a new beneficiary
    new_beneficiary = await service.create_v2(beneficiary)

    # Send a request to validate the new beneficiary
    # service.validate_beneficiary(new_beneficiary)
    return new_beneficiary


@router.get("/beneficiary/{beneficiary_id}")
async def get_beneficiary(
    beneficiary_id: int,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    return service.get(beneficiary_id)


@router.patch("/beneficiary/{beneficiary_id}")
async def update_beneficiary(
    beneficiary_id: int,
    beneficiary: BeneficiaryFormSchema,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    return service.update_by_id(beneficiary_id, beneficiary)


@router.delete("/beneficiary/{beneficiary_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_beneficiary(
    beneficiary_id: int,
    service: BeneficiaryService = Depends(get_beneficiary_service),
):
    try:
        await service.delete_by_id(beneficiary_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return None
