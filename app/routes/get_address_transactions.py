from flask import Blueprint, request, jsonify, current_app
from app.models.bitcoin_transaction import BitcoinTransaction

bp = Blueprint('get_address_transactions', __name__)

@bp.route('/get_address_transactions', methods=['GET'])
def get_transaction_by_from_address():
    from_address_query = request.args.get('address')
    print(from_address_query)
    if not from_address_query:
        return jsonify({"error": "No from_address provided"}), 400

    session = current_app.config['SESSION']()
    transactions = session.query(BitcoinTransaction).filter_by(from_address=from_address_query).all()
    session.close()

    if transactions:
        transaction_list = [{
            "tx_id": tx.tx_id,
            "from_address": tx.from_address,
            "to_address": tx.to_address,
            "amount": float(tx.amount),
            "timestamp": tx.timestamp.isoformat()
        } for tx in transactions]
        return jsonify(transaction_list)
    else:
        return jsonify({"error": "Transactions not found for provided from_address"}), 404
