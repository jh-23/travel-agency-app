"""added email to Traveler table

Revision ID: 80710a442050
Revises: 6178c3f7cf8a
Create Date: 2024-08-04 15:52:59.894277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80710a442050'
down_revision = '6178c3f7cf8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('travelers', schema=None) as batch_op:
        batch_op.alter_column('_password_hash',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=128),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('travelers', schema=None) as batch_op:
        batch_op.alter_column('_password_hash',
               existing_type=sa.String(length=128),
               type_=sa.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###
