# Language Trainer

A PWA for learning Polish and Italian vocabulary. No dependencies, no build step — just static HTML files with offline support.

## Architecture

A single shared `app.html` serves both languages, parameterized via URL:

```
app.html?lang=polish
app.html?lang=italian
```

Each language has its own `config.json` containing metadata, word bank data, and grammar-specific data. The app loads the config at startup and adapts all UI, modes, and grammar logic to the selected language.

```
language_learning/
  index.html          # Language selector (links to app.html?lang=...)
  app.html            # Shared app, config-driven
  polish/
    config.json       # Polish metadata + word bank + grammar data
    sample_book.json  # Reader mode library content
    hermit_dave_top_500_pl.txt  # Frequency list for reader
  italian/
    config.json       # Italian metadata + word bank + grammar data
```

### Config Structure

Each `config.json` provides:

| Field | Description |
|---|---|
| `lang` | Language code (`"pl"` or `"it"`) |
| `name` | Display name (`"Polish"` or `"Italian"`) |
| `appName` | App branding (`"Fiszki"` or `"Schede"`) |
| `speechLang` | TTS locale (`"pl-PL"` or `"it-IT"`) |
| `storagePrefix` | localStorage key prefix (`"fiszki"` or `"schede"`) |
| `specialChars` | On-screen keyboard characters (e.g. `["ą","ć","ę","ł","ń","ó","ś","ź","ż"]`) |
| `modes` | Array of mode IDs to show in the nav |
| `grammarMode` | Language-specific grammar mode (`declension` or `articles`) |
| `genderSystem` | Gender categories (`["m","f","n"]` or `["m","f"]`) |
| `conjLabels` | Conjugation person labels (e.g. `["ja","ty","on/ona/ono",...]`) |
| `nouns`, `verbs`, `adjectives` | Word bank data with language-specific fields |
| `pronunciationGuide` | Sound reference entries |
| `genderNouns` | Nouns used in gender agreement exercises |
| `verbPastData` | Past tense forms for gender mode |

## Languages

### Shared Modes (both languages)

All core study modes work identically across languages:

- **Flashcards** — flip cards with word type metadata, hints, IPA for verbs
- **Spelling** — type the translation, accepts answers with or without diacritics
- **Multiple Choice** — four options, both directions (target language <-> English)
- **Listening** — hear a word via Speech Synthesis API, type the English meaning
- **Conjugation** — fill in all 6 person forms for present tense
- **Gender** — adjective agreement and past tense gender exercises (language-aware, see below)
- **Progress** — streak, activity chart, mastery breakdown, error patterns, weak words

### Polish-Only Modes

| Mode | Description |
|---|---|
| **Declension** | Fill in noun cases (nominative, accusative, genitive) x singular/plural + gender (m/f/n) |
| **Cloze** | Fill-in-the-blank sentences testing vocabulary, conjugation, and case forms |
| **Numbers** | Number-to-word, word-to-number, and price quiz (zloty/groszy) |
| **Sentence Builder** | Drag words into correct Polish word order |
| **Speed Round** | Timed two-option vocabulary quiz |
| **Survival Phrases** | Browse and quiz common phrases |
| **Conversations** | Guided dialogue practice with role-play |
| **Reader** | Paste/upload text or browse a library with knowledge overlay and density slider |

### Italian-Only Modes

| Mode | Description |
|---|---|
| **Articles** | Fill in definite/indefinite articles (il/la/l'/lo/i/le/gli, un/una/un'/uno) + plural form + gender (m/f) |

### Language-Aware Differences

Even in shared modes, the app adapts to each language's grammar:

| Feature | Polish | Italian |
|---|---|---|
| Grammar mode | Declension (6 cases x sg/pl) | Articles (def/indef x sg/pl) |
| Gender system | 3 genders (m/f/n) | 2 genders (m/f) |
| Adjective order | Adjective + noun (`duzy dom`) | Noun + adjective (`libro grande`) |
| Past tense | Simple past with gender (`bylem/bylam`) | Passato prossimo with auxiliary (`sono andato/andata`) |
| Noun data | Case forms (nom, acc, gen x sg/pl) | Plural + article forms (def/indef x sg/pl) |
| Adjective forms | Array `[m, f, n]` | Object `{m, f, m_pl, f_pl}` |
| Diacritics | `a c e l n o s z z` | `a e e i o u` |
| Special chars keyboard | `a c e l n o s z z` | `a e e i o u` |

### Vocabulary

