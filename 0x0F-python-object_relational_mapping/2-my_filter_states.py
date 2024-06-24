#!/usr/bin/python3
""" import statement """
import MySQLdb
import sys
"""placing value"""


def search_states(username, password, database, state_name):
    # Connect to MySQL database
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    # Create a cursor object using cursor() metho
    cursor = conn.cursor()

    # Prepare SQL query with user input using format
    query = "SELECT * FROM states WHERE name LIKE %s  ORDER BY id ASC"

    # Execute the SQL query
    cursor.execute(query, (state_name + '%',))

    # Fetch all the rows in a list of tuples
    results = cursor.fetchall()
    for row in results:
        print(row)
        cursor.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, database, state_name)
