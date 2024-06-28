#!/usr/bin/python3
import MySQLdb
import sys


def list_cities(mysql_username, mysql_password, database_name, state_name):
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        
        # Create a cursor object
        cursor = db.cursor()
        
        # SQL query to select cities in the specified state, avoiding SQL injection
        query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        
        # Execute the query
        cursor.execute(query, (state_name,))
        
        # Fetch all the results
        results = cursor.fetchall()
        
        # Format the results
        cities = [city[1] for city in results]
        print(", ".join(cities))
    
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
    
    finally:
        # Ensure the cursor and database connection are closed
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} mysql_username mysql_password database_name state_name".format(sys.argv[0]))
        sys.exit(1)
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    
    list_cities(mysql_username, mysql_password, database_name, state_name)