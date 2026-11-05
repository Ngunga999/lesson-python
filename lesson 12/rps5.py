import sys
import random
from enum import Enum

game_count = 0


def play_rps():

 class RPS(Enum):
  ROCK = 1
PAPER = 2
SCISSORS = 3

 

playerchoice = input("\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")

if playerchoice not in ["1", "2", "3"]:
 print("You must enter 1,2, or 3.")
 

player = int(playerchoice)



computerchoice = random.choice("123")

computer = int(computerchoice)


print("\nYou chose " + playerchoice + " . ")
print("Python chose " + computerchoice + " . \n")

def decide_winner (player, computer):
 if player == 1 and computer== 3: 
  print("🥳You win!")

 elif player == 2 and computer== 1: 
  print("You win")
 elif player == 3 and computer== 2: 
  print("🥳You win!")
 elif player == computer: 
  print(" 😮Tie game!")
 else:
  print("🐍python wins!")

game_result = decide_winner (player, computer)

print(game_result)
global game_count
game_count += 1

print("\nGame count:" + str
(game_count))

  
playagain = input("\nplay again?  \nY for yes or \nQ to Quit \n\n")

if playagain.lower() == "y":
 playagain = True
else:
 print("\n🥳🥳🥳🥳🥳🥳")
print("Thanks for playing 🥳!")
playagain = False


sys.exit("BYE!🤷")

play_rps()

