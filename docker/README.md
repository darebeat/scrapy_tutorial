# README

## 创建本地公共网络

```
docker network create --driver=bridge --subnet=172.10.0.0/16 deploy
docker network ls
docker network inspect deploy
docker netwok rm deploy
```

## 数据库操作

```sh
docker exec -it mongodb mongo --host localhost --port 27017 -u dev -p dev12345  --authenticationDatabase scrapy
docker exec -it redis redis-cli -a 123
```