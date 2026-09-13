"""首页「最近更新」自动生成。

在构建首页（docs/index.md）时，扫描除 ABOUT / WEBSITE 之外的全部内容目录，
按最后更新时间排序，取最近若干篇，生成首页的 .qt-article-row 列表并注入到
index.md 中的占位标记之间。

排序依据（依次回退）：
1. 文章 front matter 中的 updated: YYYY-MM-DD（最近修改）
2. 文章 front matter 中的 date: YYYY-MM-DD（发布）
3. 该文件的 git 最后一次提交日期
4. 文件的系统修改时间

摘要依据：优先取 front matter 的 description，缺失时才从正文首段自动截取。
"""

from __future__ import annotations

import html
import re
import subprocess
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import List

RECENT_START = "<!-- RECENT_UPDATES_START -->"
RECENT_END = "<!-- RECENT_UPDATES_END -->"

TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)
DATE_RE = re.compile(r"^date:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
UPDATED_RE = re.compile(r"^updated:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+?)\s*$", re.MULTILINE)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

# 这些目录属于站点说明 / 关于页面，不作为「文章」参与最近更新
EXCLUDE_TOP_DIRS = {"ABOUT", "WEBSITE"}


@dataclass
class BlogPost:
    title: str
    summary: str
    rel_path: str
    updated: date


def _read_front_matter(content: str) -> str:
    if not content.startswith("---"):
        return ""
    lines = content.splitlines()
    if len(lines) < 3:
        return ""
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return ""


def _strip_front_matter(content: str) -> str:
    if not content.startswith("---"):
        return content
    lines = content.splitlines()
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1 :])
    return content


def _extract_title(front_matter: str, content: str, md_file: Path) -> str:
    match = TITLE_RE.search(front_matter)
    if match:
        return match.group(1).strip().strip("'\"")
    h1 = H1_RE.search(_strip_front_matter(content))
    if h1:
        return h1.group(1).strip()
    return md_file.stem


def _extract_date(front_matter: str, pattern: re.Pattern) -> date | None:
    match = pattern.search(front_matter)
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


def _extract_description(front_matter: str) -> str:
    """取 front matter 里的 description，去掉包裹引号并做 HTML 转义。"""
    match = DESC_RE.search(front_matter)
    if not match:
        return ""
    raw = match.group(1).strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        raw = raw[1:-1]
    raw = raw.replace('\\"', '"').replace("\\\\", "\\")
    return html.escape(raw)


def _extract_summary(content: str, limit: int = 64) -> str:
    body = _strip_front_matter(content)
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        # 跳过标题、代码块、提示块、分隔线、引用、表格、列表、图片开头等
        if line.startswith(("#", "```", "~~~", "!!!", "???", "---", "***", ">", "|", "- ", "* ", "+ ")):
            continue
        if line.startswith(("![", "[!")):
            continue
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)
        text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
        text = re.sub(r"[*_`~]", "", text).strip()
        if not text:
            continue
        if len(text) > limit:
            text = text[:limit].rstrip() + "…"
        return html.escape(text)
    return ""


def _git_last_commit_date(repo_root: Path, rel_md_path: str) -> date | None:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel_md_path],
            cwd=repo_root,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None

    raw = result.stdout.strip()
    if result.returncode != 0 or not raw:
        return None
    try:
        return datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        return None


def _discover_posts(config) -> List[BlogPost]:
    docs_dir = Path(config["docs_dir"])
    repo_root = docs_dir.parent
    posts: List[BlogPost] = []

    for md_file in docs_dir.rglob("*.md"):
        rel = md_file.relative_to(docs_dir)
        parts = rel.parts
        # 仅收录「内容目录」下的文章：至少两级、且不在排除目录中
        if len(parts) < 2 or parts[0] in EXCLUDE_TOP_DIRS:
            continue
        if md_file.name == "index.md":
            continue

        content = md_file.read_text(encoding="utf-8")
        front_matter = _read_front_matter(content)
        rel_from_docs = rel.as_posix()

        # 排序日期：优先「最近修改」，其次「发布」，再退 git / 文件时间
        updated = _extract_date(front_matter, UPDATED_RE)
        if updated is None:
            updated = _extract_date(front_matter, DATE_RE)
        if updated is None:
            updated = _git_last_commit_date(repo_root, f"docs/{rel_from_docs}")
        if updated is None:
            updated = date.fromtimestamp(md_file.stat().st_mtime)

        # 摘要：优先作者明确填写的 description，缺失才自动截取正文
        summary = _extract_description(front_matter) or _extract_summary(content)

        posts.append(
            BlogPost(
                title=_extract_title(front_matter, content, md_file),
                summary=summary,
                rel_path=rel_from_docs,
                updated=updated,
            )
        )

    posts.sort(key=lambda p: (p.updated, p.rel_path), reverse=True)
    return posts


def _build_recent_rows(posts: List[BlogPost], config, limit: int = 3) -> str:
    use_dir_urls = bool(config.get("use_directory_urls", True))
    rows: List[str] = []

    for index, post in enumerate(posts[:limit], start=1):
        if use_dir_urls:
            href = post.rel_path[:-3] + "/"
        else:
            href = post.rel_path[:-3] + ".html"

        summary = post.summary or "&nbsp;"
        rows.append(
            "\n".join(
                [
                    f'<a class="qt-article-row" href="{href}">',
                    f'  <span class="qt-article-row__number">{index:02d}</span>',
                    '  <span class="qt-article-row__body">',
                    f'    <span class="qt-article-row__title">{html.escape(post.title)}</span>',
                    f'    <span class="qt-article-row__summary">{summary}</span>',
                    "  </span>",
                    f'  <time datetime="{post.updated.isoformat()}">{post.updated.strftime("%Y.%m.%d")}</time>',
                    '  <span class="qt-article-row__arrow" aria-hidden="true">↗</span>',
                    "</a>",
                ]
            )
        )

    if not rows:
        rows.append('<p class="qt-recent__empty">暂时还没有可展示的文章。</p>')

    return "\n".join(rows)


def _replace_between(markdown: str, start: str, end: str, content: str) -> str:
    if start not in markdown or end not in markdown:
        return markdown
    pattern = re.compile(f"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL)
    return pattern.sub(f"{start}\n{content}\n{end}", markdown, count=1)


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "index.md":
        return markdown

    posts = _discover_posts(config)
    generated = _build_recent_rows(posts, config, limit=3)
    return _replace_between(markdown, RECENT_START, RECENT_END, generated)
