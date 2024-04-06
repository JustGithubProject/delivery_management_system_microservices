"""init

Revision ID: 1ff7a8950909
Revises: 99d5917742ab
Create Date: 2024-04-06 11:19:26.433980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ff7a8950909'
down_revision: Union[str, None] = '99d5917742ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
