"""
Define a function that takes in two non-negative integers a and b and returns the last
decimal digit of a**b. Note that a and b may be very large!

You may assume that the input will always be valid.

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6

# Theory behind:
https://brilliant.org/wiki/finding-the-last-digit-of-a-power/
"""


def last_digit(number, power):
    patterns = {
        "0": [0],
        "1": [1],
        "2": [2, 4, 8, 6],
        "3": [3, 9, 7, 1],
        "4": [4, 6],
        "5": [5],
        "6": [6],
        "7": [7, 9, 3, 1],
        "8": [8, 4, 2, 6],
        "9": [9, 1],
    }
    if power == 0:
        return 1
    p = patterns[str(number)[-1]]
    return 0 if p == 0 else p[power % len(p) - 1]


# SHOULD BE SOLVED EASIER WITH !!! power(number, power, 10) !!!


print(last_digit(4, 2) == 6)
print(last_digit(9, 7) == 9)
print(last_digit(10, 10**10) == 0)
print(last_digit(2**200, 2**300) == 6)
