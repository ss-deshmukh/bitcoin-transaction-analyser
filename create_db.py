# create_db.py

from app import Base
from app.models import (BitcoinAddress, BitcoinTransaction, KnownAddress,
                        TrackedTransaction)
from config import DATABASE_URL
from sqlalchemy import Column, Date, Integer, Sequence, String, create_engine
from sqlalchemy.orm import declarative_base

if not DATABASE_URL:
    raise ValueError("No DATABASE_URL found. Please check your configuration.")

engine = create_engine(DATABASE_URL)

# Create the table
Base.metadata.create_all(engine)

print("Database table created successfully.")
