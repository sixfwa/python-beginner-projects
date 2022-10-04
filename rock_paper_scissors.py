"""
Rock Paper Scissors
- Dictionaries
"""
import random

victories = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:
    computer_choice = random.choice(list(victories.keys()))
    user_choice = input("Enter Choice: [rock, paper, scissors]: ").lower()
    
    if user_choice not in victories.keys():
        continue
    
    print("Computer picked: ", computer_choice)
    
    if user_choice == computer_choice:
        print("You both picked", user_choice, "There is no winner!")
    elif user_choice == victories[computer_choice]:
        print(computer_choice, "beats", user_choice, "You lose!")
    elif computer_choice == victories[user_choice]:
        print(user_choice, "beats", computer_choice, "You win!")
        
    play_again = input("Play again: [y/n]: ")
    
    if play_again == "n":
        break