import random
import tkinter.font
from tkinter import *
from Search_Algorithms import DFS,Greedy,AStar_search

def print_field(top, c, field,size):

    X_index=0
    Y_index=100
    Start_index=20;
    End_index=120;
    center_Value=((End_index-Start_index)/2)+20;
    n = 0

    for i in range(0,size):
        for j in range(0,size):
            c.create_rectangle(Start_index+X_index, Start_index+Y_index, End_index+X_index, End_index+Y_index,outline="black", fill="white", width=2)
            c.create_text(center_Value+X_index, center_Value+Y_index, text=field[n], font=tkinter.font.Font(size=25,family='Helvetica'))
            n = n + 1
            X_index+=100
        X_index = 0;
        Y_index += 100

def show_buttons():
    #B = Button(top, text="DFS", command=DFS(root, size))

    button_generate_4 = Button(text="GENERATE RANDOM 4x4")
    button_generate_4.place(anchor="center", height=75, width=150, x=500, y=150)
    button_generate_4.bind("<ButtonPress>", generate_random_puzzle(4))

    button_generate_3 = Button(text="GENERATE RANDOM 3x3")
    button_generate_3.place(anchor="center", height=75, width=150, x=500, y=250)
    button_generate_3.bind("<ButtonPress>", generate_random_puzzle(3))


    button_greedy = Button(text="greedy")
    button_greedy = button_greedy.place(anchor="center", height=50, width=50, x=500, y=400)
    # button_greedy.bind("<ButtonPress>")

    button_A = Button(text="A*")
    button_A = button_A.place(anchor="center", height=50, width=50, x=500, y=450)

    button_dfs = Button(text="DFS")
    button_dfs = button_dfs.place(anchor="center", height=50, width=50, x=500, y=500)

    button_forward = Button(text="-->")
    button_forward.place(anchor="center", height=50, width=50, x=350, y=550)

    button_forward = Button(text="<--")
    button_forward.place(anchor="center", height=50, width=50, x=150, y=550)


    # button_dfs.pack()
    # button_A.pack()
    # button_greedy.pack()
def generate_random_puzzle(size):
    random_numbers = random.sample(range(0, size*size), size*size)
    print_field(top, c, random_numbers, size)
    print(random_numbers)

def print_empty_field():

    X_index=0
    Y_index=100
    Start_index=20;
    End_index=120;
    n = 0

    for i in range(0,3):
        for j in range(0,3):
            c.create_rectangle(Start_index+X_index, Start_index+Y_index, End_index+X_index, End_index+Y_index,outline="black", fill="gray", width=2)
            n = n + 1
            X_index+=100
        X_index = 0;
        Y_index += 100


if __name__ == "__main__":
    global app
    top = Tk()
    top.title('N-Puzzle Solver')
    top.geometry("600x600")
    # creating a simple canvas.
    c = Canvas(top, bg="white", height="600", width="600")
    root = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    # n = 3

    print_empty_field()
    show_buttons()

    c.pack()
    top.mainloop()