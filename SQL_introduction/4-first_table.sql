-- This SQL statement creates a new table named 'first_table' if it does not already exist.
-- The table has two columns: 'id' of type INT and 'name' of type VARCHAR(256).
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
