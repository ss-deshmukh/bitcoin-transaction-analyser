# create_db.py

from sqlalchemy import create_engine, Column, Integer, String, Date, Sequence
from sqlalchemy.orm import declarative_base
from config import DATABASE_URL

Base = declarative_base()

class BitcoinAddress(Base):
    __tablename__ = 'btc_addresses'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    address = Column(String(255), unique=True, nullable=False)
    times_in_mixer = Column(Integer, nullable=False)
    criminal_activities = Column(Integer, nullable=False)
    high_volume_transactions = Column(Integer, nullable=False)
    last_active_date = Column(Date, nullable=False)


if not DATABASE_URL:
    raise ValueError("No DATABASE_URL found. Please check your configuration.")

engine = create_engine(DATABASE_URL)

# Create the table
Base.metadata.create_all(engine)

print("Database table created successfully.")
