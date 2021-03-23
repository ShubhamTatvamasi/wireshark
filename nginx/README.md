# nginx

Create a nginx container for capturing traffic:
```bash
docker run -d -p 80:80 nginx:alpine
```

Now capture traffic from newly created network.

make a get request on nginx container:
```bash
curl localhost
```

Wireshark filter:
```
http && ip.src==172.17.0.2
```
