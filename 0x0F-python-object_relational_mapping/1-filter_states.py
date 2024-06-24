#!/usr/bin/python3
""" import statement """
import MySQLdb
import sys
"""placing value"""

if __name__ == "__main__":
    db = MySQLdb.connect(host = "localhost", port = 3306 , user=sys.argv[1], 
                         passwd=sys.argv[2], db =sys.argv[3] )
    cur = db.cursor()
    cur.execute("SELECT name FROM states WHERE name LIKE 'N%' ORDER BY name ASC;")
    count = 1

    query_rows = cur.fetchall()
    for row in query_rows:
        print(f"{(count)}{row}")
        count += 1
    cur.close()
    db.close()
