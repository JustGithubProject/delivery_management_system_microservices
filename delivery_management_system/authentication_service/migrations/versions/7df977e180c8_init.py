"""init

Revision ID: 7df977e180c8
Revises: c2604a35a07c
Create Date: 2024-04-06 11:19:21.433365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7df977e180c8'
down_revision: Union[str, None] = 'c2604a35a07c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
