// Ricche — Service Worker for offline caching
const CACHE_NAME = 'ricche-v33';
const ASSETS = [
  '/',
  '/index.html',
  '/contact',
  '/privacy',
  '/css/styles.min.css',
  '/js/animations.min.js',
  '/js/main.min.js',
  '/js/ai-network.min.js',
  '/fonts/inter-latin.woff2',
  '/fonts/space-grotesk-latin.woff2',
  '/assets/ricche-logo.png',
  '/manifest.json'
];

// Install: pre-cache core assets
self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(ASSETS);
    })
  );
  self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(keys) {
      return Promise.all(
        keys.filter(function(k) { return k !== CACHE_NAME; })
            .map(function(k) { return caches.delete(k); })
      );
    })
  );
  self.clients.claim();
});

// Fetch: network-first for HTML, cache-first for assets
self.addEventListener('fetch', function(e) {
  var url = new URL(e.request.url);

  // Skip non-GET and external requests
  if (e.request.method !== 'GET') return;
  if (url.origin !== self.location.origin) return;

  // HTML pages: network first, fallback to cache
  if (e.request.headers.get('accept') && e.request.headers.get('accept').includes('text/html')) {
    e.respondWith(
      fetch(e.request).then(function(res) {
        var clone = res.clone();
        caches.open(CACHE_NAME).then(function(cache) { cache.put(e.request, clone); });
        return res;
      }).catch(function() {
        return caches.match(e.request);
      })
    );
    return;
  }

  // Static assets: cache first, fallback to network
  e.respondWith(
    caches.match(e.request).then(function(cached) {
      if (cached) return cached;
      return fetch(e.request).then(function(res) {
        var clone = res.clone();
        caches.open(CACHE_NAME).then(function(cache) { cache.put(e.request, clone); });
        return res;
      });
    })
  );
});
