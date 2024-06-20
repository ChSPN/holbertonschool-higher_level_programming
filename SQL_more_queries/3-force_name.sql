-- This SQL statement creates the table 'force_name' on the MySQL server.
-- The table 'force_name' has two columns: 'id' of type INT and 'name' of type VARCHAR(256) that can't be null.
-- If the table 'force_name' already exists, the statement does nothing.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
