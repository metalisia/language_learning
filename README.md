# Language Trainer

A PWA for learning Polish and Italian vocabulary. No dependencies, no build step — just static HTML files with offline support.

## Languages

- **Polish** — flashcards, spelling, multiple choice, listening, declension, conjugation, gender
- **Italian** — flashcards, spelling, multiple choice, listening, articles, conjugation, gender

See each language's README for full feature details: [Polish](polish/README.md) | [Italian](italian/README.md)

## Hosting

### GitHub Pages (recommended)

1. Push the repo to GitHub and make it public
2. Go to **Settings → Pages → Source**, select the `main` branch and `/` root
3. Your site will be live at `https://<username>.github.io/language_learning/`

After the first visit, the service worker caches everything for offline use.

### Local server

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000` in your browser.

To access from your phone on the same Wi-Fi:

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

Then open `http://<your-local-ip>:8000` on your phone. Find your IP with:
- **Linux:** `hostname -I`
- **macOS:** `ipconfig getifaddr en0`

### Any static host

Upload the files to any static hosting service (Netlify, Vercel, Cloudflare Pages, etc.). No server-side code is needed.

## Installing on mobile

The app is a Progressive Web App. After opening it in your phone's browser:

- **Android (Chrome):** Menu → "Add to Home Screen" or "Install app"
- **iOS (Safari):** Share button → "Add to Home Screen"

Once installed, it runs like a native app (no browser bar, works offline).

## Data & Progress

All progress is stored in the browser's `localStorage` — no account or server needed. Data persists across sessions and works fully offline.

| Key | Polish | Italian | Description |
|---|---|---|---|
| SRS | `fiszki_srs` | `schede_srs` | Spaced repetition box assignments and review dates |
| Stats | `fiszki_stats` | `schede_stats` | Daily activity counts, streak, last active date |
| Errors | `fiszki_errors` | `schede_errors` | Error pattern counts by category |
| Dark mode | `fiszki_dark` | `schede_dark` | Theme preference |

To reset all progress, go to the **Progress** tab and click **Reset All Progress**. This clears SRS data, stats, and error patterns (with a confirmation prompt). Alternatively, clear site data from your browser settings.
