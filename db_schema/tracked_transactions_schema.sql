-- tracked_transactions_schema.sql

CREATE TABLE tracked_transactions (
    id SERIAL PRIMARY KEY,
    tx_id VARCHAR(255) NOT NULL,
    initial_tx_id VARCHAR(255) NOT NULL,
    victim_address VARCHAR(255) NOT NULL,
    from_address VARCHAR(255) NOT NULL,
    to_address VARCHAR(255) NOT NULL,
    UNIQUE (tx_id, initial_tx_id, victim_address)
);
