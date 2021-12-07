"""Database engine & session creation."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'sqlite:///data/meliora.db',
    #echo=True,
    future=True
)
Session = sessionmaker(bind=engine)
session = Session()
