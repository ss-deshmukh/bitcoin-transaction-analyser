# insert_data.py

import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import BitcoinAddress  # Importing the BitcoinAddress class from create_db.py

# Connect to the database
DATABASE_URL = os.getenv('HEROKU_POSTGRESQL_CHARCOAL_URL')  # Make sure to set this environment variable
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Load data from the JSON file
with open('btc_addresses.json', 'r') as file:
    btc_addresses = json.load(file)

# Insert data into the database
for address in btc_addresses:
    new_address = BitcoinAddress(
        address=address['address'],
        times_in_mixer=address['times_in_mixer'],
        criminal_activities=address['criminal_activities'],
        high_volume_transactions=address['high_volume_transactions'],
        last_active_date=address['last_active_date']
    )
    session.add(new_address)

try:
    session.commit()
    print("Data successfully inserted into the database.")
except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()
