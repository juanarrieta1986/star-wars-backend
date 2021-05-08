"""empty message

Revision ID: b40845acefaf
Revises: b3bc07a680e9
Create Date: 2021-05-08 21:15:13.026162

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b40845acefaf'
down_revision = 'b3bc07a680e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('cGUID', postgresql.UUID(as_uuid=True), nullable=False))
    op.add_column('planets', sa.Column('pGUID', sa.String(length=60), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planets', 'pGUID')
    op.drop_column('characters', 'cGUID')
    # ### end Alembic commands ###