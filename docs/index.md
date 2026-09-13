---
title: 首页
hide:
  - toc
  - footer
---

<div class="qt-home">
  <section class="qt-hero" aria-labelledby="qt-hero-title">
    <div class="qt-hero__copy fade-in">
      <h1 id="qt-hero-title" class="home-title">溪海莘</h1>
      <div class="qt-hero__lead">
        <p class="home-subtitle">记录技术与生活的个人网站</p>
        <div class="qt-hero__intro">
          <p>你好，我是溪海莘。</p>
          <p>在这里，遇见不一样的世界</p>
          <p>品味深入人心的故事和技术。</p>
        </div>
      </div>

      <div class="qt-greeting">
        <button id="greeting" class="qt-weather fade-in" type="button"
          aria-expanded="false" aria-label="查看当前时间">
          <svg class="qt-weather__icon" viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="8.5"/>
            <path d="M12 7.5V12l3 1.8"/>
          </svg>
          <span id="greeting-status" class="greeting-status">你好</span>
          <span class="qt-weather__chevron" aria-hidden="true"></span>
        </button>
        <div id="greeting-detail" class="qt-weather__detail" aria-hidden="true">
          <span id="greeting-time" class="greeting-time"></span>
        </div>
      </div>

      <p class="qt-uptime" data-launch="2025-12-04T00:00:00+08:00">
        <span class="qt-uptime__dot" aria-hidden="true"></span>
        <span>本站已稳定运行</span>
        <span id="uptime-value" class="qt-uptime__value">—</span>
      </p>
    </div>

    <div class="qt-hero__tide" aria-hidden="true">
      <span class="qt-tide__drop"></span>
      <span class="qt-tide__ripples">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
      </span>
    </div>
  </section>

  <section id="recent-posts" class="qt-section qt-recent fade-in" aria-labelledby="recent-heading">
    <header class="qt-section__header">
      <h2 id="recent-heading">最近更新</h2>
      <a class="qt-section__more" href="BLOG/">全部文章 <span aria-hidden="true">↗</span></a>
    </header>

    <div class="qt-article-index">
      <!-- RECENT_UPDATES_START -->
      <!-- RECENT_UPDATES_END -->
    </div>
  </section>

  <section id="about-me" class="qt-section qt-about fade-in" aria-labelledby="about-heading">
    <div class="qt-about__portrait">
      <span class="qt-about__avatar" aria-hidden="true">溪</span>
      <p>溪海莘<br><span>讲一点故事 · 聊一些技术</span></p>
    </div>
    <div class="qt-about__content">
      <p class="qt-section__index" aria-hidden="true">ABOUT</p>
      <h2 id="about-heading">关于我</h2>
      <p class="qt-about__lead">涓涓细流聚为溪，条条小溪终入海。</p>
      <p>你好，我是溪海莘，HPU 电子信息工程本科。这里讲述故事，记录文字，研磨技术</p>
      <a class="qt-text-link" href="ABOUT/">了解更多 <span aria-hidden="true">↗</span></a>
    </div>
  </section>

  <section class="qt-section qt-featured fade-in" aria-labelledby="featured-heading">
    <header class="qt-section__header">
      <h2 id="featured-heading">推荐文章</h2>
    </header>

    <div class="qt-featured__layout">
      <a class="qt-featured__main" href="ESSAY/Articles/251120-reaearch/">
        <span class="qt-featured__visual" aria-hidden="true"><span>NOV</span><span>20</span></span>
        <span class="qt-featured__copy">
          <span class="qt-featured__meta">思考 · 随笔</span>
          <strong>做事情的逻辑</strong>
          <span>在行动之前，先把问题本身想清楚。</span>
          <span class="qt-text-link">阅读全文 <span aria-hidden="true">↗</span></span>
        </span>
      </a>

      <nav class="qt-featured__list" aria-label="更多推荐文章">
        <a href="BLOG/Network/internet-history/"><span>互联网历史</span><span aria-hidden="true">↗</span></a>
        <a href="BLOG/Linux/kernel-compile/"><span>Linux 内核编译尝试</span><span aria-hidden="true">↗</span></a>
        <a href="LECTURE/Git/git-demos/"><span>Git 典型使用案例</span><span aria-hidden="true">↗</span></a>
      </nav>
    </div>
  </section>

  <section class="qt-section qt-paths fade-in" aria-labelledby="paths-heading">
    <header class="qt-section__header">
      <h2 id="paths-heading">继续浏览</h2>
    </header>
    <nav class="qt-paths__grid" aria-label="网站主要入口">
      <a href="BLOG/"><span>博客</span><small>学习笔记与技术文章</small><b aria-hidden="true">↗</b></a>
      <a href="DEV/"><span>技术</span><small>开发实践与工具</small><b aria-hidden="true">↗</b></a>
      <a href="LECTURE/"><span>教程</span><small>Git / Linux 等使用教程</small><b aria-hidden="true">↗</b></a>
      <a href="ABOUT/"><span>关于</span><small>了解本站与作者</small><b aria-hidden="true">↗</b></a>
    </nav>
  </section>

  <footer class="qt-home-footer fade-in">
    <p>溪海莘</p>
    <p>使用 <a href="https://squidfunk.github.io/mkdocs-material/" target="_blank" rel="noopener">MkDocs Material</a> 构建</p>
  </footer>
</div>
