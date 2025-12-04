# Linux 内核

以下内容来自[Linux](https://github.com/torvalds/linux)

内核开发者和用户可参考多份指南文档。这些指南支持多种格式渲染（如 HTML 和 PDF），请先阅读 **Documentation/admin-guide/README.rst**。

## 文档构建方法
执行以下命令构建文档：
- HTML 格式：`make htmldocs`
- PDF 格式：`make pdfdocs`

也可通过以下链接在线阅读格式化文档：
https://www.kernel.org/doc/html/latest/

## 补充说明
Documentation/ 子目录下包含多个文本文件，其中部分采用 **reStructuredText 标记语法**编写。

请务必阅读 **Documentation/process/changes.rst** 文件，该文件包含：
1. 内核构建与运行的环境要求
2. 内核升级可能引发的问题及相关说明

---

### 翻译要点说明（技术文档特性适配）
1. **术语精准性**
   - "Linux kernel" 译为"Linux 内核"（行业标准译法）
   - "reStructuredText" 保留原名+中文注释（标记语言专有名词）
   - "markup notation" 译为"标记语法"（技术文档通用表述）

2. **命令与路径格式**
   - 保留原始命令格式（如 ``make htmldocs``）和文件路径（如 Documentation/admin-guide/README.rst），符合技术文档阅读习惯
   - 路径分隔符使用 Linux 原生 `/`，不转换为 Windows 格式 `\`

3. **句式适配**
   - 英文被动语态转中文主动态（如 "can be rendered" → "支持多种格式渲染"）
   - 长句拆分（如原文最后一句拆分为两点式表述，提升可读性）
   - 省略主语补充（如 "Please read" → "请先阅读"/"请务必阅读"，明确动作主体）

4. **技术文档规范**
   - 标题层级保留原始格式（= 分隔符）
   - 关键文件路径加粗突出，便于快速定位
   - 命令和链接单独成行，符合技术文档排版惯例

5. **文化适配**
   - "several guides" 译为"多份指南文档"（避免直译"几个"的口语化）
   - "problems which may result" 译为"可能引发的问题"（中性表述，不夸大风险）