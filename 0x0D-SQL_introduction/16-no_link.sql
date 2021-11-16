-- script lists all records of second_table
-- of hbtn_0c_0 databse in your NYSQL server
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
