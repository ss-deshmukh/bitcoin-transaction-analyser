-- btc_addresses_schema.sql

CREATE TABLE btc_addresses (
    id SERIAL PRIMARY KEY,
    address VARCHAR(255) UNIQUE NOT NULL,
    times_in_mixer INTEGER NOT NULL,
    criminal_activities INTEGER NOT NULL,
    high_volume_transactions INTEGER NOT NULL,
    last_active_date DATE NOT NULL
);
