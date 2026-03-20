#!/usr/bin/env python3
"""
Tests for polish/word_bank.json data quality.

Validates:
  - JSON structure & required fields
  - No profanity in any language field
  - Declension pattern consistency (gender ↔ ending patterns)
  - Conjugation completeness (6 forms per verb)
  - Adjective forms completeness (3 forms: m/f/n)
  - CEFR levels are valid
  - No duplicate entries
  - Conversation structure & completeness
  - Example sentence structure
"""

import json
import os
import sys
import unittest
from collections import Counter

WORD_BANK_PATH = os.path.join(os.path.dirname(__file__), '..', 'polish', 'word_bank.json')

# Known Polish profanity / vulgar words to flag
PROFANITY_PL = {
    'kurwa', 'kurwy', 'kurwę', 'kurwo',
    'chuj', 'chuja', 'chujem', 'chuju',
    'pierdolić', 'pierdol', 'pierdolę', 'pierdoli',
    'jebać', 'jebany', 'jebana', 'jebane', 'jeb',
    'suka', 'suki', 'sukę',
    'dupek', 'dupa', 'dupę', 'dupy',
    'gówno', 'gówna',
    'cholera',  # mild but flagged for review
    'kurde',
    'skurwysyn', 'skurwiel',
    'spierdalaj', 'spierdolić',
    'wkurwić', 'wkurwiony',
    'zajebisty', 'zajebiste',
    'zasraniec', 'zasrany',
}

PROFANITY_EN = {
    'fuck', 'fucking', 'fucked', 'fucker',
    'shit', 'shitty', 'bullshit',
    'ass', 'asshole',
    'bitch', 'bitches',
    'damn', 'damned',
    'dick', 'cock', 'cunt',
    'bastard', 'whore', 'slut',
}

VALID_GENDERS = {'m', 'f', 'n', 'pl'}
VALID_CEFR = {'A1', 'A2', 'B1', 'B2', 'C1', 'C2'}
VALID_SPEAKERS = {'you', 'other'}

# Common Polish noun ending patterns by gender
# These are heuristics, not absolute rules
FEMININE_ENDINGS = ('a', 'ć', 'ść')
NEUTER_ENDINGS = ('o', 'e', 'ę', 'um')
# Masculine is the catch-all (consonant endings mostly)


class TestWordBankStructure(unittest.TestCase):
    """Test that word_bank.json has valid structure."""

    @classmethod
    def setUpClass(cls):
        with open(WORD_BANK_PATH, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)

    def test_top_level_keys(self):
        required = {'nouns', 'verbs', 'adjectives'}
        self.assertTrue(required.issubset(self.data.keys()),
                        f"Missing keys: {required - set(self.data.keys())}")

    def test_nouns_not_empty(self):
        self.assertGreater(len(self.data['nouns']), 0)

    def test_verbs_not_empty(self):
        self.assertGreater(len(self.data['verbs']), 0)

    def test_adjectives_not_empty(self):
        self.assertGreater(len(self.data['adjectives']), 0)


