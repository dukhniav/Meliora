"""Database engine & session creation."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    """Database class"""
    def __init__(self, db_path):
        self.engine = create_engine(
            'sqlite:///data/'+db_path,
            future=True
        )
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
