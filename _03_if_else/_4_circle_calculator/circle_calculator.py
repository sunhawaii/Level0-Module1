    # Write a Python program that asks the user for the radius of a circle.

    # Next, ask the user if they would like to calculate the area or circumference of a circle.

    # If they choose area, display the area of the circle using the radius.

    # Otherwise, display the circumference of the circle using the radius.

    #Area = πr^2
    #Circumference = 2πr

import tkinter

if __name__ == '__main__':
    window = tkinter.Tk()
    window.withdraw()

    radius = simpledialog.askstring(title='none', prompt=("What would you like the radius of your circle to be?")
    area_or_circumference = tkinter.simpledialog.askstring('title'='none', prompt=("Would you like to calculate area or circumference?")
    if area_or_circumference == "area":
        tkinter.messagebox.showinfo(title ='none'), ('message'):

    area= pi*radius^2