class TestNounFields(unittest.TestCase):
    """Test noun entries have required fields and valid values."""

    @classmethod
    def setUpClass(cls):
        with open(WORD_BANK_PATH, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)
        cls.nouns = cls.data['nouns']

    def test_required_fields(self):
        required = {'pl', 'en', 'gender', 'nom_pl', 'group', 'level'}
        for i, noun in enumerate(self.nouns):
            with self.subTest(i=i, word=noun.get('pl', '?')):
                self.assertTrue(required.issubset(noun.keys()),
                                f"Noun {noun.get('pl','?')} missing: {required - set(noun.keys())}")

    def test_singular_nouns_have_case_forms(self):
        """Non-plural-only nouns must have acc_sg, acc_pl, gen_sg, gen_pl."""
        required_sg = {'acc_sg', 'acc_pl', 'gen_sg', 'gen_pl'}
        for i, noun in enumerate(self.nouns):
            if noun['gender'] == 'pl':
                continue
            with self.subTest(i=i, word=noun['pl']):
                self.assertTrue(required_sg.issubset(noun.keys()),
                                f"Noun '{noun['pl']}' (gender={noun['gender']}) missing: "
                                f"{required_sg - set(noun.keys())}")

    def test_plural_only_nouns_have_plural_forms(self):
        """Plural-only nouns must have acc_pl and gen_pl."""
        for i, noun in enumerate(self.nouns):
            if noun['gender'] != 'pl':
                continue
            with self.subTest(i=i, word=noun['pl']):
                self.assertIn('acc_pl', noun, f"Plural noun '{noun['pl']}' missing acc_pl")
                self.assertIn('gen_pl', noun, f"Plural noun '{noun['pl']}' missing gen_pl")

    def test_valid_gender(self):
        for i, noun in enumerate(self.nouns):
            with self.subTest(i=i, word=noun['pl']):
                self.assertIn(noun['gender'], VALID_GENDERS,
                              f"Noun '{noun['pl']}' has invalid gender: {noun['gender']}")

    def test_valid_cefr_level(self):
        for i, noun in enumerate(self.nouns):
            with self.subTest(i=i, word=noun['pl']):
                self.assertIn(noun['level'], VALID_CEFR,
                              f"Noun '{noun['pl']}' has invalid CEFR: {noun['level']}")

    def test_no_empty_strings(self):
        for i, noun in enumerate(self.nouns):
            with self.subTest(i=i, word=noun.get('pl', '?')):
                for key, val in noun.items():
                    if isinstance(val, str):
                        self.assertTrue(val.strip(), f"Noun '{noun['pl']}' has empty '{key}'")

    def test_gender_ending_heuristic(self):
        """Flag nouns whose endings seem inconsistent with declared gender.
        These are warnings, not hard failures — Polish has exceptions."""
        warnings = []
        for noun in self.nouns:
            if noun['gender'] == 'pl':
                continue
            word = noun['pl'].lower()
            g = noun['gender']
            if g == 'f' and not word.endswith(FEMININE_ENDINGS) and word not in ('noc', 'krew', 'sól'):
                warnings.append(f"  '{noun['pl']}' marked feminine but ends in '{word[-1]}'")
            if g == 'n' and not word.endswith(NEUTER_ENDINGS):
                warnings.append(f"  '{noun['pl']}' marked neuter but ends in '{word[-1]}'")
        if warnings:
            print(f"\n  GENDER HEURISTIC WARNINGS ({len(warnings)} items):")
            for w in warnings[:10]:
                print(w)
            if len(warnings) > 10:
                print(f"  ... and {len(warnings)-10} more")

    def test_no_duplicate_nouns(self):
        pls = [n['pl'] for n in self.nouns]
        dupes = [w for w, c in Counter(pls).items() if c > 1]
        self.assertEqual(dupes, [], f"Duplicate nouns: {dupes}")


class TestVerbFields(unittest.TestCase):
    """Test verb entries have required fields and valid conjugation data."""

    @classmethod
    def setUpClass(cls):
        with open(WORD_BANK_PATH, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)
        cls.verbs = cls.data['verbs']

    def test_required_fields(self):
        required = {'pl', 'en', 'level', 'conj'}
        for i, verb in enumerate(self.verbs):
            with self.subTest(i=i, word=verb.get('pl', '?')):
                self.assertTrue(required.issubset(verb.keys()),
                                f"Verb '{verb.get('pl','?')}' missing: {required - set(verb.keys())}")

    def test_conjugation_has_six_forms(self):
        """Each verb must have exactly 6 conjugation forms (ja/ty/on/my/wy/oni)."""
        for i, verb in enumerate(self.verbs):
            with self.subTest(i=i, word=verb['pl']):
                self.assertIsInstance(verb['conj'], list)
                self.assertEqual(len(verb['conj']), 6,
                                 f"Verb '{verb['pl']}' has {len(verb['conj'])} conjugation forms, expected 6")

    def test_conjugation_forms_not_empty(self):
        for i, verb in enumerate(self.verbs):
            for j, form in enumerate(verb.get('conj', [])):
                with self.subTest(i=i, word=verb['pl'], person=j):
                    self.assertTrue(form.strip(),
                                    f"Verb '{verb['pl']}' has empty conjugation form at position {j}")

    def test_valid_cefr_level(self):
        for i, verb in enumerate(self.verbs):
            with self.subTest(i=i, word=verb['pl']):
                self.assertIn(verb['level'], VALID_CEFR)

    def test_infinitive_pattern(self):
        """Polish infinitives typically end in -ć or -c."""
        for i, verb in enumerate(self.verbs):
            word = verb['pl'].rstrip().split()[-1]  # handle "uczyć się" → "się"
            # For reflexive verbs, check the main verb part
            parts = verb['pl'].split()
            main = parts[0] if len(parts) > 1 and parts[-1] == 'się' else verb['pl']
            with self.subTest(i=i, word=verb['pl']):
                self.assertTrue(main.endswith('ć') or main.endswith('c'),
                                f"Verb '{verb['pl']}' main part '{main}' doesn't end in -ć/-c")

    def test_no_duplicate_verbs(self):
        pls = [v['pl'] for v in self.verbs]
        dupes = [w for w, c in Counter(pls).items() if c > 1]
        self.assertEqual(dupes, [], f"Duplicate verbs: {dupes}")


