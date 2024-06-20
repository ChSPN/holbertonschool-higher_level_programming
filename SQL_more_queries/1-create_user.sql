-- This SQL statement creates the MySQL server user 'user_0d_1' with the password 'user_0d_1_pwd'.
-- If the user 'user_0d_1' already exists, the statement does nothing.
-- The user 'user_0d_1' is granted all privileges on the MySQL server.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
