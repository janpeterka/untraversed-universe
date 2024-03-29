"""Add locations

Revision ID: 5b1e3bfbec77
Revises: 35c7b5b2c9d6
Create Date: 2023-07-13 13:04:37.775567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5b1e3bfbec77"
down_revision = "35c7b5b2c9d6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "locations",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("category", sa.String(length=255), nullable=False),
        sa.Column("coordinate_x", sa.Integer(), nullable=True),
        sa.Column("coordinate_y", sa.Integer(), nullable=True),
        sa.Column("coordinate_z", sa.Integer(), nullable=True),
        sa.Column("planet_id", sa.Integer(), nullable=True),
        sa.Column("town_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["planet_id"],
            ["locations.id"],
        ),
        sa.ForeignKeyConstraint(
            ["town_id"],
            ["locations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("locations")
    # ### end Alembic commands ###
