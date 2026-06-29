-- Creates the table id_not_null.
-- Creates the table if it does not exist with a default value for id.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
