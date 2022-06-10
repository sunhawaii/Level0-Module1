import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window=Tk()
    window.withdraw()



    number1=simpledialog.askstring(title='none', prompt="What is the first number you want to add?")
    number2 = simpledialog.askstring(title='none', prompt="What is the second number you want to add?")

    sum = number2+number1

    messagebox.showinfo(title='none', message="Your answer for the sum of the two numbers is " + str(sum) + ".")


"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""