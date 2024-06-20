-- This SQL statement creates the database 'hbtn_0d_usa' if it does not exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- This SQL statement sets the default database to 'hbtn_0d_usa'.
USE hbtn_0d_usa;

-- This SQL statement creates the table 'cities' in the database 'hbtn_0d_usa'.
-- The table 'cities' has three columns: 'id' of type INT that is unique, auto-generated, can't be null and is a primary key, 'state_id' of type INT that can't be null and is a foreign key that references the 'id' column of the 'states' table, and 'name' of type VARCHAR(256) that can't be null.
-- If the table 'cities' already exists, the statement does nothing.
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
