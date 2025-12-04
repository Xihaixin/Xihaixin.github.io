# Git 典型使用案例

## 一、基础场景：个人开发（本地仓库管理）
### 核心目标：
在本地跟踪文件修改、提交版本、查看历史，无需团队协作。

### 完整流程：
1. **初始化本地仓库**（新建项目/已有项目添加Git跟踪）
   ```bash
   # 1. 新建项目并初始化（推荐）
   mkdir my-project && cd my-project  # 创建并进入项目文件夹
   git init  # 初始化Git仓库（生成隐藏的.git目录）

   # 2. 已有项目添加Git跟踪（进入现有项目文件夹）
   cd existing-project
   git init
   ```

2. **添加文件到暂存区**（告诉Git“要跟踪这些修改”）
   ```bash
   # 添加单个文件
   git add README.md

   # 添加所有修改/新增文件（常用）
   git add .  # 注意：不会添加被.gitignore排除的文件

   # 取消暂存某个文件（误加时用）
   git reset HEAD README.md
   ```

3. **提交版本**（将暂存区的修改保存为“历史版本”，必须写提交信息）
   ```bash
   git commit -m "feat: 初始化项目，添加README和核心代码"  # 规范：类型+描述（见下方说明）
   git commit -am "fix: 修复登录按钮点击无响应问题"  # 快捷方式：跳过暂存区，直接提交已跟踪文件的修改
   ```
   ✅ 提交信息规范（推荐）：`类型: 简短描述`  
   常见类型：`feat`（新功能）、`fix`（修复bug）、`docs`（文档修改）、`style`（格式调整，不影响代码功能）、`refactor`（重构）、`test`（测试代码）、`chore`（构建/工具配置）。

4. **查看状态/历史/差异**（日常高频操作）
   ```bash
   git status  # 查看当前仓库状态（哪些文件未跟踪/已修改/已暂存）
   git log     # 查看提交历史（按时间倒序，q退出）
   git log --oneline  # 简洁显示历史（一行一个版本，含版本号前7位）
   git diff    # 查看未暂存的修改（工作区 vs 暂存区）
   git diff --cached  # 查看已暂存的修改（暂存区 vs 本地仓库）
   ```

5. **版本回滚**（修改出错，回到之前的正确版本）
   ```bash
   # 1. 查看历史，找到要回滚的版本号（比如 abc1234）
   git log --oneline

   # 2. 回滚到指定版本（保留后续修改，仅重置仓库状态）
   git reset --soft abc1234  # 工作区和暂存区不变，仅本地仓库回滚
   git reset --mixed abc1234 # （默认）工作区不变，暂存区和本地仓库回滚（常用）
   git reset --hard abc1234  # 工作区、暂存区、本地仓库全部回滚（谨慎！会丢失未提交修改）

   # 3. 若已提交错误版本，想“撤销提交”（生成新的反向提交，不删除历史）
   git revert abc1234  # 适合已推送到远程仓库的场景
   ```


## 二、核心场景：团队协作（远程仓库同步）
### 核心目标：
通过 GitHub/GitLab/Gitee 等远程仓库，与团队成员共享代码、协同开发。

### 前提准备：
- 注册远程仓库账号（如 GitHub），创建远程仓库（比如 `https://github.com/your-name/team-project.git`）
- 本地配置Git身份（首次使用必须配置，否则无法提交）
  ```bash
  git config --global user.name "你的名字"
  git config --global user.email "你的邮箱"
  ```

### 场景1：从远程仓库克隆项目（首次参与团队项目）
```bash
# 克隆远程仓库到本地（会自动创建项目文件夹）
git clone https://github.com/your-name/team-project.git

# 进入项目目录
cd team-project
```

### 场景2：本地项目关联远程仓库（本地已开发，首次推送到远程）
```bash
# 1. 本地初始化仓库（若未初始化）
git init
git add .
git commit -m "feat: 初始化项目"

# 2. 关联远程仓库（remote名默认叫origin，可自定义）
git remote add origin https://github.com/your-name/team-project.git

# 3. 推送本地分支到远程（-u 绑定本地master分支和远程master分支，后续可直接git push）
git push -u origin master  # 若远程默认分支是main，替换为 git push -u origin main
```

### 场景3：团队协作日常流程（拉取更新→开发→推送）
```bash
# 1. 开发前先拉取远程最新代码（避免冲突，必做！）
git pull origin master  # 拉取远程master分支的更新到本地

# 2. 本地开发（修改文件、新增功能）
# ... 编写代码 ...

# 3. 提交本地修改
git add .
git commit -m "feat: 新增用户列表查询功能"

# 4. 推送本地修改到远程（让团队成员看到）
git push  # 已绑定分支后，无需重复写origin master
```

