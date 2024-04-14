"""Initial migration

Revision ID: 9a14e989403a
Revises:
Create Date: 2022-01-01 12:00:00

"""

from alembic import op
import sqlalchemy as sa

# Assuming `StatusDelivery` is an enum with some predefined values like NEW, IN_PROGRESS, etc.
status_delivery_values = ['NEW', 'IN_PROGRESS', 'DELIVERED', 'CANCELLED']
status_delivery_name = 'statusdelivery'

# revision identifiers, used by Alembic.
revision = '9a14e989403a'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Check if the enum type `statusdelivery` does not exist, then create it
    if not enum_exists():
        op.execute(f"CREATE TYPE {status_delivery_name} AS ENUM ('NEW', 'IN_PROGRESS', 'DELIVERED', 'CANCELLED')")

    # Create `delivery_order` table
    op.create_table('delivery_order',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('order_id', sa.String(length=36), nullable=True),
        sa.Column('delivery_address', sa.String(), nullable=True),
        sa.Column('status', sa.Enum(*status_delivery_values, name=status_delivery_name), nullable=True, default='NEW'),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    # Drop `delivery_order` table
    op.drop_table('delivery_order')

    # Drop the enum type `statusdelivery` if it exists
    if enum_exists():
        op.execute(f"DROP TYPE {status_delivery_name}")

def enum_exists() -> bool:
    # Check if the enum type `statusdelivery` exists in the database
    conn = op.get_bind()
    query = f"""
        SELECT EXISTS (
            SELECT 1 FROM pg_type WHERE typname = '{status_delivery_name}' AND typtype = 'e'
        )
    """
    result = conn.execute(sa.text(query))
    return result.scalar()
