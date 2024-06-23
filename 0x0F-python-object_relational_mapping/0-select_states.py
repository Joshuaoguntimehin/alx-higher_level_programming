#!/usr/bin/python3
from MySQLdb import _mysql
import sys

db=_mysql.connect(host='Localhost',
                  user=sys.argv[1],
                  password=sys.argv[2],
                  database = sys.argv[3] ,
                  port = 3306)
query = "SELECT * FROM states ORDER BY id ASC"
c = database.curser()
c.execcute("select * from status")
row = c.fetchall()
for row in rows:
    print(row)
c.close()
datebase.close()


