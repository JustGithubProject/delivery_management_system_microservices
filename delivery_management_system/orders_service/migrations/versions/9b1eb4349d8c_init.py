"""init

Revision ID: 9b1eb4349d8c
Revises: 7a6ea83379fb
Create Date: 2024-04-06 11:27:33.664208

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b1eb4349d8c'
down_revision: Union[str, None] = '7a6ea83379fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
