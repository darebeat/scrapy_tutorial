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

drop table if exists t_courses;
CREATE TABLE t_courses (                          
   id bigint NOT NULL AUTO_INCREMENT,  
   title varchar(255) DEFAULT NULL,              
   `url` varchar(255) DEFAULT NULL,                
   pic varchar(255) DEFAULT NULL,                
   teacher varchar(32) DEFAULT NULL,             
   `time` varchar(16) DEFAULT NULL,                
   price varchar(16) DEFAULT NULL,               
   PRIMARY KEY (id)                              
 );


drop table if exists t_hr;
CREATE TABLE t_hr (                          
   id bigint unsigned NOT NULL AUTO_INCREMENT,  
   title varchar(255) DEFAULT NULL,              
   location varchar(32) DEFAULT NULL,                
   type varchar(32) DEFAULT NULL,                
   is_valid varchar(32) DEFAULT NULL,             
   duty text DEFAULT NULL,                
   updatetime varchar(20) DEFAULT NULL,               
   PRIMARY KEY (id)                              
);