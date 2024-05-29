
from app import Base
from sqlalchemy import Column, String


class KnownAddress(Base):
    __tablename__ = 'known_addresses'
    address = Column(String, primary_key=True)
    entity_name = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)