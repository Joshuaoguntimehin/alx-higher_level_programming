#!/usr/bin/python3
"""import statement"""
import MySQLdb
import sys

"""commmand for printing cities.id"""


def list_cities(username, password, database):
    try:
        # Connect to MySQL database
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object using cursor() method
        cur = conn.cursor()

        # Prepare and execute the SQL query
        cur.execute("SELECT id, name FROM cities ORDER BY id ASC")

        # Fetch all the rows in a list of tuples
        query_rows = cur.fetchall()

        # Display the results
        for row in query_rows:
            print(row)

        # Close the cursor
        cur.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        # Closing database connection
        if conn:
            conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_cities(username, password, database)
