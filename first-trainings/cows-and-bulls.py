#!/usr/bin/env python3

import random
import string

SIZE = 4


def get_input():
    while 1:
        guess = input(f"Enter a {SIZE}-digit number: ")
        if len(guess) < 4 or len(guess) > 4:
            print(f"Plz input 4, not {len(guess)}!")
            continue
        else:
            break
    return guess


def generate():
    return "".join(random.sample(string.digits, SIZE))


def cows_bulls(guess, guessed):
    cows, bulls = (0, 0)
    for i in range(len(guessed)):
        if guess[i] == guessed[i]:
            cows += 1
        else:
            if guess[i] in guessed[::]:
                bulls += 1
    return (cows, bulls)


def main():
    print("Welcome to the Cows and Bulls Game!")
    while True:
        results = cows_bulls(get_input(), generate())
        if results[0] == 4:
            print("You guessed the number correctly!")
            break
        else:
            print(f"{results[0]} cows, {results[1]} bulls")
            continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program ...")
