from pydantic import Field, BaseModel, field_validator
from typing import Optional
import re

from app.v1.entities.bank_account.schemas.bank_account_schema import (
    BankAccountBaseSchema,
)


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


class BeneficiaryUpdatechema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    cpf_cnpj: Optional[str] = None
    status: Optional[str] = None

    @field_validator("email")
    def validate_email(cls, value):
        if value is not None:
            if not re.match(r"^[A-Z0-9+_.-]+@[A-Z0-9.-]+$", value):
                raise ValueError("Invalid email")
        return value

    @field_validator("cpf_cnpj")
    def validate_cpf_cnpj(cls, value):
        if value is not None:
            if not re.match(
                r"(^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$)|(^[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}$)",
                value,
            ):
                raise ValueError("Invalid cpf_cnpj")
        return value


class BeneficiaryCreateInDBSchema(BeneficiaryBaseSchema):
    status: str = "rascunho"
