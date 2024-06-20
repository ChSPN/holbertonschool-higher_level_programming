-- This SQL statement creates a new table 'second_table' if it does not already exist.
-- The table has three columns: 'id' of type INT, 'name' of type VARCHAR(256), and 'score' of type INT.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- These SQL statements insert new rows into 'second_table'.
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
