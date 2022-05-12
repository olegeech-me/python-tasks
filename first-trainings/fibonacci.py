#!/usr/bin/env python3.6


def get_input():
    """Get user input"""
    while 1:
        answer = input("Plz input how many Fibonacci numbers " "would you like to see ")
        try:
            answer = int(answer)
            return answer
        except ValueError:
            print("Don't be a stupid mf, use numbers only")
            continue


def fibonacci(limit):
    """Generate Fibonacci sequence"""
    sequence = []
    for i in range(limit):
        if i == 0 or i == 1:
            sequence.append(i)
        else:
            sequence.append(sequence[i - 2] + sequence[i - 1])
    return sequence


def main():
    limit = get_input()
    print(fibonacci(limit))


if __name__ == "__main__":
    main()
