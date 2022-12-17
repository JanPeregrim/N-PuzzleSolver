import random
import tkinter.font
from time import time
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

def gen_buttons(c):
    #B = Button(top, text="DFS", command=DFS(root, size))

    button_generate_4 = Button(text="GENERATE RANDOM 4x4")
    button_generate_4.place(anchor="center", height=75, width=150, x=500, y=150)
    if button_generate_4.bind("<ButtonPress>"):
        size = 4
        root = generate_random_puzzle(size)
        alg_buttons(root, size)

    button_generate_3 = Button(text="GENERATE RANDOM 3x3")
    button_generate_3.place(anchor="center", height=75, width=150, x=500, y=250)
    if True:
    # if button_generate_3.bind("<ButtonPress>"):
        size = 3
        root = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        # root = generate_random_puzzle(size)
        alg_buttons(root, size, c)

def alg_buttons(root,size,c):

    button_greedy = Button(text="greedy")
    button_greedy.place(anchor="center", height=50, width=50, x=500, y=400)
    button_greedy.bind("<ButtonPress>",Greedy(root,size))

    button_A = Button(text="A*")
    button_A.place(anchor="center", height=50, width=50, x=500, y=450)
    # if button_A.bind("<ButtonPress>"):
    if True: ##Len aby som videl vysledok ci funguje
        time4 = time()
        AStar_solution = AStar_search(root,size)
        AStar_time = time() - time4
        c.create_text(72,100,text="Node explored: ",font=tkinter.font.Font(size=12,family='Helvetica'))
        c.create_text(145,100,text=AStar_solution[1],font=tkinter.font.Font(size=12,family='Helvetica'))
        c.create_text(40,75,text="Time: ",font=tkinter.font.Font(size=12,family='Helvetica'))
        c.create_text(150,75,text=AStar_time,font=tkinter.font.Font(size=12,family='Helvetica'))

    button_dfs = Button(text="DFS")
    button_dfs.place(anchor="center", height=50, width=50, x=500, y=500)
    # button_dfs.bind("<ButtonPress>",DFS(root,size))

    button_forward = Button(text="-->")
    button_forward.place(anchor="center", height=50, width=50, x=350, y=550)

    button_forward = Button(text="<--")
    button_forward.place(anchor="center", height=50, width=50, x=150, y=550)


def generate_random_puzzle(size):
    random_numbers = random.sample(range(0, size*size), size*size)
    print_field(top, c, random_numbers, size)
    print(random_numbers)
    return random_numbers


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
    c.create_text(300, 20, text="N - Puzzle Solver ", font=tkinter.font.Font(size=25, family='Helvetica'))

    root = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    # n = 3

    print_empty_field()
    gen_buttons(c)

    c.pack()
    top.mainloop()