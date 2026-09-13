"""为文章页注入元数据块（作者 / 发布日期 / 更新日期 / 摘要）。

读取每篇文章的 front matter：
---
title: 文章标题
date: 2025-12-04          # 首次提交（发布）
updated: 2026-07-24       # 最近提交（更新）
author: 溪海莘
description: 一段摘要
---
并在正文第一个 H1 之后插入 .page-meta 区块。首页与各目录的 index.md 不处理。
"""

from __future__ import annotations

import html
import re
from datetime import date, datetime

H1_RE = re.compile(r"^#\s+.+?$", re.MULTILINE)


def _fmt(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (date, datetime)):
        return value.strftime("%Y-%m-%d")
    return str(value).strip()


def _build_meta_html(meta: dict) -> str:
    author = _fmt(meta.get("author"))
    published = _fmt(meta.get("date"))
    updated = _fmt(meta.get("updated"))
    desc = _fmt(meta.get("description"))

    parts = []
    if author:
        parts.append(f'<span class="page-meta__author">{html.escape(author)}</span>')
    if published:
        parts.append(
            f'<span class="page-meta__date">发布于 '
            f'<time datetime="{published}">{published}</time></span>'
        )
    if updated and updated != published:
        parts.append(
            f'<span class="page-meta__updated">更新于 '
            f'<time datetime="{updated}">{updated}</time></span>'
        )

    lines = ['<div class="page-meta" markdown="0">']
    if parts:
        sep = '<span class="page-meta__sep" aria-hidden="true">·</span>'
        lines.append("  <div class=\"page-meta__row\">" + sep.join(parts) + "</div>")
    if desc:
        lines.append(f'  <p class="page-meta__desc">{html.escape(desc)}</p>')
    lines.append("</div>")
    return "\n".join(lines)


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    if src.endswith("index.md"):
        return markdown

    meta = page.meta or {}
    if not any(key in meta for key in ("author", "date", "updated", "description")):
        return markdown

    block = _build_meta_html(meta)
    match = H1_RE.search(markdown)
    if match:
        end = match.end()
        return markdown[:end] + "\n\n" + block + "\n" + markdown[end:]
    return block + "\n\n" + markdown
