// PDF Modal Viewer
(function() {
  var overlay = document.getElementById('pdfModal');
  var frame = document.getElementById('pdfModalFrame');
  var title = document.getElementById('pdfModalTitle');
  var closeBtn = document.getElementById('pdfModalClose');

  var isMobile = window.innerWidth <= 768;

  document.querySelectorAll('.pdf-trigger').forEach(function(el) {
    el.style.cursor = 'pointer';

    // Keyboard support for div[role="button"] triggers
    el.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      }
    });

    el.addEventListener('click', function() {
      var pdfSrc = this.getAttribute('data-pdf');
      var pdfTitle = this.getAttribute('data-title') || 'Document';

      if (isMobile) {
        window.open(pdfSrc, '_blank', 'noopener');
        return;
      }

      title.textContent = pdfTitle;
      frame.src = pdfSrc;
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
      closeBtn.focus();
    });
  });

  function closeModal() {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
    setTimeout(function() { frame.src = ''; }, 400);
  }

  closeBtn.addEventListener('click', closeModal);
  overlay.addEventListener('click', function(e) {
    if (e.target === overlay) closeModal();
  });
  document.addEventListener('keydown', function(e) {
    if (!overlay.classList.contains('active')) return;
    if (e.key === 'Escape') { closeModal(); return; }
    // Focus trap: cycle between close button and iframe
    if (e.key === 'Tab') {
      var focusable = [closeBtn, frame];
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey) {
        if (document.activeElement === first) { e.preventDefault(); last.focus(); }
      } else {
        if (document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    }
  });
})();

// Logo Flash
(function() {
  var logo = document.getElementById('logoTrigger');
  var flash = document.getElementById('logoFlash');
  if (!logo || !flash) return;

  logo.addEventListener('click', function(e) {
    e.preventDefault();
    flash.classList.add('active');
    setTimeout(function() {
      flash.classList.add('show');
    }, 10);
    setTimeout(function() {
      flash.classList.remove('show');
      setTimeout(function() {
        flash.classList.remove('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }, 600);
    }, 2200);
  });

  flash.addEventListener('click', function() {
    flash.classList.remove('show');
    setTimeout(function() { flash.classList.remove('active'); }, 600);
  });
})();

// Planet video — start 1.5s in, end 2.35s before end, loop
// Skip video load on mobile to save bandwidth
(function() {
  var v = document.getElementById('planetVideo');
  if (!v) return;

  if (window.innerWidth <= 768) {
    v.removeAttribute('autoplay');
    v.removeAttribute('src');
    v.querySelectorAll('source').forEach(function(s) { s.remove(); });
    v.load();
    return;
  }

  // Video error fallback — hide planet gracefully if video fails to load
  v.addEventListener('error', function() {
    var planet = document.getElementById('heroPlanet');
    if (planet) planet.style.opacity = '0';
  });
  var source = v.querySelector('source');
  if (source) {
    source.addEventListener('error', function() {
      var planet = document.getElementById('heroPlanet');
      if (planet) planet.style.opacity = '0';
    });
  }

  var startTime = 1.5;
  var endTime;
  v.addEventListener('loadedmetadata', function() {
    endTime = v.duration - 2.35;
    v.currentTime = startTime;
  });
  v.currentTime = startTime;
  v.addEventListener('timeupdate', function() {
    if (endTime && v.currentTime >= endTime) {
      v.currentTime = startTime;
    }
    if (v.currentTime < startTime) {
      v.currentTime = startTime;
    }
  });
})();

// Hero parallax — mouse interaction for planet, content, orbs
// Disabled on touch devices to save GPU and avoid janky interactions
(function() {
  var isTouch = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
  if (isTouch) return;

  var planet = document.getElementById('heroPlanet');
  var hero = document.getElementById('hero');
  var content = hero ? hero.querySelector('.hero-content') : null;
  var orbs = hero ? hero.querySelectorAll('.hero-orb') : [];
  var aurora = hero ? hero.querySelector('.hero-aurora') : null;
  if (!hero) return;

  var targetX = 0, targetY = 0, curX = 0, curY = 0;
  var isMoving = false;
  var idleTimer;

  // Collect all parallax elements for will-change management
  var parallaxEls = [planet, content, aurora].filter(Boolean);

  function enableWillChange() {
    parallaxEls.forEach(function(el) { el.style.willChange = 'transform'; });
  }
  function disableWillChange() {
    parallaxEls.forEach(function(el) { el.style.willChange = ''; });
  }

  document.addEventListener('mousemove', function(e) {
    var rect = hero.getBoundingClientRect();
    if (e.clientY < rect.top || e.clientY > rect.bottom) return;
    if (e.clientX < rect.left || e.clientX > rect.right) return;
    targetX = (e.clientX - rect.left) / rect.width - 0.5;
    targetY = (e.clientY - rect.top) / rect.height - 0.5;

    if (!isMoving) {
      isMoving = true;
      enableWillChange();
    }
    clearTimeout(idleTimer);
    idleTimer = setTimeout(function() {
      isMoving = false;
      disableWillChange();
    }, 1000);
  });
  hero.addEventListener('mouseleave', function() {
    targetX = 0;
    targetY = 0;
  });

  function animate() {
    curX += (targetX - curX) * 0.04;
    curY += (targetY - curY) * 0.04;

    if (planet) {
      planet.style.transform = 'translateY(-50%) translate(' + (curX * 35) + 'px,' + (curY * 35) + 'px)';
    }
    if (content) {
      content.style.transform = 'translate(' + (curX * 14) + 'px,' + (curY * 14) + 'px)';
    }
    orbs.forEach(function(orb, i) {
      var depth = 18 + i * 10;
      orb.style.setProperty('--px', (curX * depth) + 'px');
      orb.style.setProperty('--py', (curY * depth) + 'px');
    });
    if (aurora) {
      aurora.style.transform = 'translate(' + (curX * -10) + 'px,' + (curY * -10) + 'px)';
    }

    requestAnimationFrame(animate);
  }
  animate();
})();
