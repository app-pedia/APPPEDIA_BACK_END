"""initial database migration

Revision ID: e44c969270da
Revises: 
Create Date: 2020-06-07 16:55:10.269031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e44c969270da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('developer_name', sa.String(length=255), nullable=True),
    sa.Column('developer_public_id', sa.String(length=255), nullable=True),
    sa.Column('rating_total', sa.String(length=255), nullable=True),
    sa.Column('rating_average', sa.String(length=255), nullable=True),
    sa.Column('rating_five', sa.String(length=255), nullable=True),
    sa.Column('rating_four', sa.String(length=255), nullable=True),
    sa.Column('rating_three', sa.String(length=255), nullable=True),
    sa.Column('rating_two', sa.String(length=255), nullable=True),
    sa.Column('rating_one', sa.String(length=255), nullable=True),
    sa.Column('install', sa.String(length=255), nullable=True),
    sa.Column('install_link', sa.String(length=255), nullable=True),
    sa.Column('image_logo', sa.String(length=255), nullable=True),
    sa.Column('price', sa.String(length=255), nullable=True),
    sa.Column('update_date', sa.String(length=255), nullable=True),
    sa.Column('size', sa.String(length=255), nullable=True),
    sa.Column('version_current', sa.String(length=255), nullable=True),
    sa.Column('version_needs', sa.String(length=255), nullable=True),
    sa.Column('contents_grade', sa.String(length=255), nullable=True),
    sa.Column('interaction', sa.String(length=255), nullable=True),
    sa.Column('in_app_products', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=4095), nullable=True),
    sa.Column('related_name', sa.String(length=255), nullable=True),
    sa.Column('related_link', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('authority',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=True),
    sa.Column('application_public_id', sa.String(length=255), nullable=True),
    sa.Column('division', sa.String(length=255), nullable=True),
    sa.Column('detail', sa.String(length=511), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=511), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=True),
    sa.Column('user_email', sa.String(length=255), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.String(length=2047), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('developer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('web', sa.String(length=255), nullable=True),
    sa.Column('rating_total', sa.String(length=255), nullable=True),
    sa.Column('rating_average', sa.String(length=255), nullable=True),
    sa.Column('install_achieved', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=True),
    sa.Column('user_email', sa.String(length=255), nullable=True),
    sa.Column('application_public_id', sa.String(length=255), nullable=True),
    sa.Column('application_name', sa.String(length=255), nullable=True),
    sa.Column('application_category', sa.String(length=255), nullable=True),
    sa.Column('application_rating_average', sa.String(length=255), nullable=True),
    sa.Column('application_image_logo', sa.String(length=255), nullable=True),
    sa.Column('application_price', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('function',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=True),
    sa.Column('application_public_id', sa.String(length=255), nullable=True),
    sa.Column('detail', sa.String(length=511), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('record',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('user_email', sa.String(length=255), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.Column('device_name', sa.String(length=255), nullable=True),
    sa.Column('android_version', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('record')
    op.drop_table('function')
    op.drop_table('favorites')
    op.drop_table('developer')
    op.drop_table('contact')
    op.drop_table('blacklist_tokens')
    op.drop_table('authority')
    op.drop_table('application')
    # ### end Alembic commands ###
