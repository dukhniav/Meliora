"""SQLAlchemy Data Models."""
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, DateTime, Float
from sqlalchemy.sql import func

from meliora.persistance.database import engine

_DECL_BASE = declarative_base()


class Coin(_DECL_BASE):
    """Coin model"""

    __tablename__ = "coins"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    symbol = Column(String(255), unique=True, nullable=False)
    price = Column(Float, nullable=False)


class CoinInfo(_DECL_BASE):
    """Coin info model"""

    __tablename__ = "coin_info"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    symbol = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    bio = Column(Text)
    avatar_url = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return "<User %r>" % self.username


_DECL_BASE.metadata.create_all(engine)
