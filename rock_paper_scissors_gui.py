from tkinter import *
from rock_paper_scissors import *

def displayPressedButton(userChoice):
    computerChoice = showdown(userChoice)

    if userChoice == "r":
        Label(window, image=img_rock, bg="white").grid(row=5, column=0, pady=5, sticky=E)

    elif userChoice == "p":
        Label(window, image=img_paper, bg="white").grid(row=5, column=0, pady=5, sticky=E)

    elif userChoice == "s":
        Label(window, image=img_scissors, bg="white").grid(row=5, column=0, pady=5, sticky=E)

    if computerChoice == "r":
        Label(window, image=img_rock, bg="white").grid(row=5, column=2, pady=5, sticky=E)

    elif computerChoice == "p":
        Label(window, image=img_paper, bg="white").grid(row=5, column=2, pady=5, sticky=E)

    elif computerChoice == "s":
        Label(window, image=img_scissors, bg="white").grid(row=5, column=2, pady=5, sticky=E)

    verseTextBox = Label(text="VS")
    verseTextBox.grid(row=5, column=1)

window = Tk()
window.geometry("388x500")
window.title("Rock Paper and Scissors")

img_rock = PhotoImage(file="images/rock.png")
img_scissors = PhotoImage(file="images/scissors.png")
img_paper = PhotoImage(file="images/paper.png")


chooseOneTextBox = Label(text="Select an icon")
chooseOneTextBox.grid(row=1, column=1)

spacer1 = Label(window, text="")
spacer1.grid(row=3, column=0, pady=40)

rockButton = Button(window, image=img_rock,command= lambda: displayPressedButton("r"), borderwidth=0)
rockButton.grid(row=2, column=0, sticky=E)

scissorsButton = Button(window, image=img_scissors, command= lambda: displayPressedButton("s"), borderwidth=0)
scissorsButton.grid(row=2, column=1)

paperButton = Button(window, image=img_paper, command= lambda: displayPressedButton("p"), borderwidth=0)
paperButton.grid(row=2, column=2)

youTextBox = Label(text = "You:")
youTextBox.grid(row=4, column=0)

computerTextBox = Label(text = "Computer: " )
computerTextBox.grid(row=4, column=2)


window.mainloop()