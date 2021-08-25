import random
from replit import clear

logo = '''
 o-o                       o-O-o o            o   o            o            o
o                            |   |            |\  |            |            |
|  -o o  o o-o o-o o-o       |   O--o o-o     | \ | o  o o-O-o O-o  o-o o-o o
o   | |  | |-'  \   \        |   |  | |-'     |  \| |  | | | | |  | |-' |
 o-o  o--o o-o o-o o-o       o   o  o o-o     o   o o--o o o o o-o  o-o o   O
'''

def guess_answer(real_answer):
  guess = int(input("Make a guess:"))
  if guess < real_answer:
    print("Too low. \nGuess Again.")
  elif guess > real_answer:
    print("Too High.\nGuess Again.")
  else:
    print(f"You got it! The answer was {real_answer}")
    return True

def play_game():
  clear()
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")

  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  attempts = 0
  answer = random.randint(1,100)
  print(answer)
  if difficulty == 'easy':
    attempts = 10
  elif difficulty == 'hard':
    attempts = 5
  else:
    print("I don't understand your input. Please try again.")

  while attempts>0:
    print(f"You have {attempts} attempts remaining to guess the answer.")
    if guess_answer(answer):
      attempts = 0
    else:
      attempts -=1



play_game()
