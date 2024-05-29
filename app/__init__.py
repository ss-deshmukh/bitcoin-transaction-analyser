from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import DATABASE_URL

# Initialize SQLAlchemy components
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*"}})
    if not DATABASE_URL:
        raise ValueError("No DATABASE_URL found. Please check your configuration.")

    # Register Blueprints
    from app.routes.address import bp as address_bp
    from app.routes.get_address_transactions import bp as get_address_transactions_bp
    from app.routes.get_tracked_transactions import bp as get_tracked_transactions_bp
    from app.routes.track_transaction import bp as track_transaction_bp
    app.register_blueprint(address_bp)
    app.register_blueprint(get_address_transactions_bp)
    app.register_blueprint(get_tracked_transactions_bp)
    app.register_blueprint(track_transaction_bp)

    # Store session and engine in app config for later use
    app.config['SESSION'] = Session
    app.config['ENGINE'] = engine
    app.config['CORS_HEADERS'] = 'Content-Type'

    return app