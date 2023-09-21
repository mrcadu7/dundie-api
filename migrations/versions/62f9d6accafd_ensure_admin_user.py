"""ensure_admin_user

Revision ID: 62f9d6accafd
Revises: 17fca5233f37
Create Date: 2023-09-19 20:51:37.467806

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

from dundie.models.user import User
from sqlmodel import Session

# revision identifiers, used by Alembic.
revision = '62f9d6accafd'
down_revision = '17fca5233f37'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    admin = User(
        name="Admin",
        username="admin",
        email="admin@dm.com",
        dept="management",
        currency="USD",
        password="admin",  # pyright: ignore
    )
    # if admin user already exists it will raise IntegrityError
    try:
        session.add(admin)
        session.commit()
    except sa.exc.IntegrityError:
        session.rollback()


def downgrade() -> None:
    pass
