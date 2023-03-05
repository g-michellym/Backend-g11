"""agregue tabla maestro y seccion

Revision ID: fad1c3eab8b7
Revises: 664caab73238
Create Date: 2023-03-04 22:44:20.022662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fad1c3eab8b7'
down_revision = '664caab73238'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maestros',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('apellidos', sa.Text(), nullable=True),
    sa.Column('correo', sa.Text(), nullable=False),
    sa.Column('direccion', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('secciones',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('alumnos', sa.Integer(), nullable=True),
    sa.Column('nivel_id', sa.Integer(), nullable=False),
    sa.Column('maestro_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['maestro_id'], ['maestros.id'], ),
    sa.ForeignKeyConstraint(['nivel_id'], ['niveles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('secciones')
    op.drop_table('maestros')
    # ### end Alembic commands ###
