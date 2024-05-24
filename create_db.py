# create_db.py

from sqlalchemy import create_engine, Column, Integer, String, Date, Sequence
from sqlalchemy.orm import declarative_base
import os

Base = declarative_base()

class BitcoinAddress(Base):
    __tablename__ = 'btc_addresses'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    address = Column(String(255), unique=True, nullable=False)
    times_in_mixer = Column(Integer, nullable=False)
    criminal_activities = Column(Integer, nullable=False)
    high_volume_transactions = Column(Integer, nullable=False)
    last_active_date = Column(Date, nullable=False)

# Connect to the database
DATABASE_URL = os.getenv('HEROKU_POSTGRESQL_CHARCOAL_URL')  # Make sure to set this environment variable
engine = create_engine(DATABASE_URL)

# Create the table
Base.metadata.create_all(engine)

print("Database table created successfully.")
