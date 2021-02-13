"""empty message

Revision ID: 0797c93baed6
Revises: a2dd174add0c
Create Date: 2021-02-13 05:58:29.176625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0797c93baed6'
down_revision = 'a2dd174add0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('StoryProposal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reporter', sa.String(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('initialHeadline', sa.String(), nullable=True),
    sa.Column('possibleIssues', sa.String(), nullable=True),
    sa.Column('initialLead', sa.String(), nullable=True),
    sa.Column('contextOfStory', sa.String(), nullable=True),
    sa.Column('institutionsToVisit', sa.String(), nullable=True),
    sa.Column('listOfMaterial', sa.String(), nullable=True),
    sa.Column('listOfPeople', sa.String(), nullable=True),
    sa.Column('listOfExpert', sa.String(), nullable=True),
    sa.Column('nameOfExpert', sa.String(), nullable=True),
    sa.Column('suggestionMedia', sa.String(), nullable=True),
    sa.Column('section', sa.String(), nullable=True),
    sa.Column('draftID', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('StoryProposal')
    # ### end Alembic commands ###
