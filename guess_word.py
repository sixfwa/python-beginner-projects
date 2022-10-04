"""
Guess the word
- functions
- strings
"""
import random

words = ["apple", "breakfast", "banana", "vehicle"]

def choose_word():
    return random.choice(words)

def create_blank_word(word):
    blank_word = []
    
    for letter in word:
        blank_word.append("_")
        
    return blank_word

def display_progress_word(blank_word):
    print(' '.join(blank_word))
    
def check_letter(letter, blank_word, word):
    for i in range(len(word)):
        if word[i] == letter:
            blank_word[i] = letter
    return blank_word

def game():
    print("Welcome to Guess the word!\n")
    computer_word = choose_word()
    blank_word = create_blank_word(computer_word)
    lives = 6
    
    while computer_word != "".join(blank_word) and lives != 0:
        display_progress_word(blank_word)
        print(f"\nYou have {lives} lives left!")
        user_guess = input("\nGuess a letter: ")
        blank_word = check_letter(user_guess, blank_word, computer_word)
        if user_guess not in blank_word:
            print(f"The letter {user_guess} is not in the word.")
            lives -= 1

    if lives == 0:
        print("\nYou have run out of lives!")
    else:
        print("\nCongratulations! you got the correct word!")

game()