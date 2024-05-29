from flask import Blueprint, request, jsonify, current_app
from app.models.bitcoin_address import BitcoinAddress

bp = Blueprint('address', __name__)

@bp.route('/get_address', methods=['GET'])
def get_address():
    address_query = request.args.get('address')
    if not address_query:
        return jsonify({"error": "No address provided"}), 400

    session = current_app.config['SESSION']()
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