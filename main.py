#The main purpose of this program is for the program to function  a game of Tic-Tac-Toe between an user and a bot
#used https://stackoverflow.com/questions/57372530/python-function-for-changing-text-size-in-python-shell 

import random
import time
import sys

Letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * - + = ~ ? : ; < >"
RobotCharacterChoice = Letters.split(" ")
RobotCharacter = random.choice(RobotCharacterChoice)
Character = " "
#This list represents the Tic-Tac-Toe game board
TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
RobotSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Choose = True

#this function contained in lines 20-24 was written with help from stackoverflow (linked above)
#This functon is used to print all the print statements in a delayed manner for a more user friendly environment
#this function starts here
def delay_print(s): 
  for c in s:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.03)
#this function ends here, everything else was original

#This function is used to find out who is the winner of the game
def CheckWinnerTrue():
  global TicTacToeBoard
  global RobotCharacter
  global Character
  global RobotSpots
  if RobotCharacter == checkWinner(TicTacToeBoard):
    Character = " "
    TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    RobotSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    RobotCharacter = random.choice(RobotCharacterChoice)
    return "V"
  elif Character == checkWinner(TicTacToeBoard):
    Character = " "
    TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    RobotSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    RobotCharacter = random.choice(RobotCharacterChoice)
    return "F"

#This function is used to check if 3 seperate strings are equal to each other
def allSame(str1, str2, str3):
  return str1==str2==str3 and str1!="-"

#This function returns the winner's game character which is then used in the CheckWinnerTrue() function to find out the winner of the game
def checkWinner(TicTacToeBoard):
  if(allSame(TicTacToeBoard[0],TicTacToeBoard[1],TicTacToeBoard[2])):
    return TicTacToeBoard[0]
  elif(allSame(TicTacToeBoard[3],TicTacToeBoard[4],TicTacToeBoard[5])):
    return TicTacToeBoard[3]
  elif(allSame(TicTacToeBoard[6],TicTacToeBoard[7],TicTacToeBoard[8])):
    return TicTacToeBoard[6]
  elif(allSame(TicTacToeBoard[0],TicTacToeBoard[3],TicTacToeBoard[6])):
    return TicTacToeBoard[0]
  elif(allSame(TicTacToeBoard[1],TicTacToeBoard[4],TicTacToeBoard[7])):
    return TicTacToeBoard[1]
  elif(allSame(TicTacToeBoard[2],TicTacToeBoard[5],TicTacToeBoard[8])):
    return TicTacToeBoard[2]
  elif(allSame(TicTacToeBoard[0],TicTacToeBoard[4],TicTacToeBoard[8])):
    return TicTacToeBoard[0]
  elif(allSame(TicTacToeBoard[2],TicTacToeBoard[4],TicTacToeBoard[6])):
    return TicTacToeBoard[2]
  else:
    return False

#This function is called whenever there is a change made in the game board (when a player plays their turn) to check if the game is over
def GameOver(TicTacToeBoard):
  if(allSame(TicTacToeBoard[0],TicTacToeBoard[1],TicTacToeBoard[2])):
    return True
  elif(allSame(TicTacToeBoard[3],TicTacToeBoard[4],TicTacToeBoard[5])):
    return True
  elif(allSame(TicTacToeBoard[6],TicTacToeBoard[7],TicTacToeBoard[8])):
    return True
  elif(allSame(TicTacToeBoard[0],TicTacToeBoard[3],TicTacToeBoard[6])):
    return True
  elif(allSame(TicTacToeBoard[1],TicTacToeBoard[4],TicTacToeBoard[7])):
    return True
  elif(allSame(TicTacToeBoard[2],TicTacToeBoard[5],TicTacToeBoard[8])):
    return True
  elif(allSame(TicTacToeBoard[0],TicTacToeBoard[4],TicTacToeBoard[8])):
    return True
  elif(allSame(TicTacToeBoard[2],TicTacToeBoard[4],TicTacToeBoard[6])):
    return True
  else:
    return False

