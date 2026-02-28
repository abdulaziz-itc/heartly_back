"""Add missing fields to medicalorganization

Revision ID: 5c94a010a422
Revises: 0f276939ee5b
Create Date: 2026-02-28 07:18:28.183396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c94a010a422'
down_revision: Union[str, Sequence[str], None] = '0f276939ee5b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('medicalorganization', sa.Column('brand', sa.String(), nullable=True))
    op.add_column('medicalorganization', sa.Column('director_name', sa.String(), nullable=True))
    op.add_column('medicalorganization', sa.Column('contact_phone', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('medicalorganization', 'contact_phone')
    op.drop_column('medicalorganization', 'director_name')
    op.drop_column('medicalorganization', 'brand')
