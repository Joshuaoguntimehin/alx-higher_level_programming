#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to MySQL
    """
    Connects to a MySQL database and lists all states in ascending order by id.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database_name (str): The name of the database to connect to.
    """
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=username,
                             passwd=password, db=database_name)
        cursor = db.cursor()
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        states = cursor.fetchall()
        for state in states:
            print(state)


        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
