import sys
import random

def printHeader():
    print("ROCK, PAPER, SCISSORS")
    print(str(winCount) + " Wins, " + str(lossCount) + " Losses, " + str(tieCount) + " Ties")
    print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")



availableChoices = ["r", "p", "s"]

winCount = 0
lossCount = 0
tieCount = 0

while True:
    printHeader()
    userChoice = input().lower()
    computerChoice = availableChoices[random.randint(0, 2)]

    if userChoice == "r":
        print("ROCK versus...")
        if computerChoice == "s":
            winCount = winCount + 1
            print("SCISSORS")
            print("You win!")

        if computerChoice == "p":
            lossCount = lossCount + 1
            print("PAPER")
            print("You lose!")

        if computerChoice == "r":
            tieCount = tieCount + 1
            print("ROCK")
            print("It's a tie!")


    elif userChoice == "p":
        print("PAPER versus...")
        if computerChoice == "s":
            lossCount = lossCount + 1
            print("SCISSORS")
            print("You lose!")

        if computerChoice == "r":
            winCount = winCount + 1
            print("ROCK")
            print("You win!")

        if computerChoice == "p":
            tieCount = tieCount + 1
            print("PAPER")
            print("It's a tie!")

    elif userChoice == "s":
        if computerChoice == "r":
            lossCount = lossCount + 1
            print("ROCK")
            print("You lose!")

        if computerChoice == "p":
            winCount = winCount + 1
            print("PAPER")
            print("You win!")

        if computerChoice == "s":
            tieCount = tieCount + 1
            print("s")
            print("It's a tie!")

    elif userChoice == "q":
        sys.exit()

    print("")