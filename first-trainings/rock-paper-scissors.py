#!/usr/bin/env python3

game = {"rock": 1, "paper": 2, "scissors": 3}

while True:
    results = []
    for i in range(2):
        answer = input("Type your choice: ")
        while answer not in game.keys():
            answer = input("Wrong input! Plz choose from rock, paper, or scissors: ")
        results.append(game.get(answer))

    diff = results[0] - results[1]
    if diff in [-2, 1]:
        print(f"First player wins, second loses! ({results[0]} vs {results[1]})")
    elif diff in [-1, 2]:
        print(f"First player loses, second wins! ({results[0]} vs {results[1]})")
    else:
        print("It's a draw! ({results[0]} vs {results[1]})")
        continue

    if input("Do you wanna have another game?").lower() == "yes":
        continue
    else:
        break


