"""primeira migrate

Revision ID: 489a4d2cb84d
Revises: 
Create Date: 2025-05-21 22:56:40.336938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '489a4d2cb84d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contato',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_envio', sa.DateTime(), nullable=True),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('assunto', sa.String(length=50), nullable=True),
    sa.Column('menssagem', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contato')
    # ### end Alembic commands ###
