import sys
import random

def printHeader():
    print("ROCK, PAPER, SCISSORS")
    print(str(winCount) + " Wins, " + str(lossCount) + " Losses, " + str(tieCount) + " Ties")
    print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")


availableChoices = ["rock", "paper", "scissors"]

winCount = 0
lossCount = 0
tieCount = 0

while True:

    printHeader()
    userChoice = input().lower()

    computerChoice = availableChoices[random.randint(0, 2)]
    print(computerChoice)


    if userChoice == computerChoice:
        print("It's a tie!")
        tieCount = tieCount + 1

    elif userChoice == "rock":
        if computerChoice == "scissors":
            winCount = winCount + 1
            print("You win!")

        if computerChoice == "paper":
            lossCount = lossCount + 1
            print("You lose!")


    elif userChoice == "paper":
        if computerChoice == "scissors":
            lossCount = lossCount + 1
            print("You lose!")

        if computerChoice == "rock":
            winCount = winCount + 1
            print("You win!")

    elif userChoice == "scissors":
        if computerChoice == "rock":
            lossCount = lossCount + 1
            print("You lose!")

        if computerChoice == "paper":
            winCount = winCount + 1
            print("You win!")



