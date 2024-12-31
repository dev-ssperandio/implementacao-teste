from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = "sqlite+pysqlite:///project/db/database.db"
engine = create_engine(DB_PATH)

Session = sessionmaker(bind=engine)
session = Session()
