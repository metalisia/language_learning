const CACHE_NAME = 'linguo-v4';
const ASSETS = [
  '/',
  '/index.html',
  '/polish/flashcards.html',
  '/polish/word_bank.json',
  '/italian/flashcards.html',
  '/manifest.json',
  '/images/icon-192.svg',
  '/images/icon-512.svg',
];

// Install: pre-cache all assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

// Activate: clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch: cache-first, fall back to network
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request).then((response) => {
        // Cache new successful requests
        if (response.ok && event.request.method === 'GET') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return response;
      });
    }).catch(() => {
      // If offline and not cached, return the main page
      return caches.match('/index.html');
    })
  );
});
