"""guessing number game"""
import random


def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number guessing game!")

    while True:
        user_input = input("Guess the number between 1 - 100  >> ")
        try:
            guessed_number = int(user_input)
        except ValueError:
            print("invalid input, please enter a whole number!")
            continue

        attempts += 1

        if guessed_number < 1 or guessed_number >100:
            print("Out of range, pick a number between 1-100")
        elif guessed_number < number_to_guess:
            print("Too low, Try again!")
        elif guessed_number > number_to_guess:
            print("Too high, Try again!")
        else: 
            print(f"Congratulations! you guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()

