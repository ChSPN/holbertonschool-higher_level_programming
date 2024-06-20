-- This SQL statement creates the database 'hbtn_0d_usa' if it does not exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- This SQL statement sets the default database to 'hbtn_0d_usa'.
USE hbtn_0d_usa;

-- This SQL statement creates the table 'states' in the database 'hbtn_0d_usa'.
-- The table 'states' has two columns: 'id' of type INT that is unique, auto-generated, can't be null and is a primary key, and 'name' of type VARCHAR(256) that can't be null.
-- If the table 'states' already exists, the statement does nothing.
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
    name VARCHAR(256) NOT NULL
);
