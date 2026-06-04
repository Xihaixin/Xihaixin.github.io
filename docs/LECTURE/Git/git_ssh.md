今天使用 git 打算克隆自己在 gitee 上的远程项目。但是一直失败。我从 ssh 切换到 https ，速度很快，一下就成功了。在国内用 **Git SSH 不稳定**，是很常见的现象，原因非常现实：

# 1. SSH 不走国内优化线路，容易被墙/路由绕远
- Gitee / GitHub 的 **HTTPS** 有国内 CDN、专线、缓存，速度稳得一批。
- **SSH 是裸 TCP 连接**，没有任何应用层优化，走的是国际/跨省公网路由。
- 网络一波动、QoS 一限流、防火墙一深包检测，就直接：
  > Connection closed by remote host

# 2. SSH 长连接容易被运营商“掐断”
国内运营商（电信/移动/联通）会：
- 对**长时间不活跃的 TCP 连接**主动切断
- 对**大流量持续传输**做限速或断开
- 某些地区对 SSH 22 端口本身就有不稳定策略

而 HTTPS 走 443，是浏览器常用端口，**优先级更高、更宽容**。

# 3. SSH 不支持断线续传，Git HTTPS 支持
你出现的：
```
fetch-pack: unexpected disconnect while reading sideband packet
fatal: early EOF
```
就是典型的**中途断连，且无法恢复**。

HTTPS 下 Git 可以分段传输、自动重试，SSH 不行，断了就直接失败。

# 4. --depth=1 虽然小，但 SSH 依然脆弱
哪怕只拉最新一层，SSH 连接只要网络抖动一下就失败。
HTTPS 因为有 HTTP/1.1 分段、keep-alive、代理优化，稳很多。

---

# 简单一句话总结
**HTTPS 是绿色通道，有加速、有缓存、有重试；
SSH 是野路，裸连、远路、容易被掐，国内天然不稳定。**


