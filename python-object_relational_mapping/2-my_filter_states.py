#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials, database name, and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name,
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select states with the specified name
    query = (
        "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC".format(
            state_name
        )
    )
    cursor.execute(query)

    # Fetch all the rows from the executed query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
