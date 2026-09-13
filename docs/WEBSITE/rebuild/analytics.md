---
title: "访问统计"
date: 2026-09-13
author: "溪海莘"
description: "用 Google Analytics 4 给站点加上访问统计。"
---

# 访问统计

站点上线以后，我一直不知道有没有人来看。没有数据，也就谈不上什么「最近哪篇受欢迎」。

静态站没有后端，统计只能借助第三方。选来选去用了 Google Analytics 4——倒不是说它多好，主要是 Material 直接内置了支持，省事。

## 接上

`mkdocs.yml` 里加两行就完事：

```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

`property` 是 GA4 的衡量 ID。在后台建好媒体资源、加一个网站数据流，就能拿到。

Material 会自动往每个页面注入 `gtag.js`，而且比 Google 给的那段还多做了几件事：站内搜索词、页面反馈，以及切换页面时的浏览事件。

!!! warning "别手动粘代码"
    Google 后台会给一段全局代码，跟 Material 生成的功能一样。两个一起放会重复计数，留配置就行。

## 能看到什么

GA4 里最常用的两个数：

- **Views**，网页浏览数，大概对应「阅读次数」；
- **Users**，用户数，大概对应「浏览人数」。

「实时」里能立刻看到自己，标准报告要等一两天才出数。

本地 `mkdocs serve` 预览也会上报。介意的话，调试时把 `analytics` 那两行临时注释掉。
