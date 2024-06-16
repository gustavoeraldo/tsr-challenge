from pydantic import BaseModel, field_validator, model_validator

from app.v1.helpers import PixKeyValidator


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
    def validate_pix_key(cls, values):
        pix_key_validator = PixKeyValidator(values["pix_key"])

        if values["pix_key_type"] == "CPF" and not pix_key_validator.is_valid_cpf():
            raise ValueError("Invalid CPF")
        if values["pix_key_type"] == "CNPJ" and not pix_key_validator.is_valid_cnpj():
            raise ValueError("Invalid CNPJ")
        if values["pix_key_type"] == "PHONE" and not pix_key_validator.is_valid_phone():
            raise ValueError("Invalid Phone")
        if values["pix_key_type"] == "EMAIL" and not pix_key_validator.is_valid_email():
            raise ValueError("Invalid Email")
        if (
            values["pix_key_type"] == "RANDOM"
            and not pix_key_validator.is_valid_random_key()
        ):
            raise ValueError("Invalid Random Key")
        return values


class BankAccountCreateInDB(BankAccountBaseSchema):
    beneficiary_id: int
    account_number: str
    bank_name: str
    branch_number: str