class TestAdjectiveFields(unittest.TestCase):
    """Test adjective entries have required fields and valid forms."""

    @classmethod
    def setUpClass(cls):
        with open(WORD_BANK_PATH, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)
        cls.adjectives = cls.data['adjectives']

    def test_required_fields(self):
        required = {'pl', 'en', 'level', 'forms'}
        for i, adj in enumerate(self.adjectives):
            with self.subTest(i=i, word=adj.get('pl', '?')):
                self.assertTrue(required.issubset(adj.keys()),
                                f"Adjective '{adj.get('pl','?')}' missing: {required - set(adj.keys())}")

    def test_forms_has_three_genders(self):
        """Each adjective must have exactly 3 forms: [masculine, feminine, neuter]."""
        for i, adj in enumerate(self.adjectives):
            with self.subTest(i=i, word=adj['pl']):
                self.assertIsInstance(adj['forms'], list)
                self.assertEqual(len(adj['forms']), 3,
                                 f"Adjective '{adj['pl']}' has {len(adj['forms'])} forms, expected 3 (m/f/n)")

    def test_masculine_form_matches_pl(self):
        """The first form (masculine) should match the 'pl' field."""
        for i, adj in enumerate(self.adjectives):
            with self.subTest(i=i, word=adj['pl']):
                self.assertEqual(adj['forms'][0], adj['pl'],
                                 f"Adjective masculine form '{adj['forms'][0]}' != pl field '{adj['pl']}'")

    def test_feminine_form_pattern(self):
        """Feminine adjective forms typically end in -a."""
        for i, adj in enumerate(self.adjectives):
            fem = adj['forms'][1]
            with self.subTest(i=i, word=adj['pl'], feminine=fem):
                self.assertTrue(fem.endswith('a'),
                                f"Feminine form '{fem}' of '{adj['pl']}' doesn't end in -a")

    def test_neuter_form_pattern(self):
        """Neuter adjective forms typically end in -e or -o."""
        for i, adj in enumerate(self.adjectives):
            neut = adj['forms'][2]
            with self.subTest(i=i, word=adj['pl'], neuter=neut):
                self.assertTrue(neut.endswith('e') or neut.endswith('o'),
                                f"Neuter form '{neut}' of '{adj['pl']}' doesn't end in -e/-o")

    def test_forms_not_empty(self):
        for i, adj in enumerate(self.adjectives):
            for j, form in enumerate(adj['forms']):
                with self.subTest(i=i, word=adj['pl'], form_idx=j):
                    self.assertTrue(form.strip(),
                                    f"Adjective '{adj['pl']}' has empty form at position {j}")

    def test_valid_cefr_level(self):
        for i, adj in enumerate(self.adjectives):
            with self.subTest(i=i, word=adj['pl']):
                self.assertIn(adj['level'], VALID_CEFR)

    def test_no_duplicate_adjectives(self):
        pls = [a['pl'] for a in self.adjectives]
        dupes = [w for w, c in Counter(pls).items() if c > 1]
        self.assertEqual(dupes, [], f"Duplicate adjectives: {dupes}")


