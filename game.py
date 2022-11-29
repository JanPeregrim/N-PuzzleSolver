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
    Start_index=20;
    End_index=120;
    center_Value=((End_index-Start_index)/2)+20;

    for i in range(0,size):
        for j in range(0,size):
            c.create_rectangle(Start_index+X_index, Start_index+Y_index, End_index+X_index, End_index+Y_index,outline="black", fill="white", width=2)
            c.create_text(center_Value+X_index, center_Value+Y_index, text=field[i][j], font=tkinter.font.Font(size=25,family='Helvetica'))
            X_index+=100
        X_index = 0;
        Y_index += 100

    c.pack()
    top.mainloop()
