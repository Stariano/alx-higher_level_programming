-- A script that creates the database hbtn_0d_usa and table cities.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the db.
USE hbtn_0d_usa;

-- Create the table.
CREATE TABLE IF NOT EXISTS cities(
        id INT UNIQUE NOT NULL UNIQUE AUTO_INCREMENT,
        state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFRENCES states(id),
        PRIMARY KEY (id)
        );
