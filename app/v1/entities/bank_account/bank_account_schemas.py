from pydantic import BaseModel, field_validator, model_validator
from typing import Optional

from app.v1.helpers import PixKeyValidator


# BASIC SCHEMAS
class BankAccountBaseSchema(BaseModel):
    pix_key_type: str
    pix_key: str

    @field_validator("pix_key_type")
    @classmethod
    def validate_pix_key_type(cls, value):
        if value not in ["CPF", "CNPJ", "PHONE", "EMAIL", "RANDOM"]:
            raise ValueError("Invalid pix type")
        return value

    @model_validator(mode="before")
    @classmethod
    def validate_pix_key(cls, values: dict):
        pix_key_validator = PixKeyValidator(values.get("pix_key", None))
        pix_key_type = values.get("pix_key_type", None)

        if pix_key_type == "CPF" and not pix_key_validator.is_valid_cpf():
            raise ValueError("Invalid CPF")
        if pix_key_type == "CNPJ" and not pix_key_validator.is_valid_cnpj():
            raise ValueError("Invalid CNPJ")
        if pix_key_type == "PHONE" and not pix_key_validator.is_valid_phone():
            raise ValueError("Invalid Phone")
        if pix_key_type == "EMAIL" and not pix_key_validator.is_valid_email():
            raise ValueError("Invalid Email")
        if pix_key_type == "RANDOM" and not pix_key_validator.is_valid_random_key():
            raise ValueError("Invalid Random Key")
        return values


class BankAccountDataSchema(BankAccountBaseSchema):
    account_number: str
    bank_name: str
    branch_number: str
    account_type: str


# EXTERNAL SCHEMAS - API REQUESTS AND RESPONSES
class BankAccountUpdateSchema(BankAccountBaseSchema):
    pix_key_type: Optional[str] = None
    pix_key: Optional[str] = None


class BankAccountFilter(BaseModel):
    pix_key_type: Optional[str] = None
    pix_key: Optional[str] = None


# INTERNAL SCHEMAS - DATABASE OPERATIONS
class BankAccountCreateInDB(BankAccountDataSchema, BankAccountBaseSchema):
    beneficiary_id: int


class BankAccountUpdateInDB(BankAccountUpdateSchema):
    account_number: Optional[str]
    bank_name: Optional[str]
    branch_number: Optional[str]
    account_type: Optional[str]


class BankAccountModelSchema(BaseModel):
    id: int
    account_number: str
    bank_name: str
    branch_number: str
    account_type: str
    pix_key_type: str
    pix_key: str

    class Config:
        from_attributes = True
