import json
from rules import CONSONANTS, VOWELS, MATRAS

class Transliterator:
    def __init__(self, special_cases_file="special_cases.json"):
        # Load special cases from JSON
        with open(special_cases_file, "r", encoding="utf-8") as f:
            self.special_cases = json.load(f)

        self.consonants = CONSONANTS
        self.vowels = VOWELS
        self.matras = MATRAS

    def transliterate_word(self, word):
        word_lower = word.lower()

        # Step 1: Check special cases
        if word_lower in self.special_cases:
            return self.special_cases[word_lower]

        # Step 2: Rule-based transliteration
        result = ""
        i = 0
        while i < len(word):
            matched = False
            for length in range(3, 0, -1):  # Check 3,2,1-letter sequences
                if i + length <= len(word):
                    chunk = word[i:i+length].lower()

                    # Consonant + vowel
                    if chunk in self.consonants:
                        next_vowel = ""
                        j = i + length
                        for vl in range(2, 0, -1):  # Look ahead for vowel
                            if j + vl <= len(word):
                                vchunk = word[j:j+vl].lower()
                                if vchunk in self.matras:
                                    next_vowel = self.matras[vchunk]
                                    j += vl
                                    break
                        result += self.consonants[chunk] + next_vowel
                        i = j
                        matched = True
                        break

                    # Standalone vowel
                    elif chunk in self.vowels:
                        result += self.vowels[chunk]
                        i += length
                        matched = True
                        break

            if not matched:
                result += word[i]
                i += 1

        return result

    def transliterate(self, text):
        words = text.split()
        return " ".join([self.transliterate_word(w) for w in words])
