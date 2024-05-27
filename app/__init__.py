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
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    if not DATABASE_URL:
        raise ValueError("No DATABASE_URL found. Please check your configuration.")

    # Register Blueprints
    from app.routes.address import bp as address_bp
    app.register_blueprint(address_bp)

    # Store session and engine in app config for later use
    app.config['SESSION'] = Session
    app.config['ENGINE'] = engine

    return app