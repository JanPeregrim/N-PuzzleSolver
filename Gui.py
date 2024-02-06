import random
import tkinter.font
from time import time, sleep
from tkinter import *

import numpy as np

from Search_Algorithms import DFS,Greedy,AStar_search

def print_field(top, c, field,size):

    #pretoze premazuje pole a vypisuje ho nanovo aj tlacidla
    c.delete("all")
    c.create_text(300, 20, text="N - Puzzle Solver ", font=tkinter.font.Font(size=25, family='Helvetica'))
    gen_buttons(c, top, field, size)

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
            if field[n] == 0:
                c.create_rectangle(Start_index + X_index, Start_index + Y_index, End_index + X_index,
                                   End_index + Y_index, outline="black", fill="gray", width=2)
            n = n + 1
            X_index+=100
        X_index = 0;
        Y_index += 100

    return field, size

def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv

def solvable(puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
    inv_counter = inv_num(puzzle)
    if (inv_counter %2 ==0):
        return True
    return False

#vytvoril som vlastnu funkciu pre kontrolu pretoze sa mi zdalo ze tamta nefungovala spravne https://stackoverflow.com/questions/34570344/check-if-15-puzzle-is-solvable
def if_solvable(puzzle, n):
    parity = 0
    gridWidth = n
    row = 0
    blankRow = 0

    for i in range(len(puzzle)):
        if (i % gridWidth == 0):
            row = row + 1
        if (puzzle[i] == 0) :
            blankRow = row
            continue
        for j in range(i+1 , len(puzzle)):
            if ((puzzle[i] > puzzle[j]) and puzzle[j] != 0):
                parity = parity + 1

    if (gridWidth % 2 == 0):
        if(blankRow % 2 == 0):
            return parity % 2 != 0
        else:
            return parity % 2 == 0
    else:
        return parity % 2 == 0
def field_4(event):
    global root
    global size
    size = 4
    root = generate_random_puzzle(size)
    #root = [1, 2, 3, 7, 4, 5, 6, 11, 8, 9, 10, 15, 12, 13, 14, 0]  # test
    print(if_solvable(root, size)) #kontrola do konzoly
    # while solvable(root) == False:
    #     root = generate_random_puzzle(size)
    while if_solvable(root, size) == False:
        root = generate_random_puzzle(size)
    print(if_solvable(root, size))  #kontrola do konzoly
    alg_buttons(root, size, c)
def field_3(event):
    global root
    global size
    size = 3
    root = generate_random_puzzle(size)
    #root = [1, 0, 2, 7, 5, 4, 8, 6, 3]
    print(if_solvable(root, size)) # kontrola do konzoly
    # while solvable(root) == False:
    #     root = generate_random_puzzle(size)
    while if_solvable(root, size) == False:
        root = generate_random_puzzle(size)
    print(if_solvable(root, size))  # kontrola do konzoly
    alg_buttons(root, size, c)

def gen_buttons(c, top, root, size):

    button_generate_4 = Button(text="GENERATE RANDOM 4x4")
    button_generate_4.place(anchor="center", height=75, width=150, x=500, y=150)
    button_generate_4.bind("<Button-1>", field_4)


    button_generate_3 = Button(top, text="GENERATE RANDOM 3x3")
    button_generate_3.place(anchor="center", height=75, width=150, x=500, y=250)
    button_generate_3.bind("<Button-1>", field_3)

def greedy(event):
    global root
    global size
    global c
    global top
    # root = [13, 8, 9, 4, 7, 2, 15, 6, 14, 1, 11, 10, 3, 0, 5, 12] #test
    # vypis do konzoly
    print(root)
    print(size)
    c.create_text(150, 550, text="SOLVING BY GREEDY", font=tkinter.font.Font(size=12, family='Helvetica'))
    time3 = time()
    Greedy_solution = Greedy(root, size)
    Greedy_time = time() - time3
    # vypis do konzoly
    print('Greedy Solution is ', Greedy_solution[0])
    print('Number of explored nodes is ', Greedy_solution[1])
    print('Greedy Time:', Greedy_time , "\n")
    move_button(root, Greedy_solution[0], c, top)
    c.create_text(72, 100, text="Node explored: ", font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(145, 100, text=Greedy_solution[1], font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(40, 75, text="Time: ", font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(150, 75, text=Greedy_time, font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(350, 550, text="SOLVED BY GREEDY", font=tkinter.font.Font(size=12, family='Helvetica'))

def dfs_event(event):

    global root
    global size
    global c
    global top
    #c.create_text(150, 550, text="SOLVING BY DFS", font=tkinter.font.Font(size=12, family='Helvetica')) #nefunguje neviem preco chcel som vypisat ze ked stlacis tak aby pisalo ze riesi
    print(root)
    print(size)
    time2 = time()
    DFS_solution = DFS(root, size)
    DFS_time = time() - time2
    # vypis do konzoly
    print('DFS Solution is ', DFS_solution[0])
    print('Number of explored nodes is ', DFS_solution[1])
    print('DFS Time:', DFS_time, "\n")
    if (DFS_solution[2] == 0):
        move_button(root, DFS_solution[0], c, top)
        c.create_text(350, 550, text="SOLVED BY DFS", font=tkinter.font.Font(size=12, family='Helvetica'))
    else:
        print_field(top, c, root, size)
        c.create_text(350, 550, text="NO SOLVED BY DFS", font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(72, 100, text="Node explored: ", font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(145, 100, text=DFS_solution[1], font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(40, 75, text="Time: ", font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(150, 75, text=DFS_time, font=tkinter.font.Font(size=12, family='Helvetica'))

def Astar_event(event):
    global root
    global size
    global c
    global top
    # test
    #root = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    # size = 3

    # root = [1, 2, 3, 7, 4, 5, 6, 11, 8, 9, 10, 15, 12, 13, 14, 0] #test

    print(root)
    print(size)
    c.create_text(150, 75, text="SOLVING BY A*", font=tkinter.font.Font(size=12, family='Helvetica'))
    time4 = time()
    AStar_solution = AStar_search(root, size)
    AStar_time = time() - time4
    # vypisovanie hodnot do canvasu
    # funkcia na automaticke riesenie na pohyb matice
    move_button(root, AStar_solution[0], c, top)
    c.create_text(72, 100, text="Node explored: ", font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(145, 100, text=AStar_solution[1], font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(40, 75, text="Time: ", font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(150, 75, text=AStar_time, font=tkinter.font.Font(size=12, family='Helvetica'))
    c.create_text(350, 550, text="SOLVED BY A*", font=tkinter.font.Font(size=12, family='Helvetica'))

def alg_buttons(root,size,c):

    button_greedy = Button(text="greedy")
    button_greedy.place(anchor="center", height=50, width=50, x=500, y=400)
    button_greedy.bind("<ButtonPress>",greedy)

    button_A = Button(text="A*")
    button_A.place(anchor="center", height=50, width=50, x=500, y=450)
    button_A.bind("<Button-1>", Astar_event)

    button_dfs = Button(text="DFS")
    button_dfs.place(anchor="center", height=50, width=50, x=500, y=500)
    button_dfs.bind("<ButtonPress>",dfs_event)

#funkcia pridana pre uspanie tkinter https://stackoverflow.com/questions/10393886/tkinter-and-time-sleep
def tksleep(self, time:float) -> None:
    """
    Emulating `time.sleep(seconds)`
    Created by TheLizzard, inspired by Thingamabobs
    """
    self.after(int(time*1000), self.quit)
    self.mainloop()

tkinter.Misc.tksleep = tksleep # Monkey patching
def move_button(root,solution,c, top):

    #check the size of list
    size_of_list = len(root)
    size=0
    if size_of_list < 10:
        size = 3
    else:
        size = 4

    #transforming list to matrix
    matrix = root
    shape = (size, size)
    matrix = np.array(root)
    matrix = matrix.reshape(shape)
    print(matrix)
    solution_size = len(solution)

    #move in the matrix

    for i in range(0,solution_size):
        if solution[i] == "Up":
            position = find_zero(matrix,size)
            pos_x = position[0]
            pos_y = position[1]
            Value = matrix[pos_x-1][pos_y]
            matrix[pos_x - 1][pos_y] = 0
            matrix[pos_x][pos_y] = Value

        if solution[i] == "Down":
            position = find_zero(matrix,size)
            pos_x = position[0]
            pos_y = position[1]
            Value = matrix[pos_x+1][pos_y]
            matrix[pos_x + 1][pos_y] = 0
            matrix[pos_x][pos_y] = Value

        if solution[i] == "Right":
            position = find_zero(matrix,size)
            pos_x = position[0]
            pos_y = position[1]
            Value = matrix[pos_x][pos_y+1]
            matrix[pos_x][pos_y+1] = 0
            matrix[pos_x][pos_y] = Value

        if solution[i] == "Left":
            position = find_zero(matrix,size)
            pos_x = position[0]
            pos_y = position[1]
            Value = matrix[pos_x][pos_y-1]
            matrix[pos_x][pos_y-1] = 0
            matrix[pos_x][pos_y] = Value

        #Namiesto print do konzoly uz len vypisovanie do kanvasu cez tlacidlo alebo automaticky
        #print(matrix)
        solution_array = matrix_to_array(matrix,size)
        print(solution_array)
        print_field(top, c , solution_array, size)
        text_solve = c.create_text(150, 550, text="SOLVING", font=tkinter.font.Font(size=12, family='Helvetica'))
        top.tksleep(0.1)
    #pripadne butony na pohyb dopredu a spat
    #som dojebany nacisto, pojebany python
    # button_forward = Button(text="-->")
    # button_forward.place(anchor="center", height=50, width=50, x=350, y=550)
    #
    # button_back = Button(text="<--")
    # button_back.place(anchor="center", height=50, width=50, x=150, y=550)

    c.delete(text_solve)
def matrix_to_array(matrix,size):
    array = []
    for i in range(0,size):
        for j in range(0,size):
            array.append(matrix[i][j])
    return array
def find_zero(matrix,size):
    pos_y=0
    pos_x=0

    for i in range(0,size):
        for j in range(0, size):
            if matrix[i][j] == 0:
                pos_y = i
                pos_x = j
                return pos_y, pos_x

def generate_random_puzzle(size):
    random_numbers = random.sample(range(0, size*size), size*size)
    root = random_numbers
    print_field(top, c, root, size)
    print(root)
    return root



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
    global top
    global root

    top = Tk()
    top.title('N-Puzzle Solver')
    top.geometry("600x600")

    # creating a simple canvas.
    c = Canvas(top, bg="white", height="600", width="600")
    c.create_text(300, 20, text="N - Puzzle Solver ", font=tkinter.font.Font(size=25, family='Helvetica'))

    root = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    size = 3

    print_empty_field()
    gen_buttons(c, top, root, size)

    c.pack()
    top.mainloop()