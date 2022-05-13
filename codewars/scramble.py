"""
Complete the function scramble(str1, str2) that returns true if a portion of
str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

"""

import string
import random
from timeit import timeit


def scramble(s1, s2):
    # took: 3.9438712999999552
    # res = all(map(lambda c: True if c in s1 else False, s2))
    #
    # took: 0.6843278000014834
    # res = all([True if c in s1 else False for c in s2])
    # return res
    #
    # took: 4.54010499996366
    # letters = {"s1": {}, "s2": {}}
    # for s in s1:
    #    letters["s1"][s] = letters["s1"].get(s, 0) + 1
    # for s in s2:
    #    letters["s2"][s] = letters["s2"].get(s, 0) + 1
    #
    # took: 2.7974427999579348
    # s1_letters = {}
    # s2_letters = {}
    # for s in s1:
    #    s1_letters[s] = s1_letters.get(s, 0) + 1
    # for s in s2:
    #    s2_letters[s] = s2_letters.get(s, 0) + 1

    # took: 0.40642799995839596
    # s1_letters = {s: s1.count(s) for s in set(s1)}
    # s2_letters = {s: s2.count(s) for s in set(s2)}
    # return all(True if s2_letters[s] <= s1_letters.get(s, 0) else False for s in s2_letters.keys())

    # took: 0.28807280003093183
    # s1_letters = {s: s1.count(s) for s in string.ascii_lowercase}
    # s2_letters = {s: s2.count(s) for s in string.ascii_lowercase}
    # return all(True if s2_letters[s] <= s1_letters.get(s, 0) else False for s in s2_letters.keys())

    # FROM CODEWARS, took: 0.07772900001145899
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


print(scramble("rkqodlw", "world"))
print(scramble("':';123cedewaraaossoqqyt", "codewars"))
print(scramble("katas", "steak"))
# performance
N = 6000000
str1 = "".join(random.choices(string.ascii_lowercase, k=N))
str2 = "".join(random.choices(string.ascii_lowercase, k=N))
print(timeit("scramble(str1, str2)", number=1, globals=globals()))
