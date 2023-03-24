import time 
import numpy as np

grid  = [
[0, 6, 0, 0, 8, 0, 4, 2, 0],
[0, 1, 5, 0, 6, 0, 3, 7, 8],
[0, 0, 0, 4, 0, 0, 0, 6, 0],
[1, 0, 0, 6, 0, 4, 8, 3, 0],
[3, 0, 6, 0, 1, 0, 7, 0, 5],
[0, 8, 0, 3, 5, 0, 0, 0, 0],
[8, 3, 0, 9, 4, 0, 0, 0, 0],
[0, 7, 2, 1, 3, 0, 9, 0, 0],
[0, 0, 9, 0, 2, 0, 6, 1, 0]]   

#determine if number can be placed there
def possible(y,x,n):
    global grid
    for i in range(9):
        #check row for matching n
        if grid[y][i] == n:
            return False      
    for i in range(9):
        #check column for matching n    
        if grid[i][x] == n:
            return False
        #check all numbers in that tridrant
        x0 = (x//3)*3 #6
        y0 = (y//3)*3 #6     
    for i in range (y0,y0+3):
        for j in range (x0,x0+3):
            if grid[i][j] == n:
                return False
    return True

    
#given x and y value determine 
def solve():
    global grid
    #scan through every row and column for every number
    for y in range(9):
        for x in range(9):
            # if it is empty
            if grid[y][x] == 0: 
                #check each number from 1 to 9
                for n in range(1,10):
                    if possible(y,x,n) == True:
                        grid[y][x] = n
                        solve()
                        #reset that block if solve does not work
                        grid[y][x] = 0
                return         
    
    print(np.matrix(grid))
    
solve()
