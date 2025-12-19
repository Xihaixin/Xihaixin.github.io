---
date:
  created: 2025-12-1  
---

# 基础博客搭建指南

本文将先概述博客的核心概念，再逐步引导你完成 `博客插件` 配置、博客搭建、文章创建及元数据定义的全流程。<!-- more -->

博客是与受众互动的绝佳方式。软件开发人员可通过博客发布新功能公告、演示功能用法并提供背景信息，也能通过评论技术前沿动态彰显专业能力，或记录自身实践作为最佳案例分享。围绕热点话题撰写的博文有助于为官网引流，保持受众活跃度——当然，你也可以分享任何感兴趣的内容。

`博客插件` 让你能够轻松在现有内容中嵌入博客功能；若仅需博客作为唯一内容形式，也可将其配置为独立博客系统。

[blog plugin]: ../../plugins/blog.md 

__所需时间：__ 通常约 20 分钟
[中文教程地址](https://mkdoc-material.llango.com/)

## 核心概念

**文章（Post）与摘要（Excerpt）**：博客由若干独立的「文章」（常称博文）和一个索引页组成。索引页按时间倒序展示文章（最新文章置顶），通常仅显示简短「摘要」及跳转至完整文章的链接。

**元数据（Metadata）**：索引页和文章本身都会显示关键信息，例如发布时间、更新时间、作者及预计阅读时长。

**URL 别名（Slug）**：由于博客文章主要按时间排序，而非层级结构，其 URL 不会反映目录关系。反之，每篇文章的 URL 会包含一个简化描述（即 Slug），通常由文章的一级标题自动生成。

**导航（Navigation）**：博客的主要导航结构是时间线，可通过「分类（Categories）」进一步细分。主索引页展示最新文章，「归档（Archive）」板块按年份整理过往内容。此外，文章可添加「标签（Tags）」，标签索引页会基于内容提供额外的导航维度。

你可以在 [Material for MkDocs 官方博客] 中直观查看所有上述元素。

[Material for MkDocs blog]: https://squidfunk.github.io/mkdocs-material/blog/

## 搭建你的博客

博客插件是 Material for MkDocs 的内置组件，但需在 `mkdocs.yml` 中进行配置。

!!! example "搭建博客基础框架"

    若尚未创建项目，请先新建博客项目，然后编辑 `mkdocs.yml` 文件，确保包含以下配置：

    ```yaml
    site_name: 博客教程
    site_description: 跟随教程搭建的示例博客
    site_url: http://www.example.com

    theme:
      name: material

    plugins:
      - search
      - blog
    ```

    博客插件会自动创建所需的目录结构（若不存在），只需运行 `mkdocs serve` 即可生成：

    ```
    docs
    ├── blog
    │   ├── index.md  # 博客索引页
    │   └── posts     # 文章存储目录
    └── index.md      # 网站首页
    ```

接下来，在 `docs/blog/posts` 目录中创建你的第一篇博客文章。文章的命名规则和子目录结构可自定义，只需确保文件位于 `docs/blog/posts` 下即可。

每篇文章**必须包含页首元数据**（Front Matter），需放在 Markdown 代码顶部，用三短横线 `---` 包裹。元数据中至少需包含 `date` 字段，还可添加其他自定义信息（详见下文）。元数据之后是文章正文，请注意：

- 必须包含一级标题（`# 标题`），插件会基于该标题生成 Slug；
- 在文中添加 `<!-- more -->` 标记，可指定索引页显示的摘要截止位置。

!!! example "撰写第一篇文章"

    创建文件 `docs/blog/posts/myfirst.md`，内容如下：

    ```
    ---
    date:
      created: 2023-12-31  # 创建时间（必填）
    ---

    # 新年夜快乐！

    祝愿大家玩得开心，新的一年万事如意！
    <!-- more -->  # 摘要截止于此，后续内容仅在完整文章中显示

     ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua.（占位文本，实际使用时替换为正文）
    ```

    运行 `mkdocs serve`，在浏览器中访问 `http://localhost:8000/blog`：
    - 博客插件会自动生成导航元素，索引页仅显示摘要；
    - 点击「继续阅读（Continue reading）」链接可跳转至完整文章；
    - 观察文章 URL，其由一级标题自动生成（示例中为 `happy-new-years-eve`）。

!!! tip "导航配置"

    我们还提供了 [导航教程]，详细说明如何修改自动生成的导航、将博客集成到现有导航结构，以及如何创建二级导航、作者页面和控制分页功能。

[tutorial on navigation]: navigation.md

## 文章元数据

除了创建时间，你还可以添加其他元数据或给插件指定规则（例如标记为草稿、置顶文章等）。

### 草稿（Drafts）

若需在本地编辑文章草稿但不希望其出现在正式发布版本中，可在页首元数据中添加 `draft: true` 字段。

!!! example "创建草稿文章"

    在 `docs/blog/posts/draft.md` 中创建第二篇文章，内容如下：

    ```hl_lines="4"  # 高亮显示新增字段
    ---
    date:
      created: 2024-01-01
    draft: true  # 标记为草稿
    ---

    # 新年快乐！

    祝大家 2024 年一切顺利！
    <!-- more -->

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua.
    ```

    运行 `mkdocs serve` 本地预览时，草稿会在索引页显示但带有「草稿（Draft）」标签；运行 `mkdocs build` 构建正式版本时，草稿不会被包含在输出文件中：

    ```
    $ mkdocs build
    $ ls site/blog
    site/blog
    ├── 2023
    │   └── 12
    │       └── 31
    │           └── happy-new-years-eve
    │               └── index.html
    ...
    ```

    2024 年的草稿文章未出现在输出目录中。发布时需删除 `draft: true` 字段。

也可创建专门的草稿目录，并使用 [Meta 插件] 为该目录下所有文章自动添加 `draft: true` 元数据，便于集中管理草稿（无需逐一编辑文章页首）。Meta 插件的使用将在下文介绍。

[Meta plugin]: ../../plugins/meta.md

### 编辑记录（Edits）

若需更新已发布的文章（例如修正错误或补充内容），可在页首元数据中添加 `updated` 字段标注更新时间。

!!! example "编辑文章并添加更新时间"

    修改第一篇文章的内容，在元数据中添加更新时间：

    ```hl_lines="3 4"
    ---
    date:
      created: 2023-12-31  # 创建时间
      updated: 2024-01-02  # 更新时间（新增）
    ---
    ```

    文章的元数据区域会显示更新时间，但索引页默认不展示该信息。

### 阅读时长（Reading time）

插件会自动计算文章的预计阅读时长。若需自定义该时长，可在页首元数据中添加 `readtime` 字段（单位：分钟）。

!!! example "自定义阅读时长"

    为第一篇文章添加自定义阅读时长：

    ```hl_lines="5"
    ---
    date:
      created: 2023-12-31
      updated: 2024-01-02
    readtime: 15  # 预计阅读时长 15 分钟
    ---
    ```

### 置顶（Pinning）

若需将某篇文章固定在索引页顶部（不受发布时间影响），可在页首元数据中添加 `pin: true` 字段。

!!! example "置顶文章"

    为第一篇文章添加置顶属性：

    ```hl_lines="6"
    ---
    date:
      created: 2023-12-31
      updated: 2024-01-02
    readtime: 15
    pin: true  # 置顶文章
    ---
    ```

    本地预览时，该文章会显示在索引页顶部（即使发布时间早于其他文章），并带有小图钉图标标识。

### 相关链接（Related links）

若博客是技术文档等大型网站的一部分，可在博文中添加相关链接，引导读者访问其他内容。只需在页首元数据中通过 `links` 字段指定链接目标，插件会自动生成相关链接区域。

!!! example "添加相关链接"

    在文章元数据中添加相关链接：

    ``` hl_lines="5-7"
    ---
    date:
      created: 2023-12-31
    ...
    links:  # 相关链接（新增）
      - index.md  # 网站首页
      - blog/index.md  # 博客索引页
    ---
    ```

    相关链接会显示在元数据区域下方。

插件会自动复用 MkDocs 主导航的页面标题作为链接文本（无需手动指定）。其语法与 `mkdocs.yml` 中 `nav` 字段一致，支持自定义链接标题和多级子链接：

!!! example "自定义链接标题"

    修改链接配置，自定义标题并添加外部链接：

    ```hl_lines="6-9"
    ---
    date:
      created: 2023-12-31
    ...
    links:
      - 首页: index.md  # 自定义标题
      - 博客索引: blog/index.md
      - 外部链接:  # 多级子链接
        - Material 文档: https://squidfunk.github.io/mkdocs-material
    ---
    ```

    显示效果：
    - 宽屏设备：相关链接显示在左侧侧边栏；
    - 窄屏设备：相关链接显示在文章底部。
    可调整浏览器窗口大小查看适配效果。

## Meta 插件

Meta 插件用于简化同一目录下多个文件的通用元数据管理。无需在每个文件的页首重复添加相同元数据，只需在目录中创建 `.meta.yml` 文件，插件会自动将其内容合并到该目录下所有文章的页首元数据中。若某篇文章的页首包含相同字段，将以文章自身配置为准（支持覆盖）。

例如，可创建专门的草稿目录，通过 `.meta.yml` 为目录下所有文章自动添加 `draft: true`，既无需逐一编辑文章，又能集中管理草稿。

!!! example "使用 Meta 插件管理草稿"

    1. 首先在 `mkdocs.yml` 中启用 Meta 插件：

    ```yaml hl_lines="4"
    plugins:
      - search
      - blog
      - meta  # 启用 Meta 插件
    ```

    2. 创建草稿目录：

    === "MacOS/Linux"

        ```bash
        $ mkdir docs/blog/posts/drafts
        ```

    === "Windows"
        ```powershell
        $ mkdir docs\blog\posts\drafts
        ```

    3. 在 `drafts` 目录中创建 `.meta.yml` 文件，内容如下：

    ```yaml
    draft: true  # 该目录下所有文章自动标记为草稿
    ```

    4. 在 `drafts` 目录中添加博客文章，本地预览时文章会显示「草稿」标签，正式构建时不会被包含。发布时只需将文章移出 `drafts` 目录即可。

[meta]: ../../plugins/meta.md

## 后续操作

至此，你已成功搭建可运行的博客。随着内容积累，可进一步优化以下功能：

1. **增强导航与发现**：添加标签、分类等二级导航，支持多作者 attribution 及作者页面生成，详见 [导航、分页与作者教程]。
2. **提升互动与传播**：配置 RSS 订阅功能或评论系统，详见 [互动与传播教程]。

[tutorial on navigation, pagination, and authors]: navigation.md
[engagement and dissemination tutorial]: engage.md
