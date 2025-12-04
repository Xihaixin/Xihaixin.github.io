# Git

[Git项目:快速、可扩展的分布式版本控制系统](https://github.com/git/git),提供异常丰富的命令集，既支持高层级操作，也允许直接访问底层核心功能。

Git 是开源项目，遵循 GNU 通用公共许可证第 2 版（部分组件采用与 GPLv2 兼容的其他许可证）。它最初由林纳斯·托瓦兹（Linus Torvalds）在全球开发者社区的协助下编写而成。

## 安装指南
请阅读文件获取安装说明。

## 在线资源
可通过 <https://git-scm.com/> 访问 Git 官方在线资源，包括完整文档和相关工具。

## 入门与文档查阅
1. 入门教程：查看 [Documentation/gittutorial.adoc] ，或通过 `man gittutorial` 或 `git help tutorial` （需先完成安装）
2. 日常命令：查看 [Documentation/giteveryday.adoc] ，获取常用核心命令集
3. 命令详解：每个命令的文档可查看 `Documentation/git-<命令名>.adoc`，或通过 `man git-<命令名>` 或 `git help <命令名>` （需先完成安装）
4. CVS 迁移：原 CVS 用户可参考 [Documentation/gitcvs-migration.adoc] ，或通过 `man gitcvs-migration` 或 `git help cvs-migration` （需先完成安装）

## 社区参与与贡献
- **邮件列表**：Git 的用户讨论和开发工作通过邮件列表进行，欢迎向 git@vger.kernel.org 发送 Bug 报告、功能请求、评论或补丁
  - 补丁提交指南：查看 Documentation/SubmittingPatches
  - 编码规范：查看 Documentation/CodingGuidelines
- **订阅方式**：发送邮件至 <git+subscribe@vger.kernel.org> 订阅（详情见 https://subspace.kernel.org/subscribing.html）
- **邮件归档**：可通过 <https://lore.kernel.org/git/>、<https://marc.info/?l=git> 等平台查阅
- **安全问题**：安全相关问题请通过 Git 安全邮件列表 <git-security@googlegroups.com> 私下披露
- **项目状态**：维护者会定期向邮件列表发送 "What's cooking" 报告，汇总当前开发进度、方向及待办任务，相关讨论可作为项目状态的重要参考

## 本地化翻译贡献
如需参与错误提示、使用说明等文本的翻译（国际化 i18n/本地化 l10n），请查看 README.md（po 文件即 Portable Object 文件，用于存储翻译内容）。

## "git" 名称的由来
"git" 这个名字由林纳斯·托瓦兹在编写最初版本时命名。他将这款工具描述为「愚蠢的内容跟踪器」，而名称的含义可根据你的心情解读：
- 三个字母的可发音组合，且未被任何常见 UNIX 命令使用（其发音与 "get" 相近，这一点可能无关紧要）
- 愚蠢、卑劣、可鄙、简单（可从俚语词典中任选其一）
- 「全球信息跟踪器」（Global Information Tracker）：当你心情愉悦且工具正常工作时，仿佛天使在歌唱，房间瞬间被光芒照亮
- 「该死的一堆垃圾」（Goddamn Idiotic Truckload of Sh*t）：当它出现故障时
