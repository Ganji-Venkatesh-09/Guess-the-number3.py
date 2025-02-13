import random

# Define range of numbers
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while True:
    guess = input("Enter your guess: ")

    # Check if input is a number
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        # Check if number is within range
        if guess < lowest_num or guess > highest_num:
            print(f"That number is out of range! Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low! Try Again!")
        elif guess > answer:
            print("Too High! Try Again!")
        else:
            print(f"Correct! The answer was {answer}.")
            print(f"Number of guesses: {guesses}")
            break  # End the game when guessed correctly
    else:
        print(f"Invalid guess! Please enter a number between {lowest_num} and {highest_num}")



