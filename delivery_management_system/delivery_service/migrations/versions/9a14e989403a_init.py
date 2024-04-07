from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Assuming `StatusDelivery` is an enum with some predefined values like NEW, IN_PROGRESS, etc.
# You should replace `NEW`, `IN_PROGRESS`, etc. with the actual statuses in your `StatusDelivery` enum.
status_delivery_enum = postgresql.ENUM('NEW', 'IN_PROGRESS', 'DELIVERED', 'CANCELLED', name='statusdelivery', create_type=False)

# revision identifiers, used by Alembic.
revision = '9a14e989403a'
down_revision = '898a8c4c299b'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create the enum type for `StatusDelivery` if not exists
    status_delivery_enum.create(op.get_bind(), checkfirst=True)

    # Create `delivery_order` table
    op.create_table('delivery_order',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('order_id', sa.String(length=36), nullable=True),
        sa.Column('delivery_address', sa.String(), nullable=True),
        sa.Column('status', sa.Enum('NEW', 'IN_PROGRESS', 'DELIVERED', 'CANCELLED', name='statusdelivery'), nullable=True, default='NEW'),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    # Drop `delivery_order` table
    op.drop_table('delivery_order')

    # Drop the enum type for `StatusDelivery`. Note: This might need to be handled carefully if other tables use the same enum type.
    status_delivery_enum.drop(op.get_bind(), checkfirst=True)
