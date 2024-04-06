"""init

Revision ID: 7a6ea83379fb
Revises: 8ceccc376d0d
Create Date: 2024-04-06 11:19:27.533935

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a6ea83379fb'
down_revision: Union[str, None] = '8ceccc376d0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
