import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    score=0

    riddle1 = simpledialog.askstring(title='Riddle_1', prompt="What goes up but never comes down?")
    riddle2 = simpledialog.askstring(title='Riddle_2', prompt="I have lakes with no water, mountains with no stone, and cities with no buildings. What am I?")
    riddle3 = simpledialog.askstring(title='Riddle_3', prompt="What has to be broken before you use it?")

    if riddle1 == "Age":
        score+1
    else:
        score+0

    if riddle2 == "A map":
        score+1
    else:
        score+0
    if riddle3 == "A egg":
        score+1
    else:
        score+0


messagebox.showinfo(title='none', message= "You got "+str(score)+" out of 3 riddles correct!")
"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""