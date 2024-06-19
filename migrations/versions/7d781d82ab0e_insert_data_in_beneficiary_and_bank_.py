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
        INSERT INTO beneficiary (id, name, email, cpf_cnpj, status, created_at, updated_at)
        VALUES 
            (1, 'Alice Johnson', 'ALICE.JOHNSON@EXAMPLE.COM', '164.512.834-54', 'validado', NOW(), NOW()),
            (2, 'Alice Johnson', 'ALICE.JOHNSON@EXAMPLE.COM', '24.458.563/9004-85', 'rascunho', NOW(), NOW()),
            (3, 'Carol White', 'CAROL.WHITE@EXAMPLE.COM', '240.481.032-88', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (4, 'David Brown', 'DAVID.BROWN@EXAMPLE.COM', '26.735.652/5688-04', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (5, 'Emma Wilson', 'EMMA.WILSON@EXAMPLE.COM', '368.496.134-00', 'validado', NOW(), NOW()),
            (6, 'Emma Wilson', 'EMMA.WILSON@EXAMPLE.COM', '94.062.452/2279-67', 'rascunho', NOW(), NOW()),
            (7, 'Grace Lee', 'GRACE.LEE@EXAMPLE.COM', '856.914.210-41', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (8, 'Henry Harris', 'HENRY.HARRIS@EXAMPLE.COM', '37.159.405/3186-30', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (9, 'Ivy Clark', 'IVY.CLARK@EXAMPLE.COM', '737.548.207-75', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (10, 'Jack Lewis', 'JACK.LEWIS@EXAMPLE.COM', '13.789.758/8160-77', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (11, 'Kathy Young', 'KATHY.YOUNG@EXAMPLE.COM', '546.837.149-23', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (12, 'Larry Walker', 'LARRY.WALKER@EXAMPLE.COM', '82.570.137/4631-50', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (13, 'Megan Hall', 'MEGAN.HALL@EXAMPLE.COM', '725.149.398-96', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (14, 'Nathan Allen', 'NATHAN.ALLEN@EXAMPLE.COM', '92.631.840/2144-51', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (15, 'Olivia King', 'OLIVIA.KING@EXAMPLE.COM', '560.498.017-38', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (16, 'Paul Wright', 'PAUL.WRIGHT@EXAMPLE.COM', '45.214.375/3068-41', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (17, 'Quincy Scott', 'QUINCY.SCOTT@EXAMPLE.COM', '189.064.352-20', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (18, 'Rachel Green', 'RACHEL.GREEN@EXAMPLE.COM', '87.461.920/3546-98', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (19, 'Steve Adams', 'STEVE.ADAMS@EXAMPLE.COM', '203.476.501-56', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (20, 'Tina Baker', 'TINA.BAKER@EXAMPLE.COM', '34.523.789/1425-10', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (21, 'Uma Reed', 'UMA.REED@EXAMPLE.COM', '968.142.835-71', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (22, 'Victor Morris', 'VICTOR.MORRIS@EXAMPLE.COM', '60.351.769/0542-49', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (23, 'Wendy Rogers', 'WENDY.ROGERS@EXAMPLE.COM', '431.570.498-82', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (24, 'Xander Brooks', 'XANDER.BROOKS@EXAMPLE.COM', '27.501.243/1359-60', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (25, 'Yara Gray', 'YARA.GRAY@EXAMPLE.COM', '754.908.216-34', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (26, 'Zachary Diaz', 'ZACHARY.DIAZ@EXAMPLE.COM', '67.135.982/9125-80', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (27, 'Angela Carter', 'ANGELA.CARTER@EXAMPLE.COM', '314.679.205-93', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (28, 'Brian Foster', 'BRIAN.FOSTER@EXAMPLE.COM', '36.752.490/1126-34', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (29, 'Clara Simmons', 'CLARA.SIMMONS@EXAMPLE.COM', '649.523.187-15', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW()),
            (30, 'Daniel Ward', 'DANIEL.WARD@EXAMPLE.COM', '11.246.378/8764-32', CASE WHEN RANDOM() < 0.5 THEN 'validado' ELSE 'rascunho' END, NOW(), NOW())
        """
    )


def downgrade() -> None:
    op.execute("DELETE FROM beneficiary WHERE id BETWEEN 1 AND 30")
