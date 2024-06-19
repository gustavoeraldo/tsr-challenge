from pydantic import Field, BaseModel, field_validator
from typing import Optional
import re

from app.v1.core.pagination_schema import Pagination

from .beneficiary_mappers import BeneficiaryListMapper
from app.v1.entities.bank_account.bank_account_schemas import (
    BankAccountBaseSchema,
    BankAccountUpdateSchema,
)


# BASIC SCHEMAS
class BeneficiaryBaseSchema(BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    email: Optional[str] = Field(
        ..., max_length=250, pattern=r"^[A-Z0-9+_.-]+@[A-Z0-9.-]+$"
    )
    cpf_cnpj: str = Field(
        ...,
        min_length=11,
        max_length=14,
        pattern=r"(^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$)|(^[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}$)",
    )


class BeneficiaryBaseUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    cpf_cnpj: Optional[str] = None


class BeneficiaryBaseFilter(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None


# EXTERNAL SCHEMAS - API REQUESTS AND RESPONSES
class BeneficiaryFormSchema(BankAccountBaseSchema, BeneficiaryBaseSchema):

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "João da Silva",
                "email": "JOAO.DA.SILVA@GMAIL.COM",
                "cpf_cnpj": "067.956.219-07",
                "pix_key_type": "EMAIL",
                "pix_key": "joao.da.silva@gmail.com",
            }
        }
    }


class BeneficiaryUpdateFormSchema(BeneficiaryBaseSchema, BankAccountUpdateSchema):
    name: Optional[str] = None
    email: Optional[str] = Field(
        None, max_length=250, pattern=r"^[A-Z0-9+_.-]+@[A-Z0-9.-]+$"
    )
    cpf_cnpj: Optional[str] = Field(
        None,
        min_length=11,
        max_length=14,
        pattern=r"(^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$)|(^[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}$)",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "",
                "email": "",
                "cpf_cnpj": "",
                "pix_key_type": "",
                "pix_key": "",
            }
        }
    }


class BeneficiaryPaginatedResponseSchema(Pagination):
    data: list[BeneficiaryListMapper]


# INTERNAL SCHEMAS - DATABASE MANIPULATION
class BeneficiaryCreateInDBSchema(BeneficiaryBaseSchema):
    status: str = "rascunho"


class BeneficiaryUpdateInDBSchema(BeneficiaryBaseUpdate):
    status: Optional[str] = None
