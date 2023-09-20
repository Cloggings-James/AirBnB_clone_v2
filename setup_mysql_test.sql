-- Create a database
CREATE DATABASE mydatabase;

-- Use the database
USE mydatabase;

-- Create a table
CREATE TABLE mytable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Insert data into the table
INSERT INTO mytable (name) VALUES ('John');
INSERT INTO mytable (name) VALUES ('Jane');

