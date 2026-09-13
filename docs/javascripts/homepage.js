/**
 * 首页交互：is-homepage 类、时间问候、滚动淡入。
 * 仅依赖原生 API，无外部请求。
 */
(function () {
  'use strict';

  var HOME_CLASS = 'is-homepage';

  function ready(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  }

  function normalizePath(url) {
    return url.pathname.replace(/\/+$/, '') || '/';
  }

  /**
   * 首页 URL：优先取顶栏 logo 链接（始终指向站点根），
   * 退化时取第一个顶部标签，最后退回路径名判断。
   */
  function resolveHomeUrl() {
    var candidates = [
      document.querySelector('.md-header__button.md-logo'),
      document.querySelector('.md-tabs__item .md-tabs__link'),
      document.querySelector('.md-nav__button.md-logo')
    ];
    for (var i = 0; i < candidates.length; i++) {
      var el = candidates[i];
      if (!el) continue;
      var href = el.getAttribute('href');
      if (!href) continue;
      try {
        return new URL(href, window.location.href);
      } catch (e) {
        /* 忽略非法 href */
      }
    }
    return null;
  }

  function isHomepage() {
    var home = resolveHomeUrl();
    if (!home) {
      var path = normalizePath(window.location);
      return path === '/' || path === '/index.html';
    }
    var here = new URL(window.location.href);
    return home.origin === here.origin && normalizePath(home) === normalizePath(here);
  }

  function applyHomepageClass() {
    var home = isHomepage();
    document.body.classList.toggle(HOME_CLASS, home);
    ['.md-main', '.md-container'].forEach(function (selector) {
      var el = document.querySelector(selector);
      if (el) el.classList.toggle(HOME_CLASS, home);
    });
    return home;
  }

  /* ---------- 时间问候 ---------- */

  var periodDefs = [
    [0, 5, '凌晨', '夜深了，注意休息'],
    [5, 7, '清晨', '清晨好，新的一天开始了'],
    [7, 9, '早上', '早上好'],
    [9, 11, '上午', '上午好'],
    [11, 13, '中午', '中午好，记得休息一下'],
    [13, 15, '午后', '午后好'],
    [15, 18, '下午', '下午好'],
    [18, 20, '傍晚', '傍晚好'],
    [20, 22, '晚上', '晚上好'],
    [22, 24, '夜深', '夜深了，早点休息']
  ];

  function updateClock() {
    var timeEl = document.getElementById('greeting-time');
    var statusEl = document.getElementById('greeting-status');
    if (!timeEl || !statusEl) return;

    var now = new Date();
    var hour = now.getHours();
    var weekdays = ['日', '一', '二', '三', '四', '五', '六'];
    var period = periodDefs[periodDefs.length - 1];
    for (var i = 0; i < periodDefs.length; i++) {
      if (hour >= periodDefs[i][0] && hour < periodDefs[i][1]) {
        period = periodDefs[i];
        break;
      }
    }

    var pad = function (n) {
      return String(n).padStart(2, '0');
    };

    statusEl.textContent = period[3] + '，欢迎来到溪海莘的网站';
    timeEl.textContent =
      now.getFullYear() + '.' + pad(now.getMonth() + 1) + '.' + pad(now.getDate()) +
      ' 星期' + weekdays[now.getDay()] + ' · ' + period[2] + ' ' +
      pad(hour) + ':' + pad(now.getMinutes()) + ':' + pad(now.getSeconds());
  }

  function startClock() {
    updateClock();
    setInterval(updateClock, 1000);
  }

  /* ---------- 稳定运行时长 ---------- */

  function startUptime() {
    var el = document.getElementById('uptime-value');
    if (!el) return;
    var host = el.closest('.qt-uptime');
    var launch = host ? new Date(host.getAttribute('data-launch')) : null;
    if (!launch || isNaN(launch.getTime())) {
      el.textContent = '—';
      return;
    }

    function pad(n) {
      return String(n).padStart(2, '0');
    }

    function tick() {
      var ms = Date.now() - launch.getTime();
      if (ms < 0) ms = 0;
      var total = Math.floor(ms / 1000);
      var days = Math.floor(total / 86400);
      var hours = Math.floor((total % 86400) / 3600);
      var minutes = Math.floor((total % 3600) / 60);
      var seconds = total % 60;
      el.textContent = days + ' 天 ' + pad(hours) + ':' + pad(minutes) + ':' + pad(seconds);
    }

    tick();
    setInterval(tick, 1000);
  }

  /* ---------- 问候按钮展开 / 收起 ---------- */

  function setupDisclosure() {
    function detail() {
      return document.getElementById('greeting-detail');
    }

    document.addEventListener('click', function (e) {
      var trigger = e.target.closest('#greeting.qt-weather');
      var openTrigger = document.querySelector('#greeting.qt-weather[aria-expanded="true"]');

      if (trigger) {
        var isOpen = trigger.getAttribute('aria-expanded') === 'true';
        trigger.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
        var panel = detail();
        if (panel) panel.setAttribute('aria-hidden', isOpen ? 'true' : 'false');
        return;
      }

      if (openTrigger && !e.target.closest('#greeting-detail')) {
        openTrigger.setAttribute('aria-expanded', 'false');
        var openPanel = detail();
        if (openPanel) openPanel.setAttribute('aria-hidden', 'true');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      var openTrigger = document.querySelector('#greeting.qt-weather[aria-expanded="true"]');
      if (!openTrigger) return;
      openTrigger.setAttribute('aria-expanded', 'false');
      var panel = detail();
      if (panel) panel.setAttribute('aria-hidden', 'true');
      openTrigger.focus();
    });
  }

  /* ---------- 滚动淡入 ---------- */

  var scrollObserver = null;
  var scrollAnchor = null;

  function setupScrollAnimations() {
    if (!('IntersectionObserver' in window)) {
      document.querySelectorAll('.fade-in').forEach(function (el) {
        el.classList.add('fade-in-visible');
      });
      return;
    }

    var nodes = Array.prototype.slice.call(document.querySelectorAll('.fade-in'));
    var anchor = nodes[0] || null;
    if (scrollObserver && scrollAnchor === anchor) return;
    if (scrollObserver) scrollObserver.disconnect();

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    scrollObserver = observer;
    scrollAnchor = anchor;

    nodes.forEach(function (el) {
      var rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight - 50 && rect.bottom > 0) {
        el.classList.add('fade-in-visible');
        return;
      }
      observer.observe(el);
    });
  }

  /* ---------- 初始化 / 页面切换复检 ---------- */

  function init() {
    var home = applyHomepageClass();
    if (!home) return;

    setupDisclosure();
    startClock();
    startUptime();
    setupScrollAnimations();
  }

  ready(init);

  var recheckTimer = null;
  function scheduleRecheck() {
    if (recheckTimer) clearTimeout(recheckTimer);
    recheckTimer = setTimeout(init, 150);
  }

  document.addEventListener('navigation', scheduleRecheck);
  window.addEventListener('locationchange', scheduleRecheck);
  window.addEventListener('popstate', scheduleRecheck);
})();
