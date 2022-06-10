import turtle
from tkinter import messagebox, simpledialog, Tk


# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # Make a new turtle
    turt = turtle.Turtle()
    turt.shape('turtle')
    turt.speed(0)
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring('none', "What shape do you want to draw?(triangle/square/circle)")
    # Draw the shape requested by the user using if-elif-else statements
    # print(shape)
    if shape == "triangle":
        turt.color('red')
        turt.pencolor('black')
        turt.fillcolor('red')
        turt.fillcolor('red')
        turt.begin_fill()
        turt.goto
        for i in range(3):
            turt.forward(100)
            turt.left(120)
        turt.end_fill


    elif shape == "circle":
        turt.color('red')
        turt.pencolor('black')
        turt.fillcolor('red')
        turt.fillcolor('red')
        turt.begin_fill()
        turt.circle(57, steps=30)
        turt.end_fill
    else:
        turt.color('red')
        turt.pencolor('black')
        turt.fillcolor('red')
        turt.fillcolor('red')
        turt.begin_fill()
        for x in range(4):
            turt.forward(100)
            turt.left(90)
            turt.end_fill
    # Call the turtle .done() method
turtle.done()