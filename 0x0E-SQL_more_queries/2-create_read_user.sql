-- A script that creates the database hbtn_0d_2.

-- Create a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Create a database
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';

-- Grant select
GRANT SELECT ON hbtn_0d_2.* TO 'hbtn_0d_2'@'localhost';
