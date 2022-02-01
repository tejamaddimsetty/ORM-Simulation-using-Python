-- Creation of DB
CREATE DATABASE stud;

-- Creation of Table
create table records(
   id INT NOT NULL,
   name VARCHAR(100) NOT NULL,
   age int(40) NOT NULL,
   PRIMARY KEY ( id )
);

-- Project Table
create table record(
   id INT NOT NULL,
   name VARCHAR(100) NOT NULL,
   class VARCHAR(100) NOT NULL,
   age int(40) NOT NULL,
   school VARCHAR(100) NOT NULL,
   PRIMARY KEY ( id )
);