"""init

Revision ID: 9d7817564aa0
Revises: 1ff7a8950909
Create Date: 2024-04-06 11:27:43.056129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d7817564aa0'
down_revision: Union[str, None] = '1ff7a8950909'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
