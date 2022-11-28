import random
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
    print_field(field)

def print_field(field):

    top = Tk()
    top.geometry("500x500")
    # creating a simple canvas.
    c = Canvas(top, bg="black", height="500", width=500)

    c.pack()
    top.mainloop()
