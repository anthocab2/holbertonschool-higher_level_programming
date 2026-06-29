-- Creates the table force_name.
-- Creates the table if it does not exist with a NOT NULL name column.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
