"""A single-player number guessing game."""

import random


def main():
    secret_number = random.randint(1, 100)

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while True:
        guess_text = input("Enter your guess: ")

        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a whole number between 1 and 100.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess > secret_number:
            print("Your guess is too high. Guess again.")
        elif guess < secret_number:
            print("Your guess is too low. Guess again.")
        else:
            print("Congratulations! You guessed the number correctly!")
            break


if __name__ == "__main__":
    main()
