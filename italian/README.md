# Schede - Italian Language Trainer

A single-page web app for learning Italian vocabulary, built as a standalone HTML file with no dependencies.

`python3 -m http.server 8000  `

## Features

### Study Modes

- **Flashcards** — Flip cards showing an Italian word on the front and English translation on the back. Includes word type metadata (noun gender, verb, adjective). Supports hints that reveal the first letter with blanks. Verbs display IPA transcriptions.
- **Spelling** — Given an English word, type the Italian translation. Accepts answers with or without Italian accents (e.g. "citta" matches "città"). Shows the exact spelling after answering. Includes an on-screen Italian character keyboard (à, è, é, ì, ò, ù).
- **Multiple Choice** — Pick the correct translation from four options. Supports both directions: Italian → English and English → Italian.
- **Listening** — Hear an Italian word spoken aloud (via the browser's Speech Synthesis API, `it-IT` locale, 0.85x speed) and type its English meaning. Includes a replay button and hints. Requires the browser/OS to have an Italian voice installed.
- **Articles** — Practice Italian articles by filling in definite articles (il/la/l'/lo/i/le/gli), indefinite articles (un/una/un'/uno), partitive articles (dei/delle/degli), and plural noun forms, plus identifying the noun's grammatical gender (m/f).
- **Conjugation** — Practice present-tense verb conjugation (presente indicativo) by filling in all 6 person forms (io, tu, lui/lei, noi, voi, loro) for each of the 30 verbs. Each verb displays its IPA transcription and includes a collapsible pronunciation guide covering Italian sounds.
- **Gender** — Gender-aware practice mode testing adjective agreement and passato prossimo forms. Exercise types include:
  - *Adjective agreement*: given a noun, type the correctly gendered adjective (e.g. "libro grande" vs "casa grande" vs "piccolo" vs "piccola").
  - *Passato prossimo with essere*: fill in the correct past participle agreeing with the subject (e.g. "Lui è andato" vs "Lei è andata" vs "Loro sono andati").
  - *Passato prossimo with avere*: fill in the past participle (e.g. "Io ho mangiato").

### Vocabulary

150+ words organized into categories:

| Category | Type | Count |
|---|---|---|
| People, Animals, Food, Home, Nature, Body, Objects, Places, Concepts, Misc | Nouns | 100 |
| — | Verbs | 30 |
| — | Adjectives | 20 |

Noun entries include plural forms, definite/indefinite/partitive articles for both singular and plural, and grammatical gender.

Verb entries include present-tense conjugation for all 6 persons, passato prossimo past participle forms (masculine/feminine singular and plural), auxiliary verb (essere/avere), and IPA transcriptions.

Adjective entries include masculine singular, feminine singular, masculine plural, and feminine plural forms.

### Pronunciation Guide

A built-in reference for Italian pronunciation aimed at English speakers, accessible from the Conjugation tab. Covers 17 Italian sounds with:

- IPA transcription
- Plain-English description of how to produce each sound
- Special focus on sounds that differ from English: soft c/g (before e/i), hard ch/gh, double consonants, gl/gn combinations, accented vowels, and the z sound

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
- **Error pattern analysis** — horizontal bar chart breaking down mistakes by category (Accents, Gender, Articles, Conjugation, Vocabulary), with descriptions of your weakest areas and a reset option
- **Weak words list** — words with the lowest accuracy after 2+ reviews

### Error Pattern Analysis

Errors are automatically classified and tracked across all modes:

| Category | Tracked from | Description |
|---|---|---|
| Accents | Spelling, Conjugation, Gender | Correct letters but wrong/missing Italian accent marks |
| Gender | Articles, Gender | Wrong masculine/feminine form |
| Articles | Articles | Wrong definite/indefinite/partitive article |
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
- **Italian keyboard** — on-screen buttons for accented characters in spelling, conjugation, and gender modes

## Usage

Open `flashcards.html` in any modern browser. No server or build step required.
