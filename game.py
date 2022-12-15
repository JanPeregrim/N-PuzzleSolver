import random
import tkinter.font
from tkinter import *

def create_random_playground(size):
    random_numbers = random.sample(range(0, size*size), size*size)

    #### Field for testing ######
    #field = [[1, 2, 3, 4,] ,[5, 6, 7, 8] , [13, 9, 12, 15] , [0, 11, 10, 14]]

    field = []
    numbers = []
    for i in random_numbers:
        numbers.append(i)
        if len(numbers) == size:
            field.append(numbers)
            numbers = []


    print(field)
    #test pre vyriesenie hry
    print(solved_game(field, size))
    print_field(field,size)
    print_status(field,size)


    #osetrenie ak by sa vytvorilo uz vyriesene pole
    if solved_game(field, size) == True:
        create_random_playground(size)

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

def solved_game(field, size):

    state = False

    control_index = 0

    for i in range(0,size):
        for j in range(0,size):
            if field[i][j] != control_index:
                return state
            control_index = control_index + 1
    state = True
    return state

def getInvCount(field,size):
    arr1 = []
    for y in field:
        for x in y:
            arr1.append(x)

    field = arr1
    inv_count = 0
    for i in range(size * size - 1):
        for j in range(i + 1, size * size):
            if (field[j] and field[i] and field[i] > field[j]):
                inv_count += 1

    return inv_count


# find Position of blank from bottom
def findXPosition(field,size):
    # start from bottom-right corner of matrix
    for i in range(size - 1, -1, -1):
        for j in range(size - 1, -1, -1):
            if (field[i][j] == 0):
                return size - i


# This function returns true if given
# instance of N*N - 1 puzzle is solvable

def isSolvable(field, size):
    # Count inversions in given puzzle
    invCount = getInvCount(field, size)
    # If grid is odd, return true if inversion
    # count is even.
    if (size & 1):
        return ~(invCount & 1)

    else:  # grid is even
        pos = findXPosition(field, size)
        if (pos & 1):
            return ~(invCount & 1)
        else:
            return invCount & 1

def print_status(field,size):
    if isSolvable(field,size):
        print("Solvable")
        return 1
    else:
        print("Not Solvable")
        return 0