### 场景4：解决代码冲突（多人修改同一文件同一位置）
冲突是团队协作中最常见的问题，核心是“协商后保留正确代码”：
```bash
# 1. 拉取远程更新时触发冲突，Git会提示“Automatic merge failed”
git pull origin master

# 2. 查看冲突文件（Git会在文件中标记冲突位置）
# 冲突文件内容示例：
# <<<<<<< HEAD（你的本地修改）
# 你的代码：let name = "张三";
# =======
# 远程代码：let name = "李四";
# >>>>>>> abc1234（远程版本号）

# 3. 手动编辑冲突文件：删除冲突标记（<<<<<<、=======、>>>>>>），保留正确代码
# 编辑后：let name = "张三"; （或协商后改为其他内容）

# 4. 重新提交冲突后的修改
git add 冲突文件名  # 或 git add .
git commit -m "merge: 解决用户名称变量冲突"
git push  # 推送解决后的代码到远程
```


## 三、进阶场景：分支管理（多功能并行开发）
### 核心目标：
通过分支隔离不同功能/修复，避免干扰主分支（master/main）的稳定性。

### 分支命名规范（推荐）：
- 功能分支：`feature/用户登录`、`feature/支付功能`
- 修复分支：`bugfix/登录失败`、`hotfix/生产环境崩溃`
- 发布分支：`release/v1.0.0`

### 完整流程：
1. **创建并切换到新分支**（基于主分支创建）
   ```bash
   # 方法1：先创建分支，再切换
   git branch feature/login  # 创建分支
   git checkout feature/login  # 切换到该分支

   # 方法2：创建并切换（常用快捷方式）
   git checkout -b feature/login

   # 方法3：Git 2.23+ 推荐用switch（更直观）
   git switch -c feature/login  # -c = create
   ```

2. **在分支上开发并提交**（流程和主分支一致）
   ```bash
   # ... 开发登录功能 ...
   git add .
   git commit -m "feat: 完成登录页面和接口对接"
   ```

3. **功能完成后，合并到主分支**
   ```bash
   # 1. 先切换回主分支
   git switch master  # 或 git checkout master

   # 2. 拉取远程主分支最新更新（避免合并后冲突）
   git pull origin master

   # 3. 合并功能分支到主分支
   git merge feature/login  # 若有冲突，按“场景4”解决后提交

   # 4. 推送合并后的主分支到远程
   git push origin master
   ```

4. **删除已合并的分支（可选，清理分支）**
   ```bash
   # 删除本地分支
   git branch -d feature/login

   # 删除远程分支（若已推送过该分支到远程）
   git push origin --delete feature/login
   ```


## 四、高频场景：其他实用操作
### 1. 忽略不需要跟踪的文件（.gitignore）
创建 `.gitignore` 文件，写入不需要Git跟踪的文件/目录（如编译产物、日志、IDE配置）：
```bash
# 编辑.gitignore（在项目根目录）
touch .gitignore
```
`.gitignore` 内容示例（前端项目）：
```
# 依赖包
node_modules/
# 编译产物
dist/
build/
# 日志
logs/
# IDE配置
.idea/
.vscode/
# 环境变量文件
.env
# 缓存文件
*.log
*.tmp
```

### 2. 临时存储修改（stash，开发中切换分支用）
场景：正在开发功能A（未提交），需要紧急修复bug（切换到其他分支），但不想提交未完成的代码：
```bash
# 1. 暂存当前修改（工作区和暂存区都会被存储）
git stash save "开发到一半的登录功能"  # 可加描述，方便后续识别

# 2. 切换到bugfix分支修复问题
git switch bugfix/login-error
# ... 修复bug并提交 ...
git commit -m "fix: 修复登录时密码加密错误"
git switch master
git merge bugfix/login-error
git push

# 3. 回到原功能分支，恢复暂存的修改
git switch feature/login
git stash pop  # 恢复最近一次stash，并删除该stash
# 或 git stash apply stash@{0}  # 恢复指定stash（不删除，可通过git stash list查看）

# 查看所有stash
git stash list
```

### 3. 查看远程仓库信息
```bash
git remote -v  # 查看关联的远程仓库地址（origin对应的URL）
git remote show origin  # 查看远程仓库的详细信息（分支、提交记录等）
```

### 4. 撤销本地修改（未暂存/已暂存）
```bash
# 1. 撤销工作区的未暂存修改（未git add的文件）
git checkout -- README.md  # 单个文件
git checkout -- .  # 所有文件（谨慎！会丢失未提交的修改）

# 2. 撤销暂存区的修改（已git add，但未git commit）
git reset HEAD README.md  # 单个文件
git reset HEAD .  # 所有文件
```


## 五、总结：Git核心工作流图谱
```
工作区（本地文件）→ git add → 暂存区 → git commit → 本地仓库 → git push → 远程仓库
                                  ↑                    ↑
                                  |                    |
                           git reset --mixed       git pull
                                  |                    |
                                  ↓                    ↓
工作区（本地文件）←───────────────── 暂存区 ←───────────────── 远程仓库
```

## 关键原则：
1. 提交要“小而频繁”，每个提交只做一件事（便于回滚和审查）
2. 团队协作前必做 `git pull`，避免冲突
3. 重要分支（如master）禁止直接提交，通过分支合并
4. 提交信息要清晰，让他人（或未来的你）能看懂修改目的

按以上场景操作，可覆盖 90% 的日常Git使用需求，遇到问题优先用 `git status` 查看当前状态，Git的错误提示通常会给出解决方案～