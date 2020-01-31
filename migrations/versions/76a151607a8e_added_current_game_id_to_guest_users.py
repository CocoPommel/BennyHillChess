"""added current game ID to guest users

Revision ID: 76a151607a8e
Revises: edfc20513439
Create Date: 2020-01-22 13:10:22.639552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76a151607a8e'
down_revision = 'edfc20513439'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('current_game', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'current_game')
    # ### end Alembic commands ###
