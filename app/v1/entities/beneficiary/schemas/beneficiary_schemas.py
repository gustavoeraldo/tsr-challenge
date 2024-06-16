from pydantic import Field, BaseModel
from typing import Optional

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


class BeneficiaryFormSchema(BeneficiaryBaseSchema, BankAccountBaseSchema): ...
