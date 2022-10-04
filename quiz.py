"""
Quiz game
- Reading from a file
- JSON library
"""
import json
import random

print("Welcome to the quiz game!\n")

with open("questions.json") as json_file:
    questions = json.load(json_file)
    
score = 0

while len(questions) != 0:
    question = random.choice(list(questions.keys()))
    answer = input(f"\n{question} ")
    if answer == questions[question]:
        score += 1
    del questions[question]

print(f"\nYour score is: {score}!")