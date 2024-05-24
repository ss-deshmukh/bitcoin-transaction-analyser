# app.py
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from create_db import BitcoinAddress  # Ensure create_db.py is in the same directory

app = Flask(__name__)

Base = declarative_base()

# Database setup
DATABASE_URL = os.getenv('HEROKU_POSTGRESQL_CHARCOAL_URL')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@app.route('/get_address', methods=['GET'])
def get_address():
    address_query = request.args.get('address')
    if not address_query:
        return jsonify({"error": "No address provided"}), 400

    session = Session()
    address_data = session.query(BitcoinAddress).filter_by(address=address_query).first()
    session.close()

    if address_data:
        return jsonify({
            "address": address_data.address,
            "times_in_mixer": address_data.times_in_mixer,
            "criminal_activities": address_data.criminal_activities,
            "high_volume_transactions": address_data.high_volume_transactions,
            "last_active_date": address_data.last_active_date.isoformat()
        })
    else:
        return jsonify({"error": "Address not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
