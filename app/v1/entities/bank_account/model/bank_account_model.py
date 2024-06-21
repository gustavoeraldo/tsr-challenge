from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.v1.database.db import Base
from ..bank_account_schemas import BankAccountModelSchema


class BankAccountModel(Base):
    __tablename__ = "bank_account"

    id = Column(Integer, primary_key=True, index=True)
    beneficiary_id = Column(Integer, ForeignKey("beneficiary.id"), nullable=False)
    account_type = Column(String(10), nullable=False)
    account_number = Column(String(10), nullable=False)
    pix_key_type = Column(String(20), nullable=False)
    pix_key = Column(String(250), nullable=False)
    bank_name = Column(String(50), nullable=False)
    branch_number = Column(String(10), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())

    beneficiary_relation = relationship("BeneficiaryModel", backref="beneficiary")

    def to_dict(self, **kwargs):
        _data = BankAccountModelSchema(
            id=self.id,
            beneficiary_id=self.beneficiary_id,
            account_type=self.account_type,
            account_number=self.account_number,
            pix_key_type=self.pix_key_type,
            pix_key=self.pix_key,
            bank_name=self.bank_name,
            branch_number=self.branch_number,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

        return _data.model_dump(**{**kwargs})
