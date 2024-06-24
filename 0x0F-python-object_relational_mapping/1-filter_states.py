#!/usr/bin/python3
""" import statement """
import MySQLdb
import sys

"""placing value"""
db = MySQLdb.connect(host = "localhost", port = 3306 , user=sys.argv[1], 
                   passwd=sys.argv[2], db =sys.argv[3] )
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
cur.execute("SELECT name FROM states WHERE name LIKE 'N%';")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()