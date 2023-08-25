"""empty message

Revision ID: b694b354b717
Revises: 
Create Date: 2023-07-30 18:36:26.319286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b694b354b717'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('datasets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('file_name', sa.String(length=120), nullable=False),
    sa.Column('file_columns', sa.ARRAY(sa.String(length=120)), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('calculations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('column_name', sa.String(length=120), nullable=False),
    sa.Column('benford_law_distribution', sa.JSON(), nullable=False),
    sa.Column('rows_count', sa.Integer(), nullable=False),
    sa.Column('skipped_rows_count', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calculations')
    op.drop_table('datasets')
    # ### end Alembic commands ###