import random

print("Number Guessing Game")
print("I am thinking of a number between 1 and 100.")

# Step 1: Generate random number
number = random.randint(1, 100)

# Step 2: Initialize attempts
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break