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

# Fetch the DATABASE_URL from environment variables
DATABASE_URL = os.getenv('HEROKU_POSTGRESQL_CHARCOAL_URL')  # This should be set in your Heroku app's config vars

# Adjust the URL if it starts with 'postgres://' to be 'postgresql://'
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

if not DATABASE_URL:
    raise ValueError("No DATABASE_URL found. Please check your configuration.")

engine = create_engine(DATABASE_URL)

# Create the table
Base.metadata.create_all(engine)

print("Database table created successfully.")
