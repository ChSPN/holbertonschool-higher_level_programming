-- This SQL statement creates the table 'unique_id' on the MySQL server.
-- The table 'unique_id' has two columns: 'id' of type INT with the default value 1 and must be unique, and 'name' of type VARCHAR(256).
-- If the table 'unique_id' already exists, the statement does nothing.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
