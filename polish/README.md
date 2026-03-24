# Fiszki - Polish Language Trainer

Polish module for the [Language Trainer](../README.md). Loaded via `app.html?lang=polish` using `config.json` for all language-specific data.

## Modes

15 study modes — the most complete language in the app:

- **Flashcards** — flip cards with word type metadata, hints, IPA for verbs
- **Spelling** — type the Polish translation, accepts answers with or without diacritics (e.g. "zly" matches "zly")
- **Multiple Choice** — four options, both directions (Polish <-> English)
- **Listening** — hear a word via Speech Synthesis API (`pl-PL`, 0.85x speed), type the meaning
- **Declension** — fill in noun cases (Nominative, Accusative, Genitive) x singular/plural + gender (m/f/n)
- **Conjugation** — present-tense verb conjugation for all 6 persons (ja, ty, on/ona/ono, my, wy, oni/one)
- **Gender** — adjective agreement (`duzy dom` vs `duza kobieta` vs `duze dziecko`) and past tense gender forms (1st person male/female, 3rd person he/she/it)
- **Cloze** — fill-in-the-blank sentences testing vocabulary, conjugation, and case forms
- **Numbers** — number-to-word, word-to-number, and price quiz (zloty/groszy)
- **Sentence Builder** — drag words into correct Polish word order
- **Speed Round** — timed two-option vocabulary quiz
- **Survival Phrases** — browse and quiz common phrases
- **Conversations** — guided dialogue practice with role-play
- **Reader** — paste/upload text or browse graded stories with knowledge overlay and density slider
- **Progress** — streak, activity chart, mastery breakdown, error patterns, weak words

## Vocabulary

| Type | Count | Details |
|---|---|---|
| Nouns | 122 | Full declension data (nom_pl, acc_sg, acc_pl, gen_sg, gen_pl), gender (m/f/n/pl), 10 thematic groups |
| Verbs | 40 | Present-tense conjugation (6 persons), past tense (5 gender forms), IPA |
| Adjectives | 30 | Nominative forms `[m, f, n]` |

Plural-only nouns (e.g. drzwi, okulary) are handled separately with reduced case forms.

## Pronunciation Guide

17 Polish sounds with IPA transcriptions and plain-English descriptions. Covers nasal vowels (a, e), soft consonants (c, s, z, n, dz), hard sibilants (sz, cz, z/rz, dz), and common surprises (l = /w/, w = /v/, o = /u/).

## Reader Mode

### Input Methods

| Method | Description |
|---|---|
| **Paste Text** | Paste any Polish text and hit "Read" |
| **Upload File** | Browse for a `.txt` file |
| **Library** | Graded stories with chunk-aligned EN/PL parallel text and density slider |

### Knowledge Overlay

Words are color-coded by SRS status (known/learning/unknown) with frequency-inferred knowledge and i+1 sprinkling for acquisition from context.

### Data Files

- `config.json` — all metadata, word bank, grammar data
- `sample_book.json` — graded reader library content
- `hermit_dave_top_500_pl.txt` — word frequency list for reader knowledge inference

## Error Categories

| Category | Sources |
|---|---|
| Diacritics | Spelling, Declension, Conjugation, Gender |
| Gender | Declension, Gender |
| Case Forms | Declension |
| Conjugation | Conjugation |
| Vocabulary | Spelling, Multiple Choice, Listening |
