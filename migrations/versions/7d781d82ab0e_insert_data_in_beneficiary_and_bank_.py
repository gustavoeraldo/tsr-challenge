"""insert data in beneficiary table

Revision ID: 7d781d82ab0e
Revises: 9cee2aadf707
Create Date: 2024-06-15 17:59:57.138835

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7d781d82ab0e"
down_revision: Union[str, None] = "9cee2aadf707"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO beneficiary (id, name, email, status, created_at, updated_at)
        VALUES 
            (1, 'Alice Johnson', 'ALICE.JOHNSON@EXAMPLE.COM', 'validado', NOW(), NOW()),
            (2, 'Alice Johnson', 'ALICE.JOHNSON@EXAMPLE.COM', 'rascunho', NOW(), NOW()),
            (3, 'Carol White', 'CAROL.WHITE@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (4, 'David Brown', 'DAVID.BROWN@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (5, 'Emma Wilson', 'EMMA.WILSON@EXAMPLE.COM', 'validado', NOW(), NOW()),
            (6, 'Emma Wilson', 'EMMA.WILSON@EXAMPLE.COM', 'rascunho', NOW(), NOW()),
            (7, 'Grace Lee', 'GRACE.LEE@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (8, 'Henry Harris', 'HENRY.HARRIS@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (9, 'Ivy Clark', 'IVY.CLARK@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (10, 'Jack Lewis', 'JACK.LEWIS@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (11, 'Kathy Young', 'KATHY.YOUNG@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (12, 'Larry Walker', 'LARRY.WALKER@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (13, 'Megan Hall', 'MEGAN.HALL@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (14, 'Nathan Allen', 'NATHAN.ALLEN@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (15, 'Olivia King', 'OLIVIA.KING@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (16, 'Paul Wright', 'PAUL.WRIGHT@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (17, 'Quincy Scott', 'QUINCY.SCOTT@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (18, 'Rachel Green', 'RACHEL.GREEN@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (19, 'Steve Adams', 'STEVE.ADAMS@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (20, 'Tina Baker', 'TINA.BAKER@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (21, 'Uma Reed', 'UMA.REED@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (22, 'Victor Morris', 'VICTOR.MORRIS@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (23, 'Wendy Rogers', 'WENDY.ROGERS@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (24, 'Xander Brooks', 'XANDER.BROOKS@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (25, 'Yara Gray', 'YARA.GRAY@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (26, 'Zachary Diaz', 'ZACHARY.DIAZ@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (27, 'Angela Carter', 'ANGELA.CARTER@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (28, 'Brian Foster', 'BRIAN.FOSTER@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (29, 'Clara Simmons', 'CLARA.SIMMONS@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (30, 'Daniel Ward', 'DANIEL.WARD@EXAMPLE.COM', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()
        )
        """
    )


def downgrade() -> None:
    op.execute("DELETE FROM beneficiary WHERE id BETWEEN 1 AND 30")
