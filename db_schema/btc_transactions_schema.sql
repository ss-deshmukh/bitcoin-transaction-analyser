-- btc_transactions_schema.sql

CREATE TABLE btc_transactions (
    id SERIAL PRIMARY KEY,
    tx_id  VARCHAR(255) NOT NULL,
    from_address VARCHAR(255) NOT NULL,
    to_address VARCHAR(255) NOT NULL,
    amount DECIMAL NOT NULL,
    timestamp DATE NOT NULL
);
