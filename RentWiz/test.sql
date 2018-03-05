drop table if exists testTable;
create table testTable (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) 
);
INSERT INTO testTable (name) VALUES ("Dylan");