# /app/app.py
from flask import Flask

# creating the app.py to create a endpoint for all routes in flask

from routes.address import bp as address
from routes.get_address_transactions import bp as get_address_transactions
from routes.get_tracked_transactions import bp as get_tracked_transactions
from routes.track_transaction import bp as track_transaction  # Assume you have another Blueprint in user_routes.py

app = Flask(__name__)

# Register the Blueprints
app.register_blueprint(address)
app.register_blueprint(get_address_transactions)
app.register_blueprint(get_tracked_transactions)
app.register_blueprint(track_transaction)

if __name__ == '__main__':
    app.run(debug=True)
