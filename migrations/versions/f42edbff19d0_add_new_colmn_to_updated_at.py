"""Add new colmn to updated_at

Revision ID: f42edbff19d0
Revises: fd6cde06ba9c
Create Date: 2024-12-27 19:16:43.040482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f42edbff19d0'
down_revision: Union[str, None] = 'fd6cde06ba9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    # ### end Alembic commands ###
