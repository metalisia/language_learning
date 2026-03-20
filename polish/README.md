# Fiszki - Polish Language Trainer

A single-page web app for learning Polish vocabulary, built as a standalone HTML file with no dependencies.

`python3 -m http.server 8000  `

## Features

### Study Modes

- **Flashcards** — Flip cards showing a Polish word on the front and English translation on the back. Includes word type metadata (noun gender, verb, adjective). Supports hints that reveal the first letter with blanks. Verbs display IPA transcriptions.
- **Spelling** — Given an English word, type the Polish translation. Accepts answers with or without Polish diacritics (e.g. "zly" matches "zły"). Shows the exact spelling after answering. Includes an on-screen Polish character keyboard (ą, ć, ę, ł, ń, ó, ś, ź, ż).
- **Multiple Choice** — Pick the correct translation from four options. Supports both directions: Polish → English and English → Polish.
- **Listening** — Hear a Polish word spoken aloud (via the browser's Speech Synthesis API, `pl-PL` locale, 0.85x speed) and type its English meaning. Includes a replay button and hints. Requires the browser/OS to have a Polish voice installed.
- **Declension** — Practice noun declension by filling in a grid of cases (Nominative, Accusative, Genitive) in both singular and plural forms, plus identifying the noun's grammatical gender (m/f/n).
- **Conjugation** — Practice present-tense verb conjugation by filling in all 6 person forms (ja, ty, on/ona/ono, my, wy, oni/one) for each of the 30 verbs. Each verb displays its IPA transcription and includes a collapsible pronunciation guide covering all Polish sounds.
- **Gender** — Gender-aware practice mode testing adjective agreement and past-tense gender forms. Exercise types include:
  - *Adjective agreement*: given a noun, type the correctly gendered adjective (e.g. "duży dom" vs "duża kobieta" vs "duże dziecko").
  - *Past tense 1st person*: fill in the correct form for male or female speakers (e.g. "byłem" vs "byłam").
  - *Past tense 3rd person*: fill in the correct he/she/it form (e.g. "on czytał" vs "ona czytała" vs "ono czytało").

### Vocabulary

150+ words organized into categories:

| Category | Type | Count |
|---|---|---|
| People, Animals, Food, Home, Nature, Body, Objects, Places, Concepts, Misc | Nouns | 100 |
| — | Verbs | 30 |
| — | Adjectives | 20 |

Noun entries include full declension data (nominative plural, accusative singular/plural, genitive singular/plural) and grammatical gender. Plural-only nouns (e.g. drzwi, okulary) are handled separately.

Verb entries include present-tense conjugation for all 6 persons, past-tense forms (masculine/feminine/neuter for 1st and 3rd person singular), and IPA transcriptions.

Adjective entries include masculine, feminine, and neuter nominative forms.

### Pronunciation Guide

A built-in reference for Polish pronunciation aimed at English speakers, accessible from the Conjugation tab. Covers 17 Polish sounds with:

- IPA transcription
- Plain-English description of how to produce each sound
- Special focus on sounds that don't exist in English: nasal vowels (ą, ę), soft consonants (ć, ś, ź, ń, dź), hard sibilants (sz, cz, ż/rz, dż), and common surprises (ł = /w/, w = /v/, ó = /u/)

### Word Groups

Filter vocabulary by thematic group (People, Animals, Food, etc.) or word type (Verbs, Adjectives). A **Smart Review** group surfaces words that are due for review based on the spaced repetition schedule.

### Spaced Repetition (Leitner System)

Words are tracked across 5 boxes with increasing review intervals (1, 2, 4, 8, 16 days). Correct answers promote a word to the next box; incorrect answers reset it to box 1. All progress is persisted in `localStorage`.

### Progress Tracker

A dedicated Progress tab showing:

- **Day streak** — consecutive days of practice
- **New words this week** — words seen for the first time in the last 7 days
- **Words seen** — total words encountered vs. total available
- **7-day activity chart** — bar chart of daily review counts
- **Word mastery breakdown** — stacked bar showing distribution across Leitner boxes (Unseen → Mastered)
- **Error pattern analysis** — horizontal bar chart breaking down mistakes by category (Diacritics, Gender, Case Forms, Conjugation, Vocabulary), with descriptions of your weakest areas and a reset option
- **Weak words list** — words with the lowest accuracy after 2+ reviews

### Error Pattern Analysis

Errors are automatically classified and tracked across all modes:

| Category | Tracked from | Description |
|---|---|---|
| Diacritics | Spelling, Declension, Conjugation, Gender | Correct letters but wrong/missing Polish special characters |
| Gender | Declension, Gender | Wrong masculine/feminine/neuter form |
| Case Forms | Declension | Wrong noun case form |
| Conjugation | Conjugation | Wrong verb conjugation form |
| Vocabulary | Spelling, Multiple Choice, Listening | Completely wrong word or meaning |

All error counts are persisted in `localStorage` and visualized in the Progress tab.

### Session Results

After completing a round, a results screen shows:

- Animated score ring with percentage
- Count of correct answers
- List of missed words for review
- Option to retry only missed words or start a new round

### UI / UX

- **Dark mode** — toggle between light and dark themes, preference saved in `localStorage`
- **Keyboard shortcuts** — full keyboard navigation for every mode (Space to flip, arrow keys, number keys for multiple choice, Enter to advance, Tab between conjugation fields, etc.)
- **Responsive design** — adapts layout for mobile screens
- **Polish keyboard** — on-screen buttons for special characters in spelling, declension, conjugation, and gender modes

## Usage

### Desktop

Open `flashcards.html` in any modern browser. No server or build step required.

### Mobile (PWA)

The app is a Progressive Web App — install it on your phone for offline access:

1. Start a local server from the `language_learning/` root:
   ```
   cd ~/language_learning
   python3 -m http.server 8000
   ```
   Or host the files on any static web server.

2. Open the URL on your phone (e.g. `http://<your-ip>:8000`)

3. You'll see a language selector — pick Polish or Italian

4. **Install to home screen:**
   - **Android (Chrome):** Tap the menu (three dots) > "Add to Home Screen" or "Install app"
   - **iOS (Safari):** Tap the share button > "Add to Home Screen"

5. The app now works like a native app — own icon, no browser bar, fully offline

All your progress is saved in the browser's localStorage and persists across sessions.
