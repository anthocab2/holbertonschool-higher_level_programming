-- Creates the table unique_id.
-- Creates the table if it does not exist with a unique id.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
