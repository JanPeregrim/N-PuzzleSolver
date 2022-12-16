import random
import tkinter.font
from tkinter import *
from Search_Algorithms import DFS


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
    button_greedy = Button(text="greedy")
    button_greedy = button_greedy.place(anchor="center", height=50, width=50, x=500, y=150)
    button_A = Button(text="A*")
    button_A = button_A.place(anchor="center", height=50, width=50, x=500, y=250)
    button_dfs = Button(text="DFS")
    button_dfs = button_dfs.place(anchor="center", height=50, width=50, x=500, y=350)

    # button_dfs.pack()
    # button_A.pack()
    # button_greedy.pack()


if __name__ == "__main__":
    global app
    top = Tk()
    top.title('N-Puzzle Solver')
    top.geometry("600x600")
    # creating a simple canvas.
    c = Canvas(top, bg="white", height="600", width="600")
    root = [1, 2, 3, 4, 5, 6, 7, 0, 8, 9 ,10,11,12,13,14,15]
    n = 4
    # root = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    # n = 3
    print_field(top, c, root, n)
    show_buttons()
    c.pack()
    top.mainloop()