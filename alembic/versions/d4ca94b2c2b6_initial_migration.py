"""Initial migration

Revision ID: d4ca94b2c2b6
Revises: 
Create Date: 2025-11-06 17:22:15.580309

"""
from sqlalchemy import text

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4ca94b2c2b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### Create currencies table ###
    op.create_table(
        'currencies',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('code', sa.String(length=3), nullable=False, unique=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('rate', sa.Float(), nullable=False),
    )
    # ### Create conversions table ###
    op.create_table(
        'conversions',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, index=True),
        sa.Column('base_currency', sa.String(length=3), nullable=False),
        sa.Column('target_currency', sa.String(length=3), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('result', sa.Float(), nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False),
    )


def downgrade():
    op.drop_table('conversions')
    op.drop_table('currencies')
