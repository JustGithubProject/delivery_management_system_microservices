"""init

Revision ID: 3846f85d53cf
Revises: 7df977e180c8
Create Date: 2024-04-06 11:27:42.460856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3846f85d53cf'
down_revision: Union[str, None] = '7df977e180c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
