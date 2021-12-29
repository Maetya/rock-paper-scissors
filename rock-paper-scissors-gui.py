from tkinter import *

window = Tk()
window.title("Rock Paper and Scissors")
#
img_rock = PhotoImage(file="images/rock.png")
img_scissors = PhotoImage(file="images/scissors.png")
img_paper = PhotoImage(file="images/paper.png")
Label(window, image=img_rock, bg="white").grid(row=2, column=0, sticky=E)
Label(window, image=img_scissors, bg="white").grid(row=2, column=1, sticky=E)
Label(window, image=img_paper, bg="white").grid(row=2, column=2, sticky=E)
window.mainloop()
