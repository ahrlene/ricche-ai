// ============================================
// RICCHE — Animations, Theme, Scroll Reveals
// ============================================
(function () {

  // ---- Preloader (skip on repeat visits) ----
  const preloader = document.getElementById('preloader');
  if (preloader) {
    const hasVisited = sessionStorage.getItem('ricche-visited');
    if (hasVisited) {
      preloader.classList.add('hidden');
      document.body.style.overflow = '';
      document.body.removeAttribute('aria-busy');
    } else {
      document.body.style.overflow = 'hidden';
      window.addEventListener('load', () => {
        setTimeout(() => {
          preloader.classList.add('hidden');
          document.body.style.overflow = '';
          document.body.removeAttribute('aria-busy');
          sessionStorage.setItem('ricche-visited', '1');
        }, 1000);
      });
    }
  }

  // ---- Theme Toggle (dark mode default) ----
  const toggle = document.getElementById('themeToggle');
  const html = document.documentElement;

  const saved = localStorage.getItem('ricche-theme');
  if (saved) {
    html.setAttribute('data-theme', saved);
  } else {
    html.setAttribute('data-theme', 'dark');
  }

  if (toggle) {
    // Sync aria-checked with initial theme
    toggle.setAttribute('aria-checked', html.getAttribute('data-theme') === 'dark');

    toggle.addEventListener('click', () => {
      const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem('ricche-theme', next);
      toggle.setAttribute('aria-checked', next === 'dark');
    });
  }

  // ---- Header scroll effect ----
  const header = document.getElementById('header');
  if (header && !header.classList.contains('scrolled')) {
    window.addEventListener('scroll', () => {
      header.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });
  }

  // ---- Mobile nav ----
  const navToggle = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');

  if (navToggle && navMenu) {
    function lockScroll() {
      var scrollY = window.scrollY;
      document.body.style.position = 'fixed';
      document.body.style.top = '-' + scrollY + 'px';
      document.body.style.width = '100%';
      document.body.style.overflow = 'hidden';
      document.body.style.overscrollBehavior = 'none';
    }
    function unlockScroll() {
      var scrollY = parseInt(document.body.style.top || '0', 10) * -1;
      document.body.style.position = '';
      document.body.style.top = '';
      document.body.style.width = '';
      document.body.style.overflow = '';
      document.body.style.overscrollBehavior = '';
      window.scrollTo(0, scrollY);
    }

    navToggle.addEventListener('click', () => {
      navToggle.classList.toggle('open');
      navMenu.classList.toggle('open');
      const isOpen = navMenu.classList.contains('open');
      navToggle.setAttribute('aria-expanded', isOpen);
      if (isOpen) {
        lockScroll();
      } else {
        unlockScroll();
      }
    });

    navMenu.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('open');
        navMenu.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        unlockScroll();
      });
    });

    // Close mobile nav on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && navMenu.classList.contains('open')) {
        navToggle.classList.remove('open');
        navMenu.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        unlockScroll();
        navToggle.focus();
      }
    });
  }

  // ---- Active nav on scroll ----
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link[data-section]');

  if (navLinks.length) {
    function updateNav() {
      const y = window.scrollY + window.innerHeight * 0.35;
      sections.forEach(sec => {
        const top = sec.offsetTop;
        const id = sec.id;
        if (y >= top && y < top + sec.offsetHeight) {
          navLinks.forEach(l => {
            const isActive = l.dataset.section === id;
            l.classList.toggle('active', isActive);
            if (isActive) l.setAttribute('aria-current', 'page');
            else l.removeAttribute('aria-current');
          });
        }
      });
    }
    window.addEventListener('scroll', updateNav, { passive: true });
  }

  // ---- Scroll Reveal (IntersectionObserver) ----
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const idx = el.getAttribute('data-index');
          if (idx !== null) el.style.setProperty('--index', idx);
          el.classList.add('visible');
          observer.unobserve(el);
        }
      });
    }, {
      threshold: 0.06,
      rootMargin: '0px 0px -30px 0px'
    });
    reveals.forEach(el => observer.observe(el));
  }

  // ---- Counter animation (re-triggers every scroll, daily increments) ----
  // Base values and daily growth rates (proportional to size)
  const counterConfig = {
    '128': { base: 128, dailyRate: 2, max: 500 },        // Experiments: +~2/day, cap at 500
    '2540': { base: 2540, dailyRate: 45, max: 10000 },   // Simulation Jobs: +~45/day, cap at 10k
    '6': { base: 6, dailyRate: 0.15, max: 24 }           // Active Validations: +~0.15/day, cap at 24
  };

  // Calculate days since a fixed reference date for consistent growth
  const refDate = new Date('2025-01-01').getTime();
  const daysSinceRef = (Date.now() - refDate) / (1000 * 60 * 60 * 24);

  function getDailyTarget(baseTarget) {
    const cfg = counterConfig[String(baseTarget)];
    if (!cfg) return baseTarget;
    return Math.min(Math.round(cfg.base + cfg.dailyRate * daysSinceRef), cfg.max);
  }

  const counters = document.querySelectorAll('.stat-number[data-target]');
  if (counters.length) {
    // Track animation state per counter
    const counterState = new Map();
    counters.forEach(el => {
      counterState.set(el, { animating: false, wasVisible: false });
    });

    function animateCount(el, target) {
      const state = counterState.get(el);
      if (state.animating) return;
      state.animating = true;

      const dur = 2200;
      const start = performance.now();
      function tick(now) {
        const t = Math.min((now - start) / dur, 1);
        const ease = 1 - Math.pow(1 - t, 4);
        el.textContent = Math.round(ease * target).toLocaleString();
        if (t < 1) {
          requestAnimationFrame(tick);
        } else {
          state.animating = false;
        }
      }
      requestAnimationFrame(tick);
    }

    // Use IntersectionObserver but DON'T unobserve — re-trigger on every enter
    const counterObs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const el = entry.target;
        const state = counterState.get(el);
        if (entry.isIntersecting && !state.wasVisible) {
          // Entered viewport — animate
          state.wasVisible = true;
          const baseTarget = parseInt(el.dataset.target, 10);
          const target = getDailyTarget(baseTarget);
          el.textContent = '0';
          animateCount(el, target);
        } else if (!entry.isIntersecting && state.wasVisible) {
          // Left viewport — reset so it re-triggers next scroll
          state.wasVisible = false;
          el.textContent = '0';
        }
      });
    }, { threshold: 0.3 });

    counters.forEach(el => counterObs.observe(el));
  }

  // ---- Architecture pipeline scroll progress ----
  const archPipeline = document.getElementById('archPipeline');
  const archFill = document.getElementById('archProgressFill');

  if (archPipeline && archFill) {
    const archSteps = archPipeline.querySelectorAll('.arch-step');

    function updateArchProgress() {
      const viewH = window.innerHeight;
      const triggerY = viewH * 0.75;

      const pipeRect = archPipeline.getBoundingClientRect();
      const pipeTop = pipeRect.top;
      const pipeHeight = pipeRect.height;
      const totalSteps = archSteps.length;

      // Smooth continuous fill based on exact scroll position
      // The fill tracks from the first dot to the last dot
      let firstDotY = 0;
      let lastDotY = pipeHeight;
      const dotPositions = [];

      archSteps.forEach((step, idx) => {
        const dot = step.querySelector('.arch-dot');
        const connector = step.querySelector('.arch-connector');
        if (!dot) return;

        const dotRect = dot.getBoundingClientRect();
        const dotCenter = dotRect.top + dotRect.height / 2;
        const relY = dotCenter - pipeRect.top;
        dotPositions.push(relY);

        if (dotCenter < triggerY) {
          dot.classList.add('reached');
          if (connector) connector.classList.add('reached');
        } else {
          dot.classList.remove('reached');
          if (connector) connector.classList.remove('reached');
        }
      });

      if (dotPositions.length > 1 && pipeHeight > 0) {
        firstDotY = dotPositions[0];
        lastDotY = dotPositions[dotPositions.length - 1];

        // Where is the trigger line relative to the pipeline?
        const triggerRelY = triggerY - pipeRect.top;

        // Map trigger position smoothly between first and last dot
        let progress = (triggerRelY - firstDotY) / (lastDotY - firstDotY);
        progress = Math.max(0, Math.min(1, progress));

        archFill.style.height = (progress * 100) + '%';
      }
    }

    // Debounce scroll/resize with rAF to avoid layout thrashing
    let archTicking = false;
    function onArchScroll() {
      if (!archTicking) {
        archTicking = true;
        requestAnimationFrame(() => {
          updateArchProgress();
          archTicking = false;
        });
      }
    }
    window.addEventListener('scroll', onArchScroll, { passive: true });
    window.addEventListener('resize', onArchScroll, { passive: true });
    updateArchProgress();
  }

  // ---- About chart — animate once per scroll into view ----
  const streamFills = document.querySelectorAll('.stream-fill');
  if (streamFills.length) {
    const streamObs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Reset and re-trigger
          streamFills.forEach(el => {
            el.classList.remove('animate-once');
            void el.offsetWidth; // force reflow
            el.classList.add('animate-once');
          });
        } else {
          // Reset when leaving so it re-triggers next time
          streamFills.forEach(el => el.classList.remove('animate-once'));
        }
      });
    }, { threshold: 0.3 });
    const streamContainer = document.querySelector('.hero-visual');
    if (streamContainer) streamObs.observe(streamContainer);
  }

  // ---- Smooth scroll for anchor links ----
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        window.scrollTo({
          top: target.getBoundingClientRect().top + window.scrollY - 76,
          behavior: 'smooth'
        });
      }
    });
  });

})();
