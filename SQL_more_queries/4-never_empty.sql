-- This SQL statement creates the table 'id_not_null' on the MySQL server.
-- The table 'id_not_null' has two columns: 'id' of type INT with the default value 1 and 'name' of type VARCHAR(256).
-- If the table 'id_not_null' already exists, the statement does nothing.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
