import sys
import random

winCount = 0
lossCount = 0
tieCount = 0
result = "dasd"


availableChoices = ["r", "p", "s"]

def printHeader():
    print("ROCK, PAPER, SCISSORS")
    print(str(winCount) + " Wins, " + str(lossCount) + " Losses, " + str(tieCount) + " Ties")
    print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")

def returnScore():
    return (str(winCount) + " Wins, " + str(lossCount) + " Losses, " + str(tieCount) + " Ties")

def returnResult():
    return result

def showdown(userChoice):
    global winCount
    global lossCount
    global tieCount
    global computerChoice
    global result

    printHeader()
    computerChoice = availableChoices[random.randint(0, 2)]

    if userChoice == "r":
        print("ROCK versus...")
        if computerChoice == "s":
            winCount = winCount + 1
            print("SCISSORS")
            result = "You win!"
            print(result)


        if computerChoice == "p":
            lossCount = lossCount + 1
            print("PAPER")
            result = "You lose!"
            print(result)

        if computerChoice == "r":
            tieCount = tieCount + 1
            print("ROCK")
            result = "It's a tie!"
            print(result)

    elif userChoice == "p":
        print("PAPER versus...")
        if computerChoice == "s":
            lossCount = lossCount + 1
            print("SCISSORS")
            result = "You lose!"
            print(result)

        if computerChoice == "r":
            winCount = winCount + 1
            print("ROCK")
            result = "You win!"
            print(result)

        if computerChoice == "p":
            tieCount = tieCount + 1
            print("PAPER")
            result = "It's a tie!"
            print(result)

    elif userChoice == "s":
        if computerChoice == "r":
            lossCount = lossCount + 1
            print("ROCK")
            result = "You lose!"
            print(result)

        if computerChoice == "p":
            winCount = winCount + 1
            print("PAPER")
            result = "You win!"
            print(result)



        if computerChoice == "s":
            tieCount = tieCount + 1
            print("s")
            result = "It's a tie!"
            print(result)

    elif userChoice == "q":
        sys.exit()


    print(" ")

    return computerChoice