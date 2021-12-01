"""SQLAlchemy Data Models."""
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import false
from sqlalchemy.types import Integer, Text, String, DateTime, Float
from sqlalchemy.sql import func

from meliora.persistance.database import engine

_DECL_BASE = declarative_base()


class Coin(_DECL_BASE):
    """Coin model"""

    __tablename__ = "coins"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    symbol = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.symbol


class Exchanges(_DECL_BASE):
    """Exchange model"""

    __tablename__ = "exchanges"

    exchange_id = Column(Integer,primary_key=True, autoincrement="auto")
    name = Column(String(250), nullable=false)

class Wallets(_DECL_BASE):
    """Wallets model"""
    __tablename__ = "wallets"
    wallet_id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(250), nullable=False)


class Ledger(_DECL_BASE):
    """Ledger model"""
    __tablename__ = "ledger"
    symbol_id = Column(Float, primary_key=True, autoincrement="auto")
    transaction_id = Column(Float, nullable=False)
    quantity = Column(Float, nullable=False)
    wallet_id = Column(Float, nullable=False)
    assets = Column(Float, nullable=False)
    exchange_id = Column(Float, nullable=False)


class Portfolio(_DECL_BASE):
    """Portfolio model"""
    __tablename__ = "portfolio"
    wallet_id = Column(Float, primary_key=True, autoincrement="auto")
    assets = Column(Float, nullable=False)


class Transactions(_DECL_BASE):
    """Transactions model"""
    __tablename__ = "transactions"

    trans_id = Column(Integer, primary_key=True, autoincrement="auto")
    symbol_id = Column(String(255), unique=True, nullable=False)
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    fees = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    source = Column(String(250), nullable=False)
    destination = Column(String(250), nullable=False)
    exchange_id = Column(Integer, nullable=False)
    ledger_id = Column(Integer, nullable=False)
    link = Column(String(250), nullable=False)
    when = Column(DateTime, nullable=False)


_DECL_BASE.metadata.create_all(engine)
