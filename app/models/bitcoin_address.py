from app import Base
from sqlalchemy import Column, Date, Integer, String


class BitcoinAddress(Base):
    __tablename__ = 'btc_addresses'

    address = Column(String, primary_key=True)
    times_in_mixer = Column(Integer)
    criminal_activities = Column(Integer)
    high_volume_transactions = Column(Integer)
    last_active_date = Column(Date)