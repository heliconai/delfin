"""add baseline tables

Revision ID: 19eeed8c4808
Revises:
Create Date: 2020-07-15 22:37:28.589874-04:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import app

# revision identifiers, used by Alembic.
revision = '19eeed8c4808'
down_revision = None
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
    op.create_table('datasets',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('instructions', sa.String(), nullable=True),
    sa.Column('data_modality', sa.String(), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_datasets_id'), 'datasets', ['id'], unique=False)
    op.create_index(op.f('ix_datasets_name'), 'datasets', ['name'], unique=False)
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
    op.create_table('data',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('dataset_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('properties', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('scopes', app.models.util.CastingArray(postgresql.JSONB(astext_type=sa.Text())), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_dataset_id'), 'data', ['dataset_id'], unique=False)
    op.create_index(op.f('ix_data_id'), 'data', ['id'], unique=False)
    op.create_index(op.f('ix_data_name'), 'data', ['name'], unique=False)
    op.create_table('labeloptions',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('dataset_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('annotation_type_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('labels', app.models.util.CastingArray(postgresql.JSONB(astext_type=sa.Text())), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['annotation_type_id'], ['annotationtypes.id'], ),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_labeloptions_dataset_id'), 'labeloptions', ['dataset_id'], unique=False)
    op.create_index(op.f('ix_labeloptions_id'), 'labeloptions', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_labeloptions_id'), table_name='labeloptions')
    op.drop_index(op.f('ix_labeloptions_dataset_id'), table_name='labeloptions')
    op.drop_table('labeloptions')
    op.drop_index(op.f('ix_data_name'), table_name='data')
    op.drop_index(op.f('ix_data_id'), table_name='data')
    op.drop_index(op.f('ix_data_dataset_id'), table_name='data')
    op.drop_table('data')
    op.drop_index(op.f('ix_annotationtypes_id'), table_name='annotationtypes')
    op.drop_index(op.f('ix_annotationtypes_data_modality_id'), table_name='annotationtypes')
    op.drop_table('annotationtypes')
    op.drop_index(op.f('ix_datasets_name'), table_name='datasets')
    op.drop_index(op.f('ix_datasets_id'), table_name='datasets')
    op.drop_table('datasets')
    op.drop_index(op.f('ix_datamodality_id'), table_name='datamodality')
    op.drop_table('datamodality')
    # ### end Alembic commands ###