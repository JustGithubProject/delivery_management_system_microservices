"""init

Revision ID: 9a14e989403a
Revises: 898a8c4c299b
Create Date: 2024-04-06 11:27:30.130988

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a14e989403a'
down_revision: Union[str, None] = '898a8c4c299b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
