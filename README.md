# wireshark

Create a nginx container for capturing traffic:
```bash
docker run -d -p 80:80 nginx:alpine
```

Wireshark filter:
```
http && ip.src==172.17.0.2
```
