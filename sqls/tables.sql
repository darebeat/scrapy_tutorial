use test;

drop table if exists t_author;
create table t_author(
  id bigint NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255),
  birthdate VARCHAR(255),
  bio text,
  PRIMARY KEY (id)
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
  PRIMARY KEY (id)
);

drop table if exists t_douban_book;
CREATE TABLE t_douban_book (
  id bigint(20) unsigned NOT NULL COMMENT 'ID号',
  title varchar(255) DEFAULT NULL COMMENT '书名',
  author varchar(64) DEFAULT NULL COMMENT '作者',
  press varchar(255) DEFAULT NULL COMMENT '出版社',
  original varchar(255) DEFAULT NULL COMMENT '原作名',
  translator varchar(128) DEFAULT NULL COMMENT '译者',
  imprint varchar(128) DEFAULT NULL COMMENT '出版年',
  pages int(10) unsigned DEFAULT NULL COMMENT '页数',
  price double(6,2) unsigned DEFAULT NULL COMMENT '定价',
  binding varchar(32) DEFAULT NULL COMMENT '装帧',
  series varchar(128) DEFAULT NULL COMMENT '丛书',
  isbn varchar(128) DEFAULT NULL COMMENT 'ISBN',
  score varchar(128) DEFAULT NULL COMMENT '评分',
  number int(10) unsigned DEFAULT NULL COMMENT '评论人数',
  PRIMARY KEY (id)
);

drop table if exists t_douban_music;
create table t_douban_music (
  id bigint NOT NULL AUTO_INCREMENT,
  music_name text,
  music_alias text,
  music_singer text,
  music_time text,
  music_rating text,
  music_votes text,
  music_tags text,
  music_url text,
  PRIMARY KEY (id)
);

drop table if exists t_douban_music_review;
create table t_douban_music_review (
  id bigint NOT NULL AUTO_INCREMENT,
  review_title text,
  review_content text,
  review_author text,
  review_music text,
  review_time text,
  review_url text,
  PRIMARY KEY (id)
);

drop table if exists t_douban_video;
create table t_douban_video (
  id bigint NOT NULL AUTO_INCREMENT,
  video_name text,
  video_alias text,
  video_actor text,
  video_year text,
  video_time text,
  video_rating text,
  video_votes text,
  video_tags text,
  video_url text,
  video_director text,
  video_type text,
  video_bigtype text,
  video_area text,
  video_language text,
  video_length text,
  video_writer text,
  video_desc text,
  video_episodes text,
  PRIMARY KEY (id)
);

drop table if exists t_douban_video_review;
create table t_douban_video_review (
  id bigint NOT NULL AUTO_INCREMENT,
  review_title text,
  review_content text,
  review_author text,
  review_video text,
  review_time text,
  review_url text,
  PRIMARY KEY (id)
);
  

drop table if exists t_course;
CREATE TABLE t_course (
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

drop table if exists t_kdl;
create table t_kdl (
  ip varchar(30),
  port int,
  crawled text,
  spider varchar(100),
  primary	KEY  (ip)
);