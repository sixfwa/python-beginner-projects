"""
Guess the number game
- user input
- import libraries
- while loop
- if statements
"""
import random

print("Welcome to the random number guessing game!")
print("You will have to guess a number between 0 and 100.")
print("You will have 5 lives!")

computer_choice = random.randint(0, 100)

user_lives = 1

while user_lives != 0:
    guess = int(input("Enter your guess: "))
    
    # If the user inputs the correct number
    if guess == computer_choice:
        print("Congratulations", guess, "is correct!")
        break
    # If the user guess is less than the computers choice
    elif guess < computer_choice:
        print("Go higher")
    # if the user guess if greater than the computers choice
    elif guess > computer_choice:
        print("Go lower")
    
    user_lives -= 1
    
if user_lives == 0:
    print("You have run out of lives. The answer was: ", computer_choice)