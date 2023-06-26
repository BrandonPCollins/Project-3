# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#X = placing ship and hit battleship

#' ' for available space

#'-' for missed shot 

#For random int
from random import randint 

#For the Ships 
HIDDEN_BOARD = [[' '] * 8 for x in range (8)] 

#For Guessing
GUESS_BOARD = [[' '] * 8 for x in range (8)] 

#Convert guess letter string to int 
letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

#Function for the creation of the board 
def print_board(board):
    print(' A B C D E F G H')
    print(' - - - - - - - - ')
    row_number = 1
    for row in board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1
    print(' - - - - - - - - ')


#Places ships on the board on game start 
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7) 
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'


#Do a try and except on these later to prevent crashing!!! 

#Player Enters a location to hit a ship 
def get_ship_location():
        row = input('Please enter a ship row numbered 1-8:\n')
        while row not in '12345678':
            print('Please enter a valid row') 
            row = input('Please enter a ship row numbered 1-8:\n')
        column = input('Please enter a ship column A-H:\n').upper()
        while column not in 'ABCDEFGH':
            print('Please enter a valid column')
            column = input('Please enter a ship column A-H:\n').upper()
        return int(row) - 1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1 
    return count 

create_ships(HIDDEN_BOARD) 
print_board(HIDDEN_BOARD)
turns = 10


#Game Loop 
while turns > 0: 
    if turns == 10: 
        print('Greetings Commander. The world Naval Alliance needs your help!\n Aliens are invading and you need to blow em up.')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print('You have already bombed that co-ordinate')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('You have struck one of the invaders ships! Well done commander')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1 
    else:
        print('No casualties there commander, a miss!')
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print('Congrats, you have saved the earth!')
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('The aliens have landed, commander. We have failed!')
        break 

