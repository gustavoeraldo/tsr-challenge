"""create bank_account table

Revision ID: 9cee2aadf707
Revises: 133962d1058a
Create Date: 2024-06-15 15:32:20.254169

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9cee2aadf707"
down_revision: Union[str, None] = "133962d1058a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "bank_account",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "beneficiary_id",
            sa.Integer,
            sa.ForeignKey("beneficiary.id"),
            nullable=False,
        ),
        sa.Column("account_number", sa.String(50), nullable=False),
        sa.Column("pix_key_type", sa.String(50), nullable=False),
        sa.Column("pix_key", sa.String(50), nullable=False, unique=True),
        sa.Column("bank_name", sa.String(50), nullable=False),
        sa.Column("branch_number", sa.String(50), nullable=False),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.Column(
            "updated_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
    )

    # Create index
    op.create_index(op.f("ix_bank_account_id"), "bank_account", ["id"], unique=True)

    op.create_index(op.f("ix_pix_key"), "bank_account", ["pix_key"], unique=True)


def downgrade() -> None:
    op.drop_table("bank_account")
