from flask import Blueprint, request, jsonify, current_app
from app.models.tracked_transaction import TrackedTransaction
from app.models.known_addresses import KnownAddress

bp = Blueprint('get_tracked_transactions', __name__)

@bp.route('/get_tracked_transactions', methods=['GET'])
def get_tracked_transactions_by_victim_address():
    victim_address_query = request.args.get('victim_address')
    if not victim_address_query:
        return jsonify({"error": "No victim_address provided"}), 400

    session = current_app.config['SESSION']()

    # Fetch all tracked transactions with the given victim_address
    tracked_transactions = session.query(TrackedTransaction).filter_by(victim_address=victim_address_query).all()

    if not tracked_transactions:
        session.close()
        return jsonify({"error": "Tracked transactions not found for provided victim_address"}), 404

    # Group transactions by initial_tx_id
    transactions_by_initial = {}
    for tx in tracked_transactions:
        initial_tx_id = tx.initial_tx_id
        if initial_tx_id not in transactions_by_initial:
            transactions_by_initial[initial_tx_id] = []
        
        # Fetch known addresses
        known_from_address = session.query(KnownAddress).filter_by(address=tx.from_address).first()
        known_to_address = session.query(KnownAddress).filter_by(address=tx.to_address).first()

        transactions_by_initial[initial_tx_id].append({
            "tx_id": tx.transaction_id,
            "from_address": tx.from_address,
            "to_address": tx.to_address,
            "amount": float(tx.amount),
            "timestamp": tx.timestamp.isoformat(),
            "known_from_address": known_from_address.entity_name if known_from_address else None,
            "known_to_address": known_to_address.entity_name if known_to_address else None
        })

    session.close()

    return jsonify(transactions_by_initial)


