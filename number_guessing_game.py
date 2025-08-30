# Number Guessing Game
# How to Play:
# The computer randomly chooses a number between 1 and 100.
# You (the player) must guess the number.
# After each guess, the game will tell you if your guess is "Too High" or "Too Low".
# The game ends when you guess correctly, and it will display the number of attempts taken.

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too Low! Try again.")
            elif guess > number_to_guess:
                print("Too High! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