class TestProfanity(unittest.TestCase):
    """Ensure no profanity appears in the word bank."""

    @classmethod
    def setUpClass(cls):
        with open(WORD_BANK_PATH, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)

    def _check_fields(self, entry, entry_type, idx):
        """Check all string fields in an entry for profanity."""
        for key, val in entry.items():
            if isinstance(val, str):
                words = val.lower().split()
                for w in words:
                    clean = w.strip('.,!?;:()[]"\'')
                    with self.subTest(type=entry_type, idx=idx, field=key, word=clean):
                        self.assertNotIn(clean, PROFANITY_PL,
                                         f"Polish profanity '{clean}' in {entry_type}[{idx}].{key}")
                        self.assertNotIn(clean, PROFANITY_EN,
                                         f"English profanity '{clean}' in {entry_type}[{idx}].{key}")
            elif isinstance(val, list):
                for item in val:
                    if isinstance(item, str):
                        clean = item.lower().strip('.,!?;:()[]"\'')
                        with self.subTest(type=entry_type, idx=idx, field=key):
                            self.assertNotIn(clean, PROFANITY_PL)
                            self.assertNotIn(clean, PROFANITY_EN)

    def test_nouns_no_profanity(self):
        for i, noun in enumerate(self.data['nouns']):
            self._check_fields(noun, 'noun', i)

    def test_verbs_no_profanity(self):
        for i, verb in enumerate(self.data['verbs']):
            self._check_fields(verb, 'verb', i)

    def test_adjectives_no_profanity(self):
        for i, adj in enumerate(self.data['adjectives']):
            self._check_fields(adj, 'adjective', i)

    def test_conversations_no_profanity(self):
        for conv in self.data.get('conversations', []):
            for j, line in enumerate(conv.get('lines', [])):
                for key in ('pl', 'en'):
                    words = line.get(key, '').lower().split()
                    for w in words:
                        clean = w.strip('.,!?;:()[]"\'')
                        with self.subTest(conv=conv['id'], line=j, field=key, word=clean):
                            self.assertNotIn(clean, PROFANITY_PL)
                            self.assertNotIn(clean, PROFANITY_EN)

    def test_examples_no_profanity(self):
        for wid, ex in self.data.get('examples', {}).items():
            for key in ('pl', 'en'):
                words = ex.get(key, '').lower().split()
                for w in words:
                    clean = w.strip('.,!?;:()[]"\'')
                    with self.subTest(id=wid, field=key, word=clean):
                        self.assertNotIn(clean, PROFANITY_PL)
                        self.assertNotIn(clean, PROFANITY_EN)


class TestConversations(unittest.TestCase):
    """Test conversation entries have valid structure."""

    @classmethod
    def setUpClass(cls):
        with open(WORD_BANK_PATH, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)
        cls.conversations = cls.data.get('conversations', [])

    def test_conversations_exist(self):
        self.assertGreater(len(self.conversations), 0, "No conversations found")

    def test_required_fields(self):
        required = {'id', 'title', 'scene', 'category', 'level', 'lines'}
        for conv in self.conversations:
            with self.subTest(conv=conv.get('id', '?')):
                self.assertTrue(required.issubset(conv.keys()),
                                f"Conv '{conv.get('id','?')}' missing: {required - set(conv.keys())}")

    def test_valid_cefr_level(self):
        for conv in self.conversations:
            with self.subTest(conv=conv['id']):
                self.assertIn(conv['level'], VALID_CEFR)

    def test_lines_not_empty(self):
        for conv in self.conversations:
            with self.subTest(conv=conv['id']):
                self.assertGreater(len(conv['lines']), 0)

    def test_line_fields(self):
        required = {'speaker', 'pl', 'en'}
        for conv in self.conversations:
            for j, line in enumerate(conv['lines']):
                with self.subTest(conv=conv['id'], line=j):
                    self.assertTrue(required.issubset(line.keys()))
                    self.assertIn(line['speaker'], VALID_SPEAKERS)
                    self.assertTrue(line['pl'].strip())
                    self.assertTrue(line['en'].strip())

    def test_has_your_lines(self):
        """Each conversation should have at least one 'you' line to practice."""
        for conv in self.conversations:
            your_lines = [l for l in conv['lines'] if l['speaker'] == 'you']
            with self.subTest(conv=conv['id']):
                self.assertGreater(len(your_lines), 0,
                                   f"Conv '{conv['id']}' has no 'you' lines")

    def test_no_duplicate_ids(self):
        ids = [c['id'] for c in self.conversations]
        dupes = [i for i, c in Counter(ids).items() if c > 1]
        self.assertEqual(dupes, [], f"Duplicate conversation IDs: {dupes}")


