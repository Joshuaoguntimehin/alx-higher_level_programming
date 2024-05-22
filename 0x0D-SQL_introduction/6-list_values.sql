-- script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

SELECT TABLE_NAME
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0';
