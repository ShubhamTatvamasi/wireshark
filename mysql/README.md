# mysql

Create a nginx container for capturing traffic:
```bash
docker run -d \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=password \
  --name mysql \
  mysql
```

restore mysql data:
```bash
mysql --user=root --password=password --host=127.0.0.1 < mysqlsampledatabase.sql
```

connect to mysql:
```bash
mysql --user=root --password=password --host=127.0.0.1 classicmodels
```

make query on database:
```mysql
select * from employees;
```

