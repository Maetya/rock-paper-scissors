from tkinter import *
from rock_paper_scissors import *

font_type="Open Sans"

def displayStaticLayout():
    rockButton = Button(window, image=img_rock, command=lambda: displayPressedButton("r"), relief="solid")
    rockButton.grid(row=2, column=0, padx=10)

    scissorsButton = Button(window, image=img_scissors, command=lambda: displayPressedButton("s"), relief="solid")
    scissorsButton.grid(row=2, column=1, padx=10)

    paperButton = Button(window, image=img_paper, command=lambda: displayPressedButton("p"), relief="solid")
    paperButton.grid(row=2, column=2, padx=10)

    chooseOneTextBox = Label(text="Select an icon", fg="black", bg='#ffffff', font=(font_type, 25))
    chooseOneTextBox.grid(row=1, column=1, pady=10)

    placeHolder = Label(text="", bg='#ffffff', font=(font_type, 25))
    placeHolder.grid(row=4, column=2)

    spacer1 = Label(text="", bg='#ffffff')
    spacer1.grid(row=3, column=0, pady=50)

    youTextBox = Label(text="You", bg='#ffffff', font=(font_type, 15))
    youTextBox.grid(row=5, column=0)

    computerTextBox = Label(text="Computer", bg='#ffffff', font=(font_type, 15))
    computerTextBox.grid(row=5, column=2)


def displayPressedButton(userChoice):
    computerChoice = showdown(userChoice)

    if userChoice == "r":
        Label(window, image=img_rock, bg="white").grid(row=6, column=0, pady=0)

    elif userChoice == "p":
        Label(window, image=img_paper, bg="white").grid(row=6, column=0, pady=0)

    elif userChoice == "s":
        Label(window, image=img_scissors, bg="white").grid(row=6, column=0, pady=0)

    if computerChoice == "r":
        Label(window, image=img_rock, bg="white").grid(row=6, column=2, pady=0)

    elif computerChoice == "p":
        Label(window, image=img_paper, bg="white").grid(row=6, column=2, pady=0)

    elif computerChoice == "s":
        Label(window, image=img_scissors, bg="white").grid(row=6, column=2, pady=0)


    clearPreviousTextBox = Label(text="               ", bg='#ffffff', font=(font_type, 25))
    clearPreviousTextBox.grid(row=4, column=1)

    # TODO Could possibly create a function for resultLayout() or layoutResult().
    if getResult() == "It's a tie!":
        resultTextBox = Label(text=getResult(), bg='#ffffff', font=(font_type, 25), foreground="black")
        resultTextBox.grid(row=4, column=1)
    elif getResult() == "You win!":
        resultTextBox = Label(text=getResult(), bg='#ffffff', font=(font_type, 25), foreground="green")
        resultTextBox.grid(row=4, column=1)
    elif getResult() == "You lose!":
        resultTextBox = Label(text=getResult(), bg='#ffffff', font=(font_type, 25), foreground="red")
        resultTextBox.grid(row=4, column=1)
    else:
        resultTextBox = Label(text=getResult(), bg='#ffffff', font=(font_type, 25))
        resultTextBox.grid(row=4, column=1)

    verseTextBox = Label(text="VS", bg='#ffffff', font=(font_type, 40))
    verseTextBox.grid(row=6, column=1)

    scoreTextBox = Label(text=returnScore(),bg='#ffffff', font=(font_type, 12))
    scoreTextBox.grid(row=7, column=1, pady=10)

# Initializes a window with the specified dimensions, title, background colour and disables the minimize/maximize button.
window = Tk()
window.geometry("515x590")
window.title("Rock Paper and Scissors")
window['background'] = '#ffffff'
window.resizable(0, 0)

# Imports the rock, scissors, and paper icons.
img_rock = PhotoImage(file="images/rock.png")
img_scissors = PhotoImage(file="images/scissors.png")
img_paper = PhotoImage(file="images/paper.png")

displayStaticLayout()
window.mainloop()