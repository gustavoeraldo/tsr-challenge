from pydantic import BaseModel


class BeneficiaryItemMapper(BaseModel):
    id: int
    name: str
    cpf_cnpj: str
    status: str
    pix_key_type: str
    pix_key: str
    bank_name: str
    branch_number: str
    account_number: str
    account_type: str
