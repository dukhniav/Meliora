from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base, Session, relationship
from meliora.persistance.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Query, declarative_base, relationship, scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy.exc import NoSuchModuleError
from meliora.utils import OperationalException
from typing import Any, Dict, List, Optional
from pycoingecko import CoinGeckoAPI

_DECL_BASE: Any = declarative_base()
_SQL_DOCS_URL = 'http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls'

def init_db(db_url: str = 'sqlite:///meliora.sqlite') -> None:
    """
    Initializes this module with the given config,
    registers all known command handlers
    and starts polling for message updates
    :param db_url: Database to use
    :return: None
    """
    kwargs = {}

    if db_url == 'sqlite://':
        kwargs.update({
            'poolclass': StaticPool,
        })
    # Take care of thread ownership
    if db_url.startswith('sqlite://'):
        kwargs.update({
            'connect_args': {'check_same_thread': False},
        })

    try:
        engine = create_engine(db_url, future=True, **kwargs)
    except NoSuchModuleError:
        raise OperationalException(f"Given value for db_url: '{db_url}' "
                                   f"is no valid database URL! (See {_SQL_DOCS_URL})")

    # https://docs.sqlalchemy.org/en/13/orm/contextual.html#thread-local-scope
    # Scoped sessions proxy requests to the appropriate thread-local session.
    # We should use the scoped_session object - not a seperately initialized version
    Transaction._session = scoped_session(sessionmaker(bind=engine, autoflush=True))
    Transaction.query = Transaction._session.query_property()
    # Order.query = Trade._session.query_property()
    # PairLock.query = Trade._session.query_property()

    # previous_tables = inspect(engine).get_table_names()
    _DECL_BASE.metadata.create_all(engine)
    # check_migrate(engine, decl_base=_DECL_BASE, previous_tables=previous_tables)

    # # Clean dry_run DB if the db is not in-memory
    # if clean_open_orders and db_url != 'sqlite://':
    #     clean_dry_run_db()
    # # # TODO: add db name to config
    # # engine = create_engine(db_url)
    # # Base.metadata.create_all(engine, checkfirst=True)
    # # return sessionmaker(bind=engine)()


def cleanup_db() -> None:
    """
    Flushes all pending operations to disk.
    :return: None
    """
    Transaction.commit()


class Portfolio(_DECL_BASE):
    """
    Portfolio model

    Attributes:
        name (str): Portfolio name`.
    """
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Relationship
    assets = relationship("Asset", backref="portfolio")

    # def __init__(self, **kwargs):
    #     for key in kwargs:
    #         setattr(self, key, kwargs[key])
    #     self.recalc_open_trade_value()

    def __repr__(self):
        return f'Portfolio(id={self.id}, name={self.name}'


class Wallet(_DECL_BASE):
    """
    Wallet model

    Attributes:
        address (str): Public wallet address
        name (str): Wallet name
    """
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    name = Column(String)
    # Relationships
    assets = relationship('Asset', backref='wallet')

    def __repr__(self):
        return f'Wallet(id={self.id}, name={self.name}, address={self.address}'


class Network(_DECL_BASE):
    """
    Networks model

    Attributes:
        name (str): Network name
        url (str): Network explorer URL
    """
    __tablename__ = 'networks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    # Relationships
    coins = relationship('Asset', backref='network')

    def __repr__(self):
        return f'Network(id={self.id}, name={self.name}'


class Asset(_DECL_BASE):
    """
    Assets model

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.
    """
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contract = Column(String)
    balance = Column(Float)
    asset_type = Column(String)
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'))
    wallet_id = Column(Integer, ForeignKey('wallets.id'))
    network_id = Column(Integer, ForeignKey('networks.id'))
    # Relationships
    transactions = relationship('Transaction', backref='asset')

    def get_asset_name(self, cg: CoinGeckoAPI):
        coin_info = cg.get_coin_info_from_contract_address_by_id(self.contract)
        print("not implemented")


class Transaction(_DECL_BASE):
    """
    Transaction model
    """
    __tablename__ = 'transactions'

    hash = Column(String, primary_key=True, autoincrement='auto')
    asset_id = Column(Integer, ForeignKey('assets.id'))
    interacted_with = Column(String)
    quantity = Column(Float)
    value = Column(Float)
    fee = Column(Float)
    platform = Column(String)
    action = Column(String)
    method = Column(String)
    block = Column(Integer)
    when = Column(DateTime)

    def __repr__(self):
        return f'Transaction: {self.hash}'

    def fiat_value(self):
        return self.value * self.quantity

















