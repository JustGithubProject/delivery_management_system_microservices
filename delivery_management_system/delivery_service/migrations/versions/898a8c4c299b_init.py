"""init

Revision ID: 898a8c4c299b
Revises: 15b923b3321a
Create Date: 2024-04-06 11:19:25.115158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '898a8c4c299b'
down_revision: Union[str, None] = '15b923b3321a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
