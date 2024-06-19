"""create beneficiary table

Revision ID: 133962d1058a
Revises: 
Create Date: 2024-06-14 17:31:29.092605

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "133962d1058a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "beneficiary",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(250), nullable=False),
        sa.Column("email", sa.String(250), nullable=False),
        sa.Column("cpf_cnpj", sa.String(25), nullable=False),
        sa.Column("status", sa.String, nullable=False, server_default="rascunho"),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.Column(
            "updated_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
    )

    op.create_index(op.f("ix_beneficiary_id"), "beneficiary", ["id"], unique=False)


def downgrade() -> None:
    op.drop_table("beneficiary")
