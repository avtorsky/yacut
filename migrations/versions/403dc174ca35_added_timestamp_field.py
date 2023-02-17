"""added timestamp field

Revision ID: 403dc174ca35
Revises: 
Create Date: 2023-02-17 09:38:36.512010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '403dc174ca35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('url_map', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_url_map_timestamp'), 'url_map', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_url_map_timestamp'), table_name='url_map')
    op.drop_column('url_map', 'timestamp')
    # ### end Alembic commands ###