#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def set_difficulty():
  difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
  if difficulty_level == "easy":
    return 10
  else:
    return 5

def check_answer(guess, answer, turns):    
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1 
  else:
    print(f"You got it! The answer was {answer}. 💜")

def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!!!")
  print("I'm thinking of a number between 1 and 100") 
  answer = random.randint(1, 100)
  print("The answer-", answer)
  
  turns = set_difficulty()
  guess = 0
  
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)

    if turns == 0:
      print("You've run out of guesses, you lose. 😭")
      return
    elif guess != answer:
      print("Guess again!")
      
wanna_play = input("Do you want to try your hand at the Number Guessing Game? Type 'y' or 'n': ").lower()
if wanna_play == 'y':
  play_game()
else:
  print("Goodbye!")
