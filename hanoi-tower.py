m = int(input('Enter the number of discs : '))
count = 0 # counts the number of steps taken to solve the Tower of Hanoi

def move(initial, final) :
    """ indicates the movement of the discs from column 'initial' to column 'final'"""
    print("Move disc from column {} to column {}".format(initial, final))

def Tower_of_Hanoi(n, initial, use, final) :
    """ solves the Hanoi tower,
    'initial' : starting column, 
    'final' : final/target column, 
    'use' : the column using which we move the discs from initial to final """
    global count
    if n == 0 :
        pass
    else :
        Tower_of_Hanoi(n-1, initial, final, use)
        move(initial, final)
        count += 1
        Tower_of_Hanoi(n-1, use, initial, final)

Tower_of_Hanoi(m, 'A', 'B', 'C')
print("Number of steps taken is {}".format(count))