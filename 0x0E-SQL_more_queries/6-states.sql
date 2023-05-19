-- A script that creates the database hbtn_0d_usa and table states.

CREATE DATABASE IN NOT EXISTS hbtn_0d_usa;

-- Use the db.
USE hbtn_0d_usa;

-- Create the table.
CREATE TABLE IF NOT EXISTS states(
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
        );
