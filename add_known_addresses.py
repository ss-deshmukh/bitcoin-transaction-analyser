import json

from app.models.known_addresses import KnownAddress
from config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if not DATABASE_URL:
    raise ValueError("No DATABASE_URL found. Please check your configuration.")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

with open('known_addresses.json', 'r') as file:
    known_addresses = json.load(file)

for addr in known_addresses:
    new_known_address = KnownAddress(
        address=addr['address'],
        entity_name=addr['entity_name'],
        entity_type=addr['entity_type']
    )
    session.add(new_known_address)

try:
    session.commit()
    print("Known addresses successfully inserted into the database.")
except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()
