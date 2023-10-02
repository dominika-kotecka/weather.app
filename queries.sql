-- Create DB
CREATE DATABASE pogoda

-- Create table for Kraków
CREATE TABLE krakow (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  temp INT,
  min_temp INT,
  max_temp INT,
  humidity INT, 
  pressure INT,
  description VARCHAR(100),
  date VARCHAR(100)
)

-- Select All
SELECT * FROM krakow