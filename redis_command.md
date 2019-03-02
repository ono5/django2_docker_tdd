# redis 操作

```bash
redis-cli

# Database 切り替え
127.0.0.1:6379> SELECT 1
OK
127.0.0.1:6379[1]> 

# monitor
monitor

# 中身確認
keys *
1) "example:1:django.contrib.sessions.cachexeqsc6nzmpfaev0r636gvz73rf4jyaoa"

```