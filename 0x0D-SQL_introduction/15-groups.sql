--A script that lists the number of records with the same score in the table.

SELECT COUNT(*) AS `number`, `score` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
