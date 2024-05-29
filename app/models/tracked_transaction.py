from app import Base
from sqlalchemy import Column, String


class TrackedTransaction(Base):
    __tablename__ = 'tracked_transactions'
    tx_id = Column(String, nullable=False, primary_key=True)
    from_address= Column(String, nullable=False)
    to_address = Column(String, nullable=False)
    initial_tx_id = Column(String, nullable=False)
    victim_address = Column(String, nullable=False)
