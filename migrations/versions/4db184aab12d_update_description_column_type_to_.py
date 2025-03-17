"""Update description column type to LargeBinary

Revision ID: 4db184aab12d
Revises: 755e41231cae
Create Date: 2025-03-17 22:23:37.515379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4db184aab12d'
down_revision = '755e41231cae'
branch_labels = None
depends_on = None


def upgrade():
    # Change the `description` column to `BYTEA`
    op.alter_column(
        'todos',  # the table name
        'description',  # the column name
        type_=sa.LargeBinary(),  # change the column type to BYTEA (LargeBinary)
        postgresql_using='description::bytea'  # tell PostgreSQL how to cast existing data
    )

def downgrade():
    # Revert the `description` column to `TEXT`
    op.alter_column(
        'todos',  # the table name
        'description',  # the column name
        type_=sa.String(),  # change the column type to TEXT or VARCHAR
        postgresql_using='description::text'  # cast back to text if needed
    )