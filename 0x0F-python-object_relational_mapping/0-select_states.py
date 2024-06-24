#!/usr/bin/python3
import MySQLdb
import sys
***print in id ***

def list_states(username, password, database_name):
    # Connect to MySQL
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=username,
                             passwd=password, db=database_name)
        cursor = db.cursor()

        # Execute the query
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all the rows and print them
        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close cursor and connection
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
