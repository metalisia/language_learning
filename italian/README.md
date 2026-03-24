# Schede - Italian Language Trainer

Italian module for the [Language Trainer](../README.md). Loaded via `app.html?lang=italian` using `config.json` for all language-specific data.

## Modes

8 study modes:

- **Flashcards** — flip cards with word type metadata, hints, IPA for verbs
- **Spelling** — type the Italian translation, accepts answers with or without accents (e.g. "citta" matches "citta")
- **Multiple Choice** — four options, both directions (Italian <-> English)
- **Listening** — hear a word via Speech Synthesis API (`it-IT`, 0.85x speed), type the meaning
- **Articles** — fill in definite articles (il/la/l'/lo/i/le/gli), indefinite articles (un/una/un'/uno), plural noun form, and gender (m/f)
- **Conjugation** — present-tense verb conjugation for all 6 persons (io, tu, lui/lei, noi, voi, loro)
- **Gender** — adjective agreement (`libro grande` vs `casa grande`) and passato prossimo with essere/avere (`Lui e andato` vs `Lei e andata`, `Io ho mangiato`)
- **Progress** — streak, activity chart, mastery breakdown, error patterns, weak words

## Vocabulary

| Type | Count | Details |
|---|---|---|
| Nouns | 100 | Plural form, definite/indefinite articles (sg/pl), gender (m/f), 10 thematic groups |
| Verbs | 30 | Present-tense conjugation (6 persons), passato prossimo participles (m_sg/f_sg/m_pl/f_pl + auxiliary), IPA |
| Adjectives | 20 | Four forms `{m, f, m_pl, f_pl}` |

## Pronunciation Guide

17 Italian sounds with IPA transcriptions and plain-English descriptions. Covers soft c/g (before e/i), hard ch/gh, double consonants, gl/gn combinations, accented vowels, and the z sound.

## Language-Specific Grammar

### Articles Mode

Tests all Italian article types in a single exercise:

| | Singular | Plural |
|---|---|---|
| **Definite** | il, lo, la, l' | i, gli, le |
| **Indefinite** | un, uno, una, un' | — |

### Gender in Past Tense

Italian passato prossimo requires choosing the correct auxiliary verb and agreeing the past participle with the subject:

- **Essere verbs**: participle agrees with subject gender/number (`andato/andata/andati/andate`)
- **Avere verbs**: participle is invariant (`mangiato`)

## Error Categories

| Category | Sources |
|---|---|
| Accents | Spelling, Conjugation, Gender |
| Gender | Articles, Gender |
| Articles | Articles |
| Conjugation | Conjugation |
| Vocabulary | Spelling, Multiple Choice, Listening |

## TODO

Port remaining modes from Polish:
- Cloze
- Numbers
- Sentence Builder
- Speed Round
- Survival Phrases
- Conversations
- Reader
