import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.bitcoin_transaction import BitcoinTransaction
from app.models.tracked_transaction import TrackedTransaction

from config import DATABASE_URL

if not DATABASE_URL:
    raise ValueError("No DATABASE_URL found. Please check your configuration.")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

with open('./demo_txs/2.victim_to_thief.json', 'r') as file:
    btc_transactions = json.load(file)

for tx in btc_transactions:
    from_address = tx['from_address']
    tx_id = tx['tx_id']
    to_address = tx['to_address']

    new_btc_tx = BitcoinTransaction(
        tx_id=tx_id,
        from_address=from_address,
        to_address=to_address,
        amount=tx['amount'],
        timestamp=tx['timestamp']
    )

     # Check if the from_address is being tracked
    tracked_transaction = session.query(TrackedTransaction).filter_by(to_address=from_address).first()
    if tracked_transaction:
        new_tracked_transaction = TrackedTransaction(
            transaction_id=tx_id,
            initial_tx_id=tracked_transaction.initial_tx_id,
            to_address=to_address,
        )
        session.add(new_tracked_transaction)
    session.add(new_btc_tx)

try:
    session.commit()
    print("Data successfully inserted into the database.")
except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()
