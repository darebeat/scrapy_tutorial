use test;

drop table if exists t_author;
create table t_author(
  id bigint NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255),
  birthdate VARCHAR(255),
  bio varchar(2000),
  PRIMARY KEY (`id`)
);

drop table if exists t_douban;
create table t_douban (
  id bigint NOT NULL AUTO_INCREMENT,
  item_id bigint,
  item_name varchar(100),
  `url` varchar(255),
  info varchar(2000),
  rating decimal(2,1),
  comment int,
  PRIMARY KEY (`id`)
);