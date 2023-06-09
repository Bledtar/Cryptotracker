from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://ncu:AeWe3te9ei@localhost/Cryptotracker')
connection = sessionmaker(bind=engine)

# Is the main class for sqlalchemy to mapp all classes together
Base = declarative_base()

def connect():
    session = connection()
    return session


class Coins(Base):
    __tablename__ = 'coins'

    coinID = Column(Integer, primary_key=True)
    coin = Column(String(100), nullable=False)
    transactions = relationship('Transactions', back_populates='coin')

class Transactions(Base):
    __tablename__ = 'transactions'

    transactionID = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False) # the date I buyed it
    value = Column(Float(15), nullable=False) # How much money i spent
    quantity = Column(Float(15), nullable=False) # How much of the coin I purchased
    fees = Column(Float(15), nullable=False) # Fees Paied
    purchasePrice = Column(Float(15), nullable=False) # Actual Price of the Coin
    actualPrice = Column(Float(15), nullable=False) # After Fees
    coinID = Column(Integer, ForeignKey('coins.coinID'), nullable=False)
    coin = relationship('Coins', back_populates='transactions')

Base.metadata.create_all(engine)