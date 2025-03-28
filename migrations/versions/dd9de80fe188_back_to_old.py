"""back to old

Revision ID: dd9de80fe188
Revises: 4db184aab12d
Create Date: 2025-03-17 23:18:09.559268

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dd9de80fe188'
down_revision = '4db184aab12d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=postgresql.BYTEA(),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=255),
               type_=postgresql.BYTEA(),
               existing_nullable=False)

    # ### end Alembic commands ###
