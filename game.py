import random
import tkinter.font
from tkinter import *



def create_random_playground(size):
    #random numbers
    random_numbers = random.sample(range(0, size*size), size*size)
    field = []
    numbers = []
    for i in random_numbers:
        numbers.append(i)
        if len(numbers) == size:
            field.append(numbers)
            numbers = []

    print(field)
    print_field(field,size)

def print_field(field,size):

    top = Tk()
    top.geometry("500x500")
    # creating a simple canvas.
    c = Canvas(top, bg="white", height="500", width=500)

    X_index=0
    Y_index=0
    print()
    for i in range(0,size):
        Y_index+=100
        for j in range(0,size):
            c.create_rectangle(20+X_index, 20+Y_index, 120+X_index, 120+Y_index,outline="black", fill="white", width=2)
            c.create_text(70+X_index, 70+Y_index, text=field[i][j], font=tkinter.font.Font(size=25,family='Helvetica'))
            X_index+=100
        X_index = 0;

    c.pack()
    top.mainloop()
