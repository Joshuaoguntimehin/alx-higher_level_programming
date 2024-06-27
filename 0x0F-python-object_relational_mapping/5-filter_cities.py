#!/usr/bin/python3
import MySQLdb
import sys

def list_cities(username, password, db, state_name):
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                charset='utf8'
                )

        cursor = db.cursor()
        query = "SELECT id, name FROM cities WHERE state_name = %s ORDER BY id ASC"

        cursor.execute(query, (state_name,))
        results = cursor.fetchall()

        if row in result:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Closing database connection
        if db:
            db.close()

if __name__=="__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        list_cities(username, password, database, state_name)
