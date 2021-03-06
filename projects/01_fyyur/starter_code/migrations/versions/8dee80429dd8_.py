"""empty message

Revision ID: 8dee80429dd8
Revises: 750c3caf62ee
Create Date: 2020-10-21 23:51:39.252822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dee80429dd8'
down_revision = '750c3caf62ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('genres', sa.Column('name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('genres', 'name')
    # ### end Alembic commands ###
