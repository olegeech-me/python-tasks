"""
Define a function that takes an integer argument and returns a logical
value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater
than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given
negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the
most trivial solutions might time out. Numbers go up to 2^31 ( or similar,
depending on language ). Looping all the way up to n, or n/2, will be too slow.

Wilson's theorem states that a natural number p > 1 is a prime number if and only if
(p - 1) ! ≡  -1   mod p
OR  (p - 1) ! ≡  (p-1) mod p

In other words, any number n is a prime number if, and only if,
(n - 1)! + 1 is divisible by n
"""


from math import sqrt


def is_prime(num):
    # too slow:
    # return False if num <= 1 else (math.factorial(num - 1) + 1) % num == 0
    if num <= 1:
        return False
    print(num)
    for i in range(2, int(sqrt(num)) + 1):
        print(f"i={i}, sqrt(num) + 1 ={int(sqrt(num)) + 1}")
        if num % i == 0:
            return False
    return True


print(is_prime(1))
print(is_prime(3))
print(is_prime(5))
print(is_prime(7))
print(is_prime(11))
print(is_prime(13))
print(is_prime(-13))
print(is_prime(-1))
print(is_prime(pow(5, 31)))
