-- A script that converts hbtn_0c_0 database to UTF8.

USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;

