"""add base tables

Revision ID: c458e74ef509
Revises:
Create Date: 2020-07-04 19:05:03.998024-04:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import app

# revision identifiers, used by Alembic.
revision = 'c458e74ef509'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('instructions', sa.String(), nullable=True),
    sa.Column('data_modality', sa.String(), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_projects_id'), 'projects', ['id'], unique=False)
    op.create_index(op.f('ix_projects_name'), 'projects', ['name'], unique=False)
    op.create_table('data',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('properties', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('scopes', app.models.data.CastingArray(postgresql.JSONB(astext_type=sa.Text())), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_id'), 'data', ['id'], unique=False)
    op.create_index(op.f('ix_data_name'), 'data', ['name'], unique=False)
    op.create_index(op.f('ix_data_project_id'), 'data', ['project_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_data_project_id'), table_name='data')
    op.drop_index(op.f('ix_data_name'), table_name='data')
    op.drop_index(op.f('ix_data_id'), table_name='data')
    op.drop_table('data')
    op.drop_index(op.f('ix_projects_name'), table_name='projects')
    op.drop_index(op.f('ix_projects_id'), table_name='projects')
    op.drop_table('projects')
    # ### end Alembic commands ###