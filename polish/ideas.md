# v5+ Feature Ideas - Novel Learning Modes

Ideas for future versions. Ranked by impact and feasibility.

---

## Top 3 Priority

### 1. "The Forger" - Error Detective Mode
Show Polish sentences - some correct, some with subtle errors (wrong gender agreement, wrong case ending, wrong word order). User spots and taps the broken word.

**Why:** Trains grammatical intuition without grammar lectures. Native speakers use grammar by *feeling* something is off ("negative evidence"). No consumer app does this.

**Examples:**
- `"Widzę duża psa"` - wrong! (duża -> dużego, accusative masculine animate)
- `"Ona czytał książkę"` - wrong! (czytał is masculine past, should be czytała)
- `"Idę do sklep"` - wrong! (should be sklepu, genitive after "do")

**Data:** Generate programmatically from word_bank by introducing controlled errors (wrong case form, wrong gender suffix, wrong conjugation person).

---

### 2. "Pattern Surfing" - Grammar Without Rules
Show 4-5 Polish sentences sharing the same grammatical pattern. Pattern highlighted but never named. User generates a new sentence using the same pattern with different vocabulary.

**Why:** How children acquire grammar - statistical pattern extraction, not rule memorization. User absorbs that after "nie mam" the noun changes form without ever hearing "genitive case."

**Example:**
```
Nie mam [psa]         - I don't have a dog
Nie mam [kota]        - I don't have a cat
Nie mam [pieniędzy]   - I don't have money
Nie mam [czasu]       - I don't have time
Nie mam [______]      - I don't have a ___
```

**Patterns to cover:**
- "do + genitive" (idę do szkoły/sklepu/domu)
- "lubię + infinitive" (lubię jeść/pić/czytać)
- "jest + nominative adjective" (kawa jest gorąca/zimna/dobra)
- Adjective agreement across genders
- Word order (negation position, reflexive "się" placement)

---

### 3. "Sentence Surgery" - Transformation Drills
Given a Polish sentence, transform it: make it negative, change the tense, swap the subject, make it a question. One transformation at a time.

**Why:** Instead of learning forms in isolation, learn how Polish transforms meaning. Each step teaches one micro-rule. Low cognitive load because you're modifying a sentence you already understand. Used in military language training (DLI), almost never in consumer apps.

**Example chain:**
```
"On czyta książkę"    (He reads a book)
-> Make it negative:   "On nie czyta książki"  (genitive after negation!)
-> Change to past:     "On nie czytał książki"
-> Change to she:      "Ona nie czytała książki"
-> Make it a question: "Czy ona nie czytała książki?"
```

---

## More Ideas

### 4. "Word DNA" - Morphological X-Ray
Tap any Polish word and watch it explode into building blocks: root, prefix, suffix, ending - color-coded and explained. Then quiz: given building blocks, predict what a new word means.

**Examples:**
- `nie-za-pomni-any` -> not + completive + remember + passive adj = unforgettable
- `prze-pras-z-am` -> through + ask + conjugation + 1st person = I apologize
- `bez-dom-ny` -> without + house + adjective = homeless

**Quiz:** Show `bez-` (without) + `robót-` (work) + `-ny` (adj) -> ???. Answer: bezrobotny (unemployed). Never seen it, but can derive it.

---

### 5. "Inner Monologue" - Think, Don't Translate
App gives a situation (waking up, cooking, walking through city). No English prompt. Describe what you see/do/think in Polish using whatever words you know. Vocabulary sidebar to peek at. App highlights recognized words, gently suggests corrections.

**Why:** Breaks the English->Polish translation habit. Builds direct concept->Polish pathways. Every polyglot says this is the moment they started improving fast. No app trains it.

**Implementation:** Scene-based free writing with rule-based gentle nudges (no AI needed). Over time builds a private Polish "journal."

---

### 6. "The Eavesdropper" - Passive Listening
Overhear a Polish conversation (speech synthesis, no text shown). Answer comprehension questions: "Where are they going?" "What did she order?"

**Why:** Trains extracting meaning from partial understanding (catch 40% of words, still answer correctly). This is the actual skill needed day 1 in Poland.

**Progression:**
- Level 1: Unlimited replays, 0.7x speed
- Level 2: Fewer replays, 0.85x speed
- Level 3: One listen, normal speed, harder questions

---

### 7. "Reflex Chains" - Stimulus-Response Conditioning
Flash a situation icon + context. Produce the correct Polish response within 3 seconds. Pure reflex, no thinking.

**Why:** Targets procedural memory (like muscle memory) rather than declarative recall. Goal is automaticity - "Jak się masz?" -> "Dobrze, dziękuję" should be as automatic as catching a ball.

**Prompts:**
- [Hand wave] -> "Cześć!"
- [Question mark + face] -> "Nie rozumiem"
- [Coffee icon] -> "Poproszę kawę"
- [Clock 3:00] -> "Trzecia"

Miss the 3-second window = miss. Build streaks.

---

### 8. "Meaning Bridges" - Cross-Linguistic Connections
Show how Polish words connect to things you already know from English, Latin, French via Indo-European roots.

**Examples:**
- "woda" <-> "water" (PIE *wódr)
- "noc" <-> "night" <-> Latin "nox" <-> German "Nacht" (PIE *nókwts)
- "matka" <-> "mother" <-> Latin "mater" (PIE *méh2tēr)
- "nowy" <-> "new" <-> Latin "novus" <-> "novel" (PIE *néwos)

**Why:** Instead of random association, see they're literally the same word evolved over 5000 years. Memory becomes almost unforgettable.

---

## Design Principles

- All modes must work offline (no API calls)
- Generate exercises from existing word_bank data where possible
- Production > recognition (make the user generate, not just pick)
- Pattern > rules (show examples, don't explain grammar)
- Automaticity > accuracy (speed matters for real conversation)
