"""first_migration_all_new

Revision ID: 38cb5731123f
Revises: 
Create Date: 2019-12-16 18:05:59.309224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38cb5731123f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('subcategories',
    sa.Column('subcategory_id', sa.Integer(), nullable=False),
    sa.Column('subcategory_name', sa.String(length=64), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.category_id'], ),
    sa.PrimaryKeyConstraint('subcategory_id')
    )
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=100), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('subcategory_id', sa.Integer(), nullable=True),
    sa.Column('short_product_description', sa.String(length=200), nullable=True),
    sa.Column('product_description', sa.String(length=2000), nullable=True),
    sa.Column('product_dimensions', sa.String(length=100), nullable=True),
    sa.Column('power_wattage', sa.String(length=100), nullable=True),
    sa.Column('product_color', sa.String(length=100), nullable=True),
    sa.Column('price_USD', sa.Float(), nullable=True),
    sa.Column('amazon_link', sa.String(length=2000), nullable=True),
    sa.Column('aliexpress_link', sa.String(length=2000), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.category_id'], ),
    sa.ForeignKeyConstraint(['subcategory_id'], ['subcategories.subcategory_id'], ),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('imagesandvideos',
    sa.Column('imgandvid_id', sa.Integer(), nullable=False),
    sa.Column('imgOrvid_link', sa.String(length=400), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('imgandvid_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('imagesandvideos')
    op.drop_table('products')
    op.drop_table('subcategories')
    op.drop_table('categories')
    # ### end Alembic commands ###