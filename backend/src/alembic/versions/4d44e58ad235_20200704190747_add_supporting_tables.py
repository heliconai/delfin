"""add supporting tables

Revision ID: 4d44e58ad235
Revises: c458e74ef509
Create Date: 2020-07-04 19:07:47.692423-04:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4d44e58ad235'
down_revision = 'c458e74ef509'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('datamodality',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('data_modality', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_datamodality_id'), 'datamodality', ['id'], unique=False)
    op.create_table('annotationtypes',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('data_modality_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('annotation_type', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['data_modality_id'], ['datamodality.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_annotationtypes_data_modality_id'), 'annotationtypes', ['data_modality_id'], unique=False)
    op.create_index(op.f('ix_annotationtypes_id'), 'annotationtypes', ['id'], unique=False)
    op.create_table('labeloptions',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('annotation_type_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('labels', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['annotation_type_id'], ['annotationtypes.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_labeloptions_id'), 'labeloptions', ['id'], unique=False)
    op.create_index(op.f('ix_labeloptions_project_id'), 'labeloptions', ['project_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_labeloptions_project_id'), table_name='labeloptions')
    op.drop_index(op.f('ix_labeloptions_id'), table_name='labeloptions')
    op.drop_table('labeloptions')
    op.drop_index(op.f('ix_annotationtypes_id'), table_name='annotationtypes')
    op.drop_index(op.f('ix_annotationtypes_data_modality_id'), table_name='annotationtypes')
    op.drop_table('annotationtypes')
    op.drop_index(op.f('ix_datamodality_id'), table_name='datamodality')
    op.drop_table('datamodality')
    # ### end Alembic commands ###
