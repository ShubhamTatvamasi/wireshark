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

install tcpdump and start to capture tcpdump:
```bash
docker exec -it mysql bash -c "apt update && apt install tcpdump -y"
tcpdump -i any -w /tmp/mysql.pcap
```

connect to mysql:
```bash
mysql --user=root --password=password --host=127.0.0.1 classicmodels
```

make query on database:
```mysql
select * from employees;
```

get file from container:
```bash
docker cp mysql:/tmp/mysql.pcap .
```
---

### Python

```bash
sudo pip3 install mysql-connector-python
```

```bash
python3 mysql_select.py
```
