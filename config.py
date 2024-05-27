

import os

DATABASE_URL = os.getenv('HEROKU_POSTGRESQL_CHARCOAL_URL')

"""Local Dev DB"""
if not DATABASE_URL: 
    DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/wycheck"

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)



