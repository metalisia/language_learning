# Fiszki - Polish Language Trainer

A single-page web app for learning Polish vocabulary, built as a standalone HTML file with no dependencies.

`python3 -m http.server 8000  `

## Features

### Study Modes

- **Flashcards** — Flip cards showing a Polish word on the front and English translation on the back. Includes word type metadata (noun gender, verb, adjective). Supports hints that reveal the first letter with blanks.
- **Spelling** — Given an English word, type the Polish translation. Accepts answers with or without Polish diacritics (e.g. "zly" matches "zły"). Shows the exact spelling after answering. Includes an on-screen Polish character keyboard (ą, ć, ę, ł, ń, ó, ś, ź, ż).
- **Multiple Choice** — Pick the correct translation from four options. Supports both directions: Polish → English and English → Polish.
- **Listening** — Hear a Polish word spoken aloud (via the browser's Speech Synthesis API, `pl-PL` locale, 0.85x speed) and type its English meaning. Includes a replay button and hints. Requires the browser/OS to have a Polish voice installed.
- **Declension** — Practice noun declension by filling in a grid of cases (Nominative, Accusative, Genitive) in both singular and plural forms, plus identifying the noun's grammatical gender (m/f/n).

### Vocabulary

150+ words organized into categories:

| Category | Type | Count |
|---|---|---|
| People, Animals, Food, Home, Nature, Body, Objects, Places, Concepts, Misc | Nouns | 100 |
| — | Verbs | 30 |
| — | Adjectives | 20 |

Noun entries include full declension data (nominative plural, accusative singular/plural, genitive singular/plural) and grammatical gender. Plural-only nouns (e.g. drzwi, okulary) are handled separately.

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
- **Weak words list** — words with the lowest accuracy after 2+ reviews

### Session Results

After completing a round, a results screen shows:

- Animated score ring with percentage
- Count of correct answers
- List of missed words for review
- Option to retry only missed words or start a new round

### UI / UX

- **Dark mode** — toggle between light and dark themes, preference saved in `localStorage`
- **Keyboard shortcuts** — full keyboard navigation for every mode (Space to flip, arrow keys, number keys for multiple choice, Enter to advance, etc.)
- **Responsive design** — adapts layout for mobile screens
- **Polish keyboard** — on-screen buttons for special characters in spelling and declension modes

## Usage

Open `flashcards.html` in any modern browser. No server or build step required.
