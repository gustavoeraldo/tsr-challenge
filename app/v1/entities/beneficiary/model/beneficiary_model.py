from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.v1.database.db import Base


class BeneficiaryModel(Base):
    __tablename__ = "beneficiary"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(250), nullable=False)
    cpf_cnpj = Column(String, nullable=False)
    status = Column(String, nullable=False, default="rascunho")
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())
