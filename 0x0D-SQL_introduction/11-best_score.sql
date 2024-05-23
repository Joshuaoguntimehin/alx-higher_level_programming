-- script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

UPDATE `second_table`
set
`score` = 10
WHERE `second_table` . `name`= 'Bob';
