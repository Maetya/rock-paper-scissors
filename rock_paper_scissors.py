import sys
import random

winCount = 0
lossCount = 0
tieCount = 0
result = ""
availableChoices = ["r", "p", "s"]

# printHeader() prints a static header, the current score, and the available input choices.
def printHeader():
    print("ROCK, PAPER, SCISSORS")
    print(str(winCount) + " Wins, " + str(lossCount) + " Losses, " + str(tieCount) + " Ties")
    print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")

def returnScore():
    return str(winCount) + " Wins, " + str(lossCount) + " Losses, " + str(tieCount) + " Ties"

def getResult():
    return result

# The showdown() function compares the user's choice and computer's choice against if-conditions.
# Increments depending on whether the user wins, lose, or ties.
# The function prints the game outcome and returns the computer's choice.
# The user is able to exit the code by inputting "q".
def showdown(userChoice):
    global winCount
    global lossCount
    global tieCount
    global result

    computerChoice = availableChoices[random.randint(0, 2)]

    if userChoice == computerChoice:
        tieCount = tieCount + 1
        result = "It's a tie!"

    elif userChoice == "r":
        if computerChoice == "s":
            winCount = winCount + 1
            result = "You win!"

        if computerChoice == "p":
            lossCount = lossCount + 1
            result = "You lose!"

    elif userChoice == "p":
        if computerChoice == "s":
            lossCount = lossCount + 1
            result = "You lose!"

        if computerChoice == "r":
            winCount = winCount + 1
            result = "You win!"

    elif userChoice == "s":
        if computerChoice == "r":
            lossCount = lossCount + 1
            result = "You lose!"

        if computerChoice == "p":
            winCount = winCount + 1
            result = "You win!"

    elif userChoice == "q":
        sys.exit()

    return computerChoice