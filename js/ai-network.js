// Interactive particle network — trading dashboard aesthetic
// Stars orbit around planet video element, connected by pulsing glow lines
(function () {
  const canvas = document.getElementById('networkCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width, height, particles;
  const PARTICLE_COUNT = window.innerWidth <= 768 ? 30 : 60;
  const CONNECT_DIST = window.innerWidth <= 768 ? 120 : 180;
  const MOUSE_RADIUS = 220;
  let mouse = { x: -1000, y: -1000 };

  // Planet position (matches CSS: bottom -12%, left -8%, size 55vmin)
  let planet = { x: 0, y: 0, radius: 0 };
  const PLANET_ORBIT_DIST = 420;
  const PLANET_ATTRACT = 0.003;

  function getColor() {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    return isDark
      ? { r: 0, g: 136, b: 255, base: 0.5, line: 0.28, glow: 0.12 }
      : { r: 0, g: 85, b: 255, base: 0.4, line: 0.2, glow: 0.08 };
  }

  function resize() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = canvas.clientWidth;
    height = canvas.clientHeight;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    ctx.scale(dpr, dpr);

    // Sync planet position with the CSS .hero-planet element
    const planetEl = document.getElementById('heroPlanet');
    if (planetEl) {
      const r = planetEl.getBoundingClientRect();
      const cr = canvas.getBoundingClientRect();
      planet.x = r.left - cr.left + r.width / 2;
      planet.y = r.top - cr.top + r.height / 2;
      planet.radius = r.width / 2;
    } else {
      // Fallback — center-left
      const vmin = Math.min(width, height);
      planet.radius = vmin * 0.26;
      planet.x = width * 0.08 + planet.radius;
      planet.y = height * 0.5;
    }
  }

  function init() {
    particles = [];
    for (let i = 0; i < PARTICLE_COUNT; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.12,
        vy: (Math.random() - 0.5) * 0.12,
        r: Math.random() * 2 + 1.2,
        phase: Math.random() * Math.PI * 2,
        pulseSpeed: 0.0004 + Math.random() * 0.0005
      });
    }
  }

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Hide canvas entirely for reduced-motion preference
  if (prefersReduced) {
    canvas.style.display = 'none';
    return;
  }

  // Visibility tracking — pause animation when off-screen to save CPU
  let isVisible = false;
  let animId = null;

  function animate(t) {
    ctx.clearRect(0, 0, width, height);

    if (!isVisible) {
      animId = null;
      return;
    }

    const c = getColor();
    const globalPulse = 0.88 + Math.sin(t * 0.0003) * 0.12;

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];

      // Mouse interaction — attraction toward cursor
      const mdx = mouse.x - p.x;
      const mdy = mouse.y - p.y;
      const md = Math.sqrt(mdx * mdx + mdy * mdy);
      if (md < MOUSE_RADIUS && md > 0) {
        const f = (MOUSE_RADIUS - md) / MOUSE_RADIUS * 0.006;
        p.vx += mdx / md * f;
        p.vy += mdy / md * f;
      }

      // Planet gravity — gentle attraction so stars orbit near planet
      const pdx = planet.x - p.x;
      const pdy = planet.y - p.y;
      const pd = Math.sqrt(pdx * pdx + pdy * pdy);
      if (pd < PLANET_ORBIT_DIST && pd > planet.radius * 1.05) {
        const grav = PLANET_ATTRACT * (1 - pd / PLANET_ORBIT_DIST);
        p.vx += pdx / pd * grav;
        p.vy += pdy / pd * grav;
      }
      // Bounce off planet surface
      if (pd < planet.radius * 1.05 && pd > 0) {
        const pushF = 0.02;
        p.vx += -pdx / pd * pushF;
        p.vy += -pdy / pd * pushF;
      }

      p.vx *= 0.996;
      p.vy *= 0.996;
      p.x += p.vx;
      p.y += p.vy;

      if (p.x < -30) p.x = width + 30;
      if (p.x > width + 30) p.x = -30;
      if (p.y < -30) p.y = height + 30;
      if (p.y > height + 30) p.y = -30;

      const alpha = (c.base + Math.sin(t * p.pulseSpeed + p.phase) * 0.15) * globalPulse;
      const r = p.r * (0.9 + Math.sin(t * p.pulseSpeed * 1.5 + p.phase) * 0.2);

      // Outer glow halo
      ctx.beginPath();
      ctx.arc(p.x, p.y, r * 5, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${c.r},${c.g},${c.b},${alpha * c.glow})`;
      ctx.fill();

      // Medium glow
      ctx.beginPath();
      ctx.arc(p.x, p.y, r * 2.5, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${c.r},${c.g},${c.b},${alpha * 0.2})`;
      ctx.fill();

      // Core particle
      ctx.beginPath();
      ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${c.r},${c.g},${c.b},${alpha})`;
      ctx.fill();

      // Bright center dot
      ctx.beginPath();
      ctx.arc(p.x, p.y, r * 0.4, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${Math.min(c.r + 100, 255)},${Math.min(c.g + 100, 255)},255,${Math.min(alpha + 0.2, 1)})`;
      ctx.fill();

      // Connections — trading chart style lines
      for (let j = i + 1; j < particles.length; j++) {
        const p2 = particles[j];
        const cx = p.x - p2.x;
        const cy = p.y - p2.y;
        const cd = Math.sqrt(cx * cx + cy * cy);
        if (cd < CONNECT_DIST) {
          const proximity = 1 - cd / CONNECT_DIST;
          const lineAlpha = proximity * c.line * globalPulse;
          const lineWidth = proximity * 1.2 + 0.3;

          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.strokeStyle = `rgba(${c.r},${c.g},${c.b},${lineAlpha})`;
          ctx.lineWidth = lineWidth;
          ctx.stroke();

          if (proximity > 0.5) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = `rgba(${c.r},${c.g},${c.b},${lineAlpha * 0.3})`;
            ctx.lineWidth = lineWidth + 3;
            ctx.stroke();
          }
        }
      }

      // Connect particle to planet surface if close enough
      if (pd < PLANET_ORBIT_DIST && pd > planet.radius) {
        const surfX = planet.x + (p.x - planet.x) / pd * planet.radius;
        const surfY = planet.y + (p.y - planet.y) / pd * planet.radius;
        const proximity = 1 - (pd - planet.radius) / (PLANET_ORBIT_DIST - planet.radius);
        const lineAlpha = proximity * 0.18 * globalPulse;

        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(surfX, surfY);
        ctx.strokeStyle = `rgba(0,200,255,${lineAlpha})`;
        ctx.lineWidth = 0.8;
        ctx.stroke();
      }
    }

    animId = requestAnimationFrame(animate);
  }

  window.addEventListener('resize', () => { resize(); init(); });
  canvas.addEventListener('mousemove', (e) => {
    const r = canvas.getBoundingClientRect();
    mouse.x = e.clientX - r.left;
    mouse.y = e.clientY - r.top;
  });
  canvas.addEventListener('mouseleave', () => { mouse.x = -1000; mouse.y = -1000; });

  // Lazy-load: only run animation when canvas is in viewport
  var observer = new IntersectionObserver(function(entries) {
    isVisible = entries[0].isIntersecting;
    if (isVisible && !animId) {
      animId = requestAnimationFrame(animate);
    }
  }, { threshold: 0 });

  resize();
  init();
  observer.observe(canvas);
})();
