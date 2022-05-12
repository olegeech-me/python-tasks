"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
"""

import string


def is_pangram(s):
    return all(True if w in s.lower() else False for w in string.ascii_lowercase)


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("This is not a pangram"))
