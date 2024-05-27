from sqlalchemy import Column, String, Integer, Date
from app import Base

class BitcoinAddress(Base):
    __tablename__ = 'btc_addresses'

    address = Column(String, primary_key=True)
    times_in_mixer = Column(Integer)
    criminal_activities = Column(Integer)
    high_volume_transactions = Column(Integer)
    last_active_date = Column(Date)