| | Polish | Italian |
|---|---|---|
| Nouns | 122 | 100 |
| Verbs | 40 | 30 |
| Adjectives | 30 | 20 |
| Categories | People, Animals, Food, Home, Nature, Body, Objects, Places, Concepts, Misc | Same |
| CEFR levels | A1-B2 | A1-B2 |

## Shared Features

### Spaced Repetition (Leitner System)

Words are tracked across 5 boxes with increasing review intervals (1, 2, 4, 8, 16 days). Correct answers promote a word to the next box; incorrect answers reset it to box 1. All progress is persisted in `localStorage`.

### Word Groups

Filter vocabulary by thematic group (People, Animals, Food, etc.) or word type (Verbs, Adjectives). A **Smart Review** group surfaces words due for review based on the spaced repetition schedule.

### CEFR Level Filter

Filter vocabulary by CEFR proficiency level (A1, A2, B1, B2). Selection is saved per language.

### Error Pattern Analysis

Errors are automatically classified and tracked across all modes:

| Category | Description |
|---|---|
| Diacritics/Accents | Correct letters but wrong/missing special characters |
| Gender | Wrong masculine/feminine/neuter form |
| Case Forms | Wrong noun case (Polish only) |
| Articles | Wrong article form (Italian only) |
| Conjugation | Wrong verb conjugation |
| Vocabulary | Completely wrong word or meaning |

### Session Results

After completing a round: animated score ring, correct count, missed words list, retry missed or start new round.

### Pronunciation Guide

Built-in reference accessible from the Conjugation tab, covering sounds that differ from English with IPA transcriptions and plain-English descriptions.

### UI / UX

- **Dark mode** — shared across languages, saved in `localStorage`
- **Keyboard shortcuts** — full keyboard navigation for every mode
- **Responsive design** — adapts for mobile screens
- **Language-specific keyboard** — on-screen buttons for special characters

## Hosting

### GitHub Pages (recommended)

1. Push the repo to GitHub and make it public
2. Go to **Settings -> Pages -> Source**, select the `main` branch and `/` root
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

## Installing on Mobile

The app is a Progressive Web App. After opening it in your phone's browser:

- **Android (Chrome):** Menu -> "Add to Home Screen" or "Install app"
- **iOS (Safari):** Share button -> "Add to Home Screen"

Once installed, it runs like a native app (no browser bar, works offline).

## Data & Progress

All progress is stored in the browser's `localStorage` — no account or server needed. Data persists across sessions and works fully offline.

| Key | Polish | Italian | Description |
|---|---|---|---|
| SRS | `fiszki_srs` | `schede_srs` | Spaced repetition box assignments and review dates |
| Stats | `fiszki_stats` | `schede_stats` | Daily activity counts, streak, last active date |
| Errors | `fiszki_errors` | `schede_errors` | Error pattern counts by category |
| Dark mode | `lang_trainer_dark` | `lang_trainer_dark` | Shared theme preference |

To reset all progress, go to the **Progress** tab and click **Reset All Progress**.

## Reader Mode (Polish only)

The Reader mode turns any Polish text into a learning tool by overlaying your vocabulary knowledge onto real content.

### Input Methods

| Method | Description |
|---|---|
| **Paste Text** | Paste any Polish text and hit "Read" |
| **Upload File** | Browse for a `.txt` file from your device |
| **Library** | Pick from curated graded stories with chunk-aligned EN/PL parallel text and a density slider |

### How It Works

Every word in the text is checked against your knowledge model:

- **Known words** (SRS box >= 3) — shown in green
- **Learning words** (SRS box 1-2) — shown in blue
- **Frequency-inferred words** — common words shown in italic
- **Unknown words** — highlighted in yellow; tap to see translation
- **Function words** (top 50 most common) — prioritized for target language display in Library mode

The Library mode features a **density slider** (EN to PL) that controls how much Polish vs English is shown, plus **i+1 sprinkling** — intentionally showing 1-2 words just outside your knowledge per sentence to promote acquisition from context.

## TODO

### Italian parity

Port remaining modes from Polish to Italian. Italian currently has: Flashcards, Spelling, Multiple Choice, Listening, Articles, Conjugation, Gender, Progress. Missing:

- Cloze
- Numbers
- Sentence Builder
- Speed Round
- Survival Phrases
- Conversations
- Reader

### Adding a new language

1. Create `{lang}/config.json` following the schema above
2. Add a card to `index.html` linking to `app.html?lang={lang}`
3. Add language-specific grammar branching in `app.html` if the language has unique grammar modes

### Reader: EPUB support (planned)

Upload two EPUB files (English + target language) for automatic sentence alignment and reading with knowledge overlay. See [Polish README](polish/README.md) for technical details.
