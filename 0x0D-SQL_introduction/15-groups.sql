-- script lists number of records with the same score
-- in second_table of hbtn_0c_0 database in your MYSQL server
SELECT score, COUNT(score) AS number
FROM second_table GROUP BY score ORDER BY score DESC;
