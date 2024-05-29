from flask import Blueprint, request, jsonify, current_app
from app.models.bitcoin_transaction import BitcoinTransaction
from app.models.tracked_transaction import TrackedTransaction

bp = Blueprint('track_transaction', __name__)
    
@bp.route('/track_transaction', methods=['POST'])
def track_transaction():
    data = request.get_json()
    initial_tx_id = data.get('tx_id')
    victim_address = data.get('victim_address')


    if not initial_tx_id:
        return jsonify({"error": "No initial transaction ID provided"}), 400

    session = current_app.config['SESSION']()

    btc_tx = session.query(BitcoinTransaction).filter_by(tx_id=initial_tx_id)

    # Fetch initial transaction details
    if not btc_tx:
        return jsonify({"error": "Bitcoin transaction not found"}), 404
    
    if victim_address != btc_tx.from_address:
        return jsonify({"error": "Victim address was not part of the tx"}), 400



    initial_transaction = TrackedTransaction(
        transaction_id=initial_tx_id,
        initial_tx_id=initial_tx_id,
        victim_address=victim_address
    )

    session.add(initial_transaction)
    session.commit()

    session.close()

    return jsonify({"tracked_transactions": initial_transaction})


""" 
curl -X POST http://localhost:5000/track_transaction \
     -H "Content-Type: application/json" \
     -d '{
           "tx_id": "tx_1",
           "victim_address": "1VictimXxxXxxXxxXxxXxxXxxXxxXxxXxxX"
         }'

 """