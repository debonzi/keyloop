import sqlalchemy as sa

from .base import Base


__all__ = [
    "Realm",
]


class Realm(Base):
    __tablename__ = "realms"

    slug = sa.Column(sa.Text, unique=True, index=True)
    name = sa.Column(sa.Text)
    description = sa.Column(sa.Text, default="")
