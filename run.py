# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#X = placing ship and hit battleship

#' ' for available space

#'-' for missed shot 

#For random int
from random import randint 
boat = """
              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
"""

title = """
______   ___   _____  _____  _      _____  _   _  _____ ______  _____ 
| ___ \ / _ \ |_   _||_   _|| |    /  ___|| | | ||_   _|| ___ \/  ___|
| |_/ // /_\ \  | |    | |  | |    \ `--. | |_| |  | |  | |_/ /\ `--. 
| ___ \|  _  |  | |    | |  | |     `--. \|  _  |  | |  |  __/  `--. \
| |_/ /| | | |  | |    | |  | |____/\__/ /| | | | _| |_ | |    /\__/ /
\____/ \_| |_/  \_/    \_/  \_____/\____/ \_| |_/ \___/ \_|    \____/ 
                                                                      
"""

#Variable for board size 

board_size = 8 

#For the Ships 
HIDDEN_BOARD = [[' '] * 8 for x in range (board_size)] 

#For Guessing
GUESS_BOARD = [[' '] * 8 for x in range (board_size)] 

#Convert guess letter string to int 
letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7 }

#Function for the creation of the board 
def print_board(board):
    print(' A B C D E F G H')
    print(' - - - - - - - - ')
    row_number = 1
    for row in board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1
    print(' - - - - - - - - ')

#Variable for number of ships
num_of_ships = 5  

#Places ships on the board on game start 
def create_ships(board):
    for ship in range(num_of_ships):
        ship_row, ship_column = randint(0,7), randint(0,7) 
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'


#Do a try and except on these later to prevent crashing!!! 

#Player Enters a location to hit a ship 
def get_ship_location():
    while True:
        try:
            row = input('Please enter a ship row numbered 1-8:\n')
            if not row:
                raise ValueError("Row number is required")
            row = int(row)  # Convert input to integer
            if row not in range(1, 9):
                raise ValueError("Invalid row number")

            column = input('Please enter a ship column A-H:\n').upper()
            if not column:
                raise ValueError("Column letter is required")
            if column not in 'ABCDEFGH':
                raise ValueError("Invalid column letter")

            return row - 1, letters_to_numbers[column]

        except ValueError as e:
            print("Invalid input:", e)

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
        print(title)
        print(boat)
        name = input("Greetings Commander. What is your name?\n") 
        print(f'Greetings Commander {name}. The world Naval Alliance needs your help!\n Aliens are invading and you need to blow em up.')
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
        #Play again Option in here 
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('The aliens have landed, commander. We have failed!')
        break 

