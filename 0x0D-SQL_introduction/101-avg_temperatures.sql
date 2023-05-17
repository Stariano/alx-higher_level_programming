-- Displays the average temperature (in Fahrenheit) by city ordered by descending temperature.

`hbtn_0c_0` < temperatures.sql

SELECT `city`, avg(`value`) AS `avg_temp` FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;  
