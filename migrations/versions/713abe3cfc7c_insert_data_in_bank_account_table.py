"""insert data in bank_account table

Revision ID: 713abe3cfc7c
Revises: 7d781d82ab0e
Create Date: 2024-06-15 18:24:12.794978

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "713abe3cfc7c"
down_revision: Union[str, None] = "7d781d82ab0e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO bank_account (beneficiary_id, account_number, pix_key_type, pix_key, bank_name, branch_number, created_at, updated_at)
        VALUES
            (1, '12345678', 'CPF', '123.456.789-00', 'Banco do Brasil', '1234', NOW(), NOW()),
            (2, '23456789', 'CNPJ', '12.345.678/0001-99', 'Caixa Econômica Federal', '5678', NOW(), NOW()),
            (3, '34567890', 'EMAIL', 'carol.white@example.com', 'Bradesco', '9101', NOW(), NOW()),
            (4, '45678901', 'PHONE_NUMBER', '+5511998765432', 'Itaú Unibanco', '1123', NOW(), NOW()),
            (5, '56789012', 'RANDOM_KEY', '123e4567-e89b-12d3-a456-426614174000', 'Santander', '4567', NOW(), NOW()),
            (6, '67890123', 'CPF', '234.567.890-12', 'Banco do Brasil', '8910', NOW(), NOW()),
            (7, '78901234', 'CNPJ', '23.456.789/0001-88', 'Caixa Econômica Federal', '2345', NOW(), NOW()),
            (8, '89012345', 'EMAIL', 'grace.lee@example.com', 'Bradesco', '6789', NOW(), NOW()),
            (9, '90123456', 'PHONE_NUMBER', '+5511987654321', 'Itaú Unibanco', '3456', NOW(), NOW()),
            (10, '01234567', 'RANDOM_KEY', '123e4567-e89b-12d3-a456-426614174001', 'Santander', '7890', NOW(), NOW()),
            (11, '12345679', 'CPF', '345.678.901-23', 'Banco do Brasil', '4567', NOW(), NOW()),
            (12, '23456780', 'CNPJ', '34.567.890/0001-77', 'Caixa Econômica Federal', '8910', NOW(), NOW()),
            (13, '34567891', 'EMAIL', 'megan.hall@example.com', 'Bradesco', '1234', NOW(), NOW()),
            (14, '45678902', 'PHONE_NUMBER', '+5511976543210', 'Itaú Unibanco', '5678', NOW(), NOW()),
            (15, '56789013', 'RANDOM_KEY', '123e4567-e89b-12d3-a456-426614174002', 'Santander', '9101', NOW(), NOW()),
            (16, '67890124', 'CPF', '456.789.012-34', 'Banco do Brasil', '2345', NOW(), NOW()),
            (17, '78901235', 'CNPJ', '45.678.901/0001-66', 'Caixa Econômica Federal', '6789', NOW(), NOW()),
            (18, '89012346', 'EMAIL', 'rachel.green@example.com', 'Bradesco', '3456', NOW(), NOW()),
            (19, '90123457', 'PHONE_NUMBER', '+5511965432109', 'Itaú Unibanco', '7890', NOW(), NOW()),
            (20, '01234568', 'RANDOM_KEY', '123e4567-e89b-12d3-a456-426614174003', 'Santander', '4567', NOW(), NOW()),
            (21, '12345670', 'CPF', '567.890.123-45', 'Banco do Brasil', '8910', NOW(), NOW()),
            (22, '23456781', 'CNPJ', '56.789.012/0001-55', 'Caixa Econômica Federal', '1234', NOW(), NOW()),
            (23, '34567892', 'EMAIL', 'wendy.rogers@example.com', 'Bradesco', '5678', NOW(), NOW()),
            (24, '45678903', 'PHONE_NUMBER', '+5511954321098', 'Itaú Unibanco', '9101', NOW(), NOW()),
            (25, '56789014', 'RANDOM_KEY', '123e4567-e89b-12d3-a456-426614174004', 'Santander', '2345', NOW(), NOW()),
            (26, '67890125', 'CPF', '678.901.234-56', 'Banco do Brasil', '6789', NOW(), NOW()),
            (27, '78901236', 'CNPJ', '67.890.123/0001-44', 'Caixa Econômica Federal', '3456', NOW(), NOW()),
            (28, '89012347', 'EMAIL', 'brian.foster@example.com', 'Bradesco', '7890', NOW(), NOW()),
            (29, '90123458', 'PHONE_NUMBER', '+5511943210987', 'Itaú Unibanco', '4567', NOW(), NOW()),
            (30, '01234569', 'RANDOM_KEY', '123e4567-e89b-12d3-a456-426614174005', 'Santander', '8910', NOW(), NOW()
        )
        """
    )


def downgrade() -> None:
    op.execute("DELETE FROM bank_account WHERE id BETWEEN 1 AND 30")
