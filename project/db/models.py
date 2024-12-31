from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()

class Costumer(Base):
    __tablename__ = 'costumers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    card_number = Column(Integer)
    balance = Column(Float)
    status = Column(String)