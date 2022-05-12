#!/usr/bin/env python3.6

import random

total_guess = 0

print("Welcome to the guessing game! Plz use ctr+c for prompting exit.")
while True:
    try:
        number = random.randint(1,9)
        while 1:
            guess = input("Plz input number ")
            try:
                guess = int(guess)
                break
            except ValueError:
                print ("You're dumb as fuck, we need numbers BLYAT'!")
        total_guess += 1
        if guess > number:
            print("That's too high")
        elif guess < number:
            print("That's too low")
        else:
            print("And you are winning the AVTOMOBIIIIIL' !!!!!")
    except KeyboardInterrupt:
        if input("Do you wanna try more? ").lower() != "yes":
            break

print(f"Total guesses taken: {total_guess}")
