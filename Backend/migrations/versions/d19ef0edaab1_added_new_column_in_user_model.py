"""added new column in user model

Revision ID: d19ef0edaab1
Revises: b35512888358
Create Date: 2024-03-18 11:48:37.394636

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd19ef0edaab1'
down_revision = 'b35512888358'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Public_Id', sa.String(length=100), nullable=True))
        batch_op.alter_column('Email',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.create_unique_constraint(None, ['Public_Id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('Email',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('Public_Id')

    # ### end Alembic commands ###
