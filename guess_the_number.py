print('''
                               | | | |                                   | |                
  __ _ _   _  ___  ___ ___     | |_| |__   ___      _ __  _   _ _ __ ___ | |__   ___ _ __   
 / _` | | | |/ _ \/ __/ __|    | __| '_ \ / _ \    | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|  
| (_| | |_| |  __/\__ \__ \    | |_| | | |  __/    | | | | |_| | | | | | | |_) |  __/ |     
 \__, |\__,_|\___||___/___/     \__|_| |_|\___|    |_| |_|\__,_|_| |_| |_|_.__/ \___|_|     
  __/ |                                                                                     
 |___/                                                                                      ''')

from random import randint
easy_level_turns=10
hard_level_turns=5

def set_difficuilty():
  level=input("enter the level of difficuilty 'easy','hard': \n").lower()
  if level == "easy":
    return easy_level_turns
  elif level=="hard":
    return hard_level_turns
turns = 0
def check_answer(guess,answer,turns):
  if guess>answer:
    print(f"guessed number {guess} is too high")
    return turns-1
  elif guess<answer:
    print(f"guessed number {guess} is too low")
    return turns-1
  elif guess==answer:
    print(f"you got it , answer is {answer}")
  else:
    print("number is out of range between 1-100")

def game():
  print("welcome to the number guessing game ")
  print("i am thinking a number between 1-100")
  
  answer= randint(1,100)
  turns=set_difficuilty()
  guess=0
  while guess !=answer:
    print(f"you have {turns} number of turns left")
    guess=int(input("make a guess : "))
    turns=check_answer(guess,answer,turns)
    if turns==0:
      print("you move out of the turns 'you loose' ")
      return
game()
