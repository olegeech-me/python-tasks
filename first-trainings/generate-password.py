#!/usr/bin/env python3

import random
import string

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

def get_input():
    while 1:
        strongness = input("how strong the password should be? ")
        try:
            strongness = int(strongness)
            break
        except ValueError as err:
            print("Please don't be stupid, enter a number")
            continue
    return strongness

# method 1:

print("".join(random.sample(s, get_input())))

# method 2:

print("".join(random.choice(
    string.ascii_letters + string.punctuation + string.digits) for _ in range(get_input()))
    )
