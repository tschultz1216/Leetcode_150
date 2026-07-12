"""
408. Valid Word Abbreviation
----
A string can be abbreviated by replacing any number of non-adjacent,
non-empty substrings with their lengths. The lengths must not have
leading zeros.

Given a string word and an abbreviation abbr, return whether abbr
is a valid abbreviation of word.

Rules:
  - A digit sequence in abbr represents the count of characters to skip
    in word.
  - Leading zeros in a digit sequence are invalid  (e.g. "s010n" → invalid).
  - Digits must account for non-empty substrings   (e.g. "s0ub" → invalid).

Approach — two-pointer walk:
  i → index into word
  j → index into abbr

  At each step:
    • abbr[j] is a digit:
        - if it is '0', return False (leading zero)
        - parse the full number, advance i by that amount
    • abbr[j] is a letter:
        - if word[i] != abbr[j], return False
        - advance both i and j by 1

  After the loop: valid iff both pointers reached the end simultaneously.

  Examples:
    word = "substitution"
    "s10n"      → True   (s + 10 chars + n)
    "sub4u4"    → True
    "s55n"      → False  (adjacent replacements: 5+5=10 ≠ separate groups)
    "s010n"     → False  (leading zero)
    "s0ubstitution" → False (zero-length replacement)

"""

import re


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        numbers = re.findall(r'\d+',abbr)
        numSum = 0
        for number in numbers:
            print(number[0])
            if number[0] == '0':
                return False
            numSum += int(number)
        abbr_sub_list = re.split(r'\d+', abbr)
        for abbr_sub in abbr_sub_list:
            if not abbr_sub in word:
                return False
        abbr_cut = re.sub(r'\d+', '', abbr)
        checkSum = numSum + len(abbr_cut)
        return checkSum == len(word)


if __name__ == "__main__":
    solution = Solution()

    tests: list[tuple[str, str, bool]] = [
        # (word,           abbr,              expected)
        ("internationalization", "i12iz4n",   True),
        ("apple",          "a3e",             True),
        ("substitution",   "s10n",            True),
        ("substitution",   "sub4u4",          True),
        ("substitution",   "12",              True),
        ("substitution",   "substitution",    True),
        ("substitution",   "s55n",            False),  # adjacent replacements
        ("substitution",   "s010n",           False),  # leading zero
        ("substitution",   "s0ubstitution",   False),  # zero-length replacement
        ("a",              "2",               False),  # number exceeds word length
        ("hi",             "hi1",             False),  # abbr longer than word
    ]

    for word, abbr, expected in tests:
        result = solution.validWordAbbreviation(word, abbr)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected} | word={word!r} abbr={abbr!r}")
