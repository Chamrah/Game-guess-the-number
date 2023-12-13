# Library that do the creation of graphical interfaces
from tkinter import *
# This library implements pseudo-random number generators for different distributions.
import random

secret = random.randint(1, 100)

# Method that check the number that the user entered and the real number that must be guessed
def check_guess():
    guess = int(number.get())
    if guess == secret:
        result_label.config(text="Congratulations, you are the winner!")
    elif guess < secret:
        result_label.config(text="Larger number!")
    else:
        result_label.config(text="Smaller number!")

# Display the window
window = Tk()
window.title("Guess the number ")

Label(window, text="Guess a number between 1 and 100").pack()
number = Entry(window)
number.pack()

Button(window, text="Check !", command=check_guess).pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()
