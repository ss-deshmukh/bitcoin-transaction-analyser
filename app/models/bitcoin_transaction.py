from app import Base
from sqlalchemy import DECIMAL, Column, DateTime, String


class BitcoinTransaction(Base):
    __tablename__ = 'btc_transactions'
    
    tx_id = Column(String, primary_key=True)
    from_address = Column(String, nullable=False)
    to_address = Column(String, nullable=False)
    amount = Column(DECIMAL, nullable=False)
    timestamp = Column(DateTime, nullable=False)