---
title: "统一全站风格"
date: 2026-09-13
author: "溪海莘"
description: "首页改完之后，顺手把全站的配色、导航和页脚也统一了。"
---

# 统一全站风格

首页改完，一跳到文章页就露馅了——还是 Material 默认的白底配橙色，跟首页的海蓝完全不像一个站。

我没打算一个个组件去改样式，太累。Material 的组件其实都从一组 CSS 变量取色，把这些变量覆盖掉，整站就跟着变了。

## 换个色

```css
body[data-md-color-scheme="default"][data-md-color-primary],
body[data-md-color-scheme="slate"][data-md-color-primary] {
  --md-default-bg-color: var(--qt-bg);
  --md-default-fg-color: var(--qt-ink);
  --md-typeset-a-color: var(--qt-sea);
  --md-accent-fg-color: var(--qt-sea);
}
```

选择器看着有点长，是为了压过 Material 自己生成的主题选择器。深色那套它写成 `[data-md-color-scheme=slate][data-md-color-primary=indigo]`，特异性比我直接写一个属性高，不补一个 `[data-md-color-primary]` 就盖不住。这个坑当时卡了我一会儿。

## 顶栏那两行

顶栏分两行，上面是站名和搜索，下面是导航标签。原来两行一个颜色，平平的。现在第一行做成半透明毛玻璃，滚动时能透出下面的内容；第二行干脆用正文底色，跟内容区接上。

标签的选中状态也改了。Material 默认给激活标签加一条下划线，我不太喜欢，改成只把颜色加深，安静一点。

## 侧边栏别全展开

有个我一直想改的地方：打开任意一页，左侧目录默认全部展开，长长一大条。其实只要在 `mkdocs.yml` 里把 `navigation.expand` 注释掉，它就只展开当前页所在的那一支了。

## 站标换成「溪」

顺手把站标换成一个「溪」字。用楷体，套一个很浅的圆形底和细描边，比默认图标更像个人标识。字是 CSS 的 `content` 加进去的，没用图片：

```css
.md-header__button.md-logo::after { content: "溪"; }
```

一开始做得又大又重，后来调小、调淡，才顺眼。
