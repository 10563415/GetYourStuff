"""merging two heads

Revision ID: f686e69250e8
Revises: f3c88c1966eb, 635b9e0a304b
Create Date: 2021-07-15 21:28:49.098074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f686e69250e8'
down_revision = ('f3c88c1966eb', '635b9e0a304b')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
