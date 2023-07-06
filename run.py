#For random int
from random import randint 
from enum import Enum



BOAT = """
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

TITLE = """
______   ___   _____  _____  _      _____  _   _  _____ ______  _____ 
| ___ \ / _ \ |_   _||_   _|| |    /  ___|| | | ||_   _|| ___ \/  ___|
| |_/ // /_\ \  | |    | |  | |    \ `--. | |_| |  | |  | |_/ /\ `--. 
| ___ \|  _  |  | |    | |  | |     `--. \|  _  |  | |  |  __/  `--. | 
| |_/ /| | | |  | |    | |  | |____/\__/ /| | | | _| |_ | |    /\__/ /
\____/ \_| |_/  \_/    \_/  \_____/\____/ \_| |_/ \___/ \_|    \____/ 
                                                                      
"""

#Variable for board size 

board_size = 8 

class Symbols(Enum):
    HIT = 'X'
    MISS = '-'

#The background board 
HIDDEN_BOARD = [[' '] * 8 for x in range (board_size)] 


#Convert guess letter string to int 
letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7 }

def print_board(board):
    """
    Creates the game board
    """
    print('  A B C D E F G H')
    print('  - - - - - - - - ')
    row_number = 1
    for row in board:
        formatted_row = [f'\033[91m{cell}\033[0m' if cell == 'X' else cell for cell in row]
        print(f'{row_number}|{"|".join(formatted_row)}|')
        row_number += 1
    print('  - - - - - - - - ')

#Variable for number of ships
num_of_ships = 5 

#Places ships on the board on game start 
def create_ships(board):
    """
    Places the ships on the board, takes the board as argument 
    """
    for ship in range(num_of_ships):
        ship_row, ship_column = randint(0,7), randint(0,7) 
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    """
    Function for the players entering the location of a ship to hit 
    """
    while True:
        try:
            row = input('Please enter a ship row numbered 1-8:\n')
            if not row:
                raise ValueError("Row number is required")
            row = int(row)  # Convert input to integer
            if row not in range(1, 9):
                raise ValueError("Invalid row number")
            
        except ValueError as e:
            print("Invalid input:", e)
        
        try:
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


def playgame():
    """
    The central loop of the game 
    """

    #For Guessing - Moved here for when the player resets the game so it doesn't use the same guess board each game 
    GUESS_BOARD = [[' '] * 8 for x in range (board_size)] 

    create_ships(HIDDEN_BOARD) 
    print_board(HIDDEN_BOARD) #Temporary 

    turns = 10

    name = ""

    while turns > 0: 
        if turns == 10:
            print(TITLE)
            print(BOAT)

            #Name loop
            while not name.strip():
                name = input("Greetings Commander. What is your name?\n") 
                if not name.strip():
                    print("Please enter a valid name!")
            
            print(f'Greetings Commander {name}. The world Naval Alliance needs your help!\n'
                  'Aliens are invading and you need to blow em up.\n'
                  'Ironically this takes the form of a game of battleships. What are the chances?!')
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
            play_again = input('Do you want to play again? (y/n):\n').lower()
            if play_again!= "y":
                print("Then take a well deserved vacation, commander.")
                break
            elif play_again == "y":
                playgame()
            break 
            #Play again Option in here 
        print('You have ' + str(turns) + ' turns remaining')
        if turns == 0:
            print('The aliens have landed, commander. We have failed!')
            play_again = input('Do you want to play again? (y/n):\n').lower()
            if play_again != "y":
                print("Then the earth is doomed...")
                break
            elif play_again == "y":
                playgame()
            break 

playgame()

#print(Symbols.HIT.value)