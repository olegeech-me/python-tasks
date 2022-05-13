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
    # 3.9438712999999552
    # res = all(map(lambda c: True if c in s1 else False, s2))
    #
    # 0.4057126999996399
    res = all([True if c in s1 else False for c in s2])
    print(res)


scramble("rkqodlw", "world")
scramble("':';123cedewaraaossoqqyt", "codewars")
scramble("katas", "steak")

# performance
N = 6000000
str1 = "".join(random.choices(string.ascii_lowercase, k=N))
str2 = "".join(random.choices(string.ascii_lowercase, k=N))
print(timeit("scramble(str1, str2)", number=1, globals=globals()))
