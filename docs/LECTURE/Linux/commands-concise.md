---
title: "Linux-command"
date: 2025-12-04
author: "溪海莘"
description: "轻松通过 docker 部署 linux-command 网站。"
---

# Linux-command

[Linux-command:linux命令大全搜索工具](https://github.com/jaywcjlove/linux-command/)
[在线网站](https://git.io/linux)

轻松通过 docker 部署 linux-command 网站。
```bash
docker pull wcjiang/linux-command
docker run --name linux-command --rm -d -p 9665:3000 wcjiang/linux-command:latest
```
## Or

```bash
docker run --name linux-command -itd -p 9665:3000 wcjiang/linux-command:latest
```
在浏览器中访问以下 URL

http://localhost:9665/