class TestExamples(unittest.TestCase):
    """Test example sentences have valid structure."""

    @classmethod
    def setUpClass(cls):
        with open(WORD_BANK_PATH, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)
        cls.examples = cls.data.get('examples', {})

    def test_examples_exist(self):
        self.assertGreater(len(self.examples), 0, "No examples found")

    def test_example_fields(self):
        for wid, ex in self.examples.items():
            with self.subTest(id=wid):
                self.assertIn('pl', ex, f"Example '{wid}' missing 'pl'")
                self.assertIn('en', ex, f"Example '{wid}' missing 'en'")
                self.assertTrue(ex['pl'].strip())
                self.assertTrue(ex['en'].strip())

    def test_example_ids_valid(self):
        """Example IDs should match pattern: n<num>, v<num>, or a<num>."""
        for wid in self.examples:
            with self.subTest(id=wid):
                self.assertRegex(wid, r'^[nva]\d+$',
                                 f"Example ID '{wid}' doesn't match expected pattern")

    def test_example_ids_reference_existing_words(self):
        """Example IDs should reference words that exist in the bank."""
        n_count = len(self.data['nouns'])
        v_count = len(self.data['verbs'])
        a_count = len(self.data['adjectives'])
        for wid in self.examples:
            prefix = wid[0]
            idx = int(wid[1:])
            with self.subTest(id=wid):
                if prefix == 'n':
                    self.assertLess(idx, n_count,
                                    f"Example '{wid}' references noun index {idx} but only {n_count} nouns exist")
                elif prefix == 'v':
                    self.assertLess(idx, v_count,
                                    f"Example '{wid}' references verb index {idx} but only {v_count} verbs exist")
                elif prefix == 'a':
                    self.assertLess(idx, a_count,
                                    f"Example '{wid}' references adj index {idx} but only {a_count} adjectives exist")


class TestCrossValidation(unittest.TestCase):
    """Cross-validate data across different sections."""

    @classmethod
    def setUpClass(cls):
        with open(WORD_BANK_PATH, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)

    def test_all_groups_have_members(self):
        """Every group referenced in nouns should have at least one member."""
        groups = set(n['group'] for n in self.data['nouns'])
        for group in groups:
            members = [n for n in self.data['nouns'] if n['group'] == group]
            with self.subTest(group=group):
                self.assertGreater(len(members), 0)

    def test_cefr_distribution(self):
        """Each word type should have words at multiple CEFR levels."""
        for wtype in ('nouns', 'verbs', 'adjectives'):
            levels = set(w['level'] for w in self.data[wtype])
            with self.subTest(type=wtype):
                self.assertGreaterEqual(len(levels), 2,
                                        f"{wtype} only has CEFR levels: {levels}")

    def test_nominative_plural_differs_from_singular(self):
        """Nominative plural should generally differ from the singular form."""
        same_count = 0
        for noun in self.data['nouns']:
            if noun['gender'] == 'pl':
                continue
            if noun['pl'] == noun['nom_pl']:
                same_count += 1
        # Allow a few exceptions (some borrowed words may not change)
        self.assertLess(same_count, len(self.data['nouns']) * 0.1,
                        f"{same_count} nouns have identical singular and plural nominative forms")


if __name__ == '__main__':
    unittest.main(verbosity=2)
