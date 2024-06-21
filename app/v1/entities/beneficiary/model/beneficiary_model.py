from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.v1.database.db import Base
from ..schemas.beneficiary_schemas import BeneficiaryModelSchema


class BeneficiaryModel(Base):
    __tablename__ = "beneficiary"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(250), nullable=False)
    cpf_cnpj = Column(String, nullable=False)
    status = Column(String, nullable=False, default="rascunho")
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())

    def to_dict(self, **kwargs):
        _data = BeneficiaryModelSchema(
            id=self.id,
            name=self.name,
            email=self.email,
            cpf_cnpj=self.cpf_cnpj,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

        return _data.model_dump(**{**kwargs})
