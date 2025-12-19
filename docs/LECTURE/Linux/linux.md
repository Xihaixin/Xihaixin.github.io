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