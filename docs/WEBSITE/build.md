# 使用 mkdocs-material 搭建网站

## 基础环境建设

参考官网 [Creating your site](https://squidfunk.github.io/mkdocs-material/creating-your-site/#minimal-configuration-visual-studio-code)

```bash
# 创建 python 虚拟环境
python venv .venv

# 激活虚拟环境
.venv/scripts/activate

# 安装 mkdocs-material 
pip install mkdocs-matrial

# 在当前目录中创建一个新的站点
mkdocs new .

# 本地启动站点服务
# 可以通过 http://localhost:8000 进行访问
mkdocs serve 

```

## 两个常用的命令

- 日常写文档只用 serve，最终发布才用 build

1. mkdocs serve（开发 / 预览用）
执行后会启动一个本地 Web 服务器 (http://127.0.0.1:8000)。修改 mkdocs.yml 或 md 文档，浏览器会自动刷新，立刻看到效果，只适合本地写文档、调试样式。

1. mkdocs build（发布 / 部署用）
执行后会在项目根目录生成 site/ 文件夹，里面是完整的纯静态 HTML/CSS/JS 文件。该文件夹可以直接推送到服务器、GitHub Pages、Netlify 等平台上线运行。