#This function prints the list(TicTacToeBoard) into a 3x3 Tic-Tac-Toe square board
def PrintTicTacToe(TicTacToeBoard):
  BoardFormatted = ""
  for i in range(9):
    if i%3 == 0 and i>0:
      BoardFormatted += "\n---------------------------------\n|   " + TicTacToeBoard[i] + "   |   "
    else:
      BoardFormatted += "|   "  + TicTacToeBoard[i] + "   |   "
  return(BoardFormatted + "")

  
#This function replaces an empty spot in the game board with the user's game character using the user's chosen spot number
def ChangeSpot(Spot, Character):
  CorrectSpot = int(Spot) - 1
  global TicTacToeBoard
  TicTacToeBoard[CorrectSpot] = Character

#This function replaces an empty spot in the game board with the bot's game character using the bot's randomly chosen spot number
def RobotTurn(CharacterRobot):
  global TicTacToeBoard
  global RobotSpots
  SpotChoice = random.choice(RobotSpots)
  RobotSpots.remove(SpotChoice)
  TicTacToeBoard[SpotChoice-1] = CharacterRobot

#This function checks if there is a tie in the game
def TieChecker(TicTacToeBoard):
  if TicTacToeBoard[0]!="-" and TicTacToeBoard[1]!="-" and TicTacToeBoard[2]!="-" and TicTacToeBoard[3]!="-" and TicTacToeBoard[4]!="-" and TicTacToeBoard[5]!="-" and TicTacToeBoard[6]!="-" and TicTacToeBoard[7]!="-" and TicTacToeBoard[8]!="-" and not GameOver(TicTacToeBoard):
    return True
  else:
    return False

#This is the main function which contains all the different functions from above and puts it together so that the whole program works as intended (A game of Tic-Tac-Toe between an user and a bot)
def Game():
  global RobotCharacter
  global Character
  global TicTacToeBoard
  global RobotSpots
  global Choose
  if Choose:
    delay_print("Starting Tic-Tac-Toe...")
    Character = input("\nPlease enter your character: ")
    delay_print("The bot chose " + RobotCharacter)
    Choose = False
  if not GameOver(TicTacToeBoard):
    while True:
      SpotNumber = input("\nPlease enter a spot number: ")
      if int(SpotNumber) not in RobotSpots:
        delay_print("Hmm... Seems like that spot has occupied or is invalid!")
        time.sleep(1)
        delay_print("\nPlease enter a new spot...")
      else:
        break
  RobotSpots.remove(int(SpotNumber))
  ChangeSpot(SpotNumber, Character)
  BoardChangedPrinted = PrintTicTacToe(TicTacToeBoard)
  delay_print("Current Board --> \n")
  print(BoardChangedPrinted)
  if GameOver(TicTacToeBoard):
    if CheckWinnerTrue() == "F":
      time.sleep(1)
      delay_print("There is a winner...\nCalculating...\nPlease stand by...")
      time.sleep(1)
      delay_print("\nYou won! The bot lost!\n\nWe're starting a new game!\n")
      Choose = True
      return
  if TieChecker(TicTacToeBoard):
    time.sleep(1)
    delay_print("The game board is full...\nCalculating...\nPlease stand by...")
    time.sleep(1)
    delay_print("\nIt's a tie!\n\nWe're starting a new game!\n")
    Character = " "
    TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    RobotSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    RobotCharacter = random.choice(RobotCharacterChoice)
    Choose = True
    return
  if not GameOver(TicTacToeBoard):
    RobotTurn(RobotCharacter)
    time.sleep(1)
    delay_print("The bot is thinking...\n")
    time.sleep(1)
    BoardChangedPrinted = PrintTicTacToe(TicTacToeBoard)
    delay_print("Current Board --> \n")
    print(BoardChangedPrinted)
  if GameOver(TicTacToeBoard):
    if CheckWinnerTrue() == "V":
      time.sleep(1)
      delay_print("There is a winner...\nCalculating...\nPlease stand by...")
      time.sleep(1)
      delay_print("\nYou lost! The bot won!\n\nWe're starting a new game!\n")
      Choose = True
      return

#This while loop constantly calls the Game() function
while True:
  Game()