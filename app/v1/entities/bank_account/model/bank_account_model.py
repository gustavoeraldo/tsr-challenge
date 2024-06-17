from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.v1.database.db import Base


class BankAccountModel(Base):
    __tablename__ = "bank_account"

    id = Column(Integer, primary_key=True, index=True)
    beneficiary_id = Column(Integer, ForeignKey("beneficiary.id"), nullable=False)
    account_number = Column(String(10), nullable=False)
    pix_key_type = Column(String(20), nullable=False)
    pix_key = Column(String(250), nullable=False)
    bank_name = Column(String(50), nullable=False)
    branch_number = Column(String(10), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())

    beneficiary_relation = relationship("BeneficiaryModel")
