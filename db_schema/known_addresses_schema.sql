-- known_addresses_schema.sql

CREATE TABLE known_addresses (
    id SERIAL PRIMARY KEY,
    address VARCHAR(255) UNIQUE NOT NULL,
    entity_name VARCHAR NOT NULL,
    entity_type VARCHAR NOT NULL
);
