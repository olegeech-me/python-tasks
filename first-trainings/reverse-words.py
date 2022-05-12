#!/usr/bin/env python3

def get_input():
    """Get user input"""
    while 1:
        answer = input("Please gimme a phase with some words ")
        return answer

def reverse_phrase(phrase):
    """Reverse words in the phrase"""
    words = phrase.split()
    return " ".join(words[-1::-1])

def main():
    phrase = get_input()
    print(reverse_phrase(phrase))

if __name__ == "__main__":
    main()

