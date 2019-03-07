# GitLab

```bash
# GitLab コンテナイメージの起動
docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 22:22 \
  --name gitlab \
  --restart always \
  --volume /Users/hono/docker/gitlab/config:/etc/gitlab \
  --volume /Users/hono/docker/gitlab/logs:/var/log/gitlab \
  --volume /Users/hono/docker/gitlab/data:/var/opt/gitlab \
  gitlab/gitlab-ce:rc
```