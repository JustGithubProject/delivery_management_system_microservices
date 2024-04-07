from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7df977e180c8'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create an `user` table
    op.create_table('user',
        sa.Column('id', postgresql.UUID(), nullable=False),
        sa.Column('username', sa.String(length=50), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('password_hash', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Create an `session` table
    op.create_table('session',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', postgresql.UUID(), nullable=True),
        sa.Column('token', sa.String(), nullable=False),
        sa.Column('expires_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    # Drop `session` table first due to the foreign key constraint
    op.drop_table('session')
    # Drop `user` table
    op.drop_table('user')
