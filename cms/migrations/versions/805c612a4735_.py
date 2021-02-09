"""empty message

Revision ID: 805c612a4735
Revises: aa8e2fc15974
Create Date: 2021-02-08 05:48:40.351388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '805c612a4735'
down_revision = 'aa8e2fc15974'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
