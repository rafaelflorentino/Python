create database zooflask;
use zooflask;
create table animal(
  id int primary key auto_increment,
  nome_popular varchar(80) NOT NULL,
  nome_cientifico varchar(60) NOT NULL,
  habitos_noturnos LONGTEXT NOT NULL
)

CREATE TABLE avaliacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(255) NOT NULL,
    polaridade FLOAT NOT NULL
);