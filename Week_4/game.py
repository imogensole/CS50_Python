# Imports random module
import random

while True:
    # Checks level input is an integer
    try:
        n = int(input("Level: "))
        # Checks level is positive
        if n > 0:
            break
        else:
            pass
    except ValueError:
        pass

# Randomly selects a target number
target = random.randint(0, n)

while True:
    try:
        # Prompts user to guess number
        guess = int(input("Guess: "))

        # Checks guess is in valid range
        if guess > n or guess < 0:
            pass

        # Prints indicator of guess
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            # Breaks if user guesses correctly 
            print("Just right!")
            break
    except ValueError:
        pass

