from Search_Algorithms import DFS, Greedy, AStar_search

import tkinter.font
from tkinter import *
from gui import print_field

#initial state
n = 4
# n=int(input("Enter n\n"))
print("Enter your" ,n,"*",n, "puzzle")
# root = []
# for i in range(0,n*n):
#     p = int(input())
#     root.append(p)

#test
#root=[1, 2, 3, 4, 5, 6, 7, 0, 8]
root = [1, 2, 3, 7, 4, 5, 6, 11, 8, 9, 10, 15, 12, 13, 14, 0]  # test
root = [1, 2, 3, 7, 4, 5, 10, 6, 8, 9, 0, 11, 12, 13, 14, 15]
print("The given state is:", root)

#test gui
# top = Tk()
# top.geometry("500x500")
# # creating a simple canvas.
# c = Canvas(top, bg="white", height="500", width=500)
# print_field(top,c, root, size)
# c.pack()
# top.mainloop()

#count the number of inversions       
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
    return False #ZAMENIL SOM


#1,8,2,0,4,3,7,6,5 is solvable
#2,1,3,4,5,6,7,8,0 is not solvable

from time import time

if solvable(root):
    print("Solvable, please wait. \n")

    time2 = time()
    DFS_solution = DFS(root, n)
    DFS_time = time() - time2
    print('DFS Solution is ', DFS_solution[0])
    print('Number of explored nodes is ', DFS_solution[1])
    print('DFS Time:', DFS_time, "\n")
    
    time3 = time()
    Greedy_solution = Greedy(root, n)
    Greedy_time = time() - time3
    print('Greedy Solution is ', Greedy_solution[0])
    print('Number of explored nodes is ', Greedy_solution[1])
    print('Greedy Time:', Greedy_time , "\n")
    
    time4 = time()
    AStar_solution = AStar_search(root, n)
    AStar_time = time() - time4
    print('A* Solution is ', AStar_solution[0])
    print('Number of explored nodes is ', AStar_solution[1])   
    print('A* Time:', AStar_time)
    
    
else:
    print("Not solvable")



     