from random import randint
import time 

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

#Tracking win scores

player_wins = 0

alien_wins = 0

#The background board where the enemy ships are hidden
HIDDEN_BOARD = [[' '] * 8 for x in range (board_size)]

#Player's Board
PLAYER_BOARD = [[' '] * 8 for _ in range(board_size)]

#Convert guess letter string to int
letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def print_board(board):
    """
    Creates the game board
    """
    print('  A B C D E F G H')
    print('  - - - - - - - - ')
    row_number = 1
    for row in board:
        formatted_row = []
        for cell in row:
            if cell == 'X':
                formatted_row.append('\033[91mX\033[0m')  # Red color for "X"
            elif cell == 'O':
                formatted_row.append('\033[94mO\033[0m')  # Blue color for "O"
            else:
                formatted_row.append(cell)
        print(f'{row_number}|{"|".join(formatted_row)}|')
        row_number += 1
    print('  - - - - - - - - ')

#Variable for number of ships
num_of_ships = 5

def create_ships(board):
    """
    Clears the board and places new ships on it. Takes board as argument
    Enemy Ships as X, Player ships as O
    """
    for row in range(board_size):
        for column in range(board_size):
            board[row][column] = ' '  # Clear the board

    if board == HIDDEN_BOARD:
        for ship in range(num_of_ships):
            ship_row, ship_column = randint(0, 7), randint(0, 7)
            while board[ship_row][ship_column] == 'X':
                ship_row, ship_column = randint(0, 7), randint(0, 7)
            board[ship_row][ship_column] = 'X'

    if board == PLAYER_BOARD:
        for ship in range(num_of_ships):
            ship_row, ship_column = randint(0, 7), randint(0, 7)
            while board[ship_row][ship_column] == 'O':
                ship_row, ship_column = randint(0, 7), randint(0, 7)
            board[ship_row][ship_column] = 'O'

def get_ship_location(guess_board):
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

            column = input('Please enter a ship column A-H:\n').upper()
            if not column:
                raise ValueError("Column letter is required")
            if len(column) != 1 or column not in 'ABCDEFGH':
                raise ValueError("Invalid column value")

            if guess_board[row - 1][letters_to_numbers[column]] == '-' or guess_board[row - 1][letters_to_numbers[column]] == 'X':
                raise ValueError("You have already bombed that coordinate")

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

def ai_guess():
    """
    Generates the AI's guess for the player's ships.
    """
    while True:
        row = randint(0, 7)
        column = randint(0, 7)
        if PLAYER_BOARD[row][column] != '-' and PLAYER_BOARD[row][column] != 'X':
            return row, column

def playgame():
    """
    The central loop of the game
    """

    global player_wins, alien_wins  # Access the global win variables

    #For Guessing - Moved here for when the player resets the game so it doesn't use the same guess board each game
    GUESS_BOARD = [[' '] * 8 for x in range (board_size)]

    create_ships(HIDDEN_BOARD)

    create_ships(PLAYER_BOARD)

    turns = 15

    name = ""

    while turns > 0:
        if turns == 15:
            print(TITLE)
            print(BOAT)

            #Name loop
            while not name.strip():
                name = input("Greetings Commander. What is your name?\n")
                if not name.strip():
                    print("Please enter a valid name!")

            print(f'Greetings Commander {name}. The world Naval Alliance needs your help!\n'
                  'Aliens are invading and you need to blow em up.')
            time.sleep(1)
            print('Ironically this takes the form of a game of battleships. What are the chances?!')
            time.sleep(1)

        print("   Alien Ships")
        print_board(GUESS_BOARD)

        print("   Your Ships")
        print_board(PLAYER_BOARD)

        print('You have ' + str(turns) + ' turns remaining')

        row, column = get_ship_location(GUESS_BOARD)
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
            player_wins += 1
            print('Congrats, you have saved the earth!')
            print(f'You have defeated the aliens {player_wins} time(s). The aliens have won {alien_wins} time(s).')
            play_again = input('Do you want to play again? (y/n):\n').lower()
            if play_again!= "y":
                print("Then take a well deserved vacation, commander.")
                break
            elif play_again == "y":
                playgame()
            break
            #Play again Option in here

        if turns == 0:
            alien_wins += 1
            print('The aliens have landed, commander. We have failed!')
            print(f'You have defeated the aliens {player_wins} time(s).'
                  f'The aliens have won {alien_wins} time(s).')
            play_again = input('Do you want to play again? (y/n):\n').lower()
            if play_again != "y":
                print("Then the earth is doomed...")
                break
            elif play_again == "y":
                playgame()
            break

        print("Alien's turn...")
        time.sleep(1)
        
        # AI's turn
        ai_row, ai_column = ai_guess()
        #Should not happen as preventd in ai_guess but just in case
        if PLAYER_BOARD[ai_row][ai_column] == '-':
            print('The aliens have already bombed that coordinate')
        elif PLAYER_BOARD[ai_row][ai_column] == 'O':
            print('The aliens have struck one of your ships! Beware, commander')
            PLAYER_BOARD[ai_row][ai_column] = 'X'
        else:
            print('The aliens missed their shot, commander!')
            PLAYER_BOARD[ai_row][ai_column] = '-'

        if count_hit_ships(PLAYER_BOARD) == 5:
            print('Oh no, the aliens have destroyed all your ships! The earth is doomed!')
            alien_wins += 1
            print('The aliens have landed, commander. We have failed!')
            play_again = input('Do you want to play again? (y/n):\n').lower()
            if play_again != "y":
                print("Then the earth is lost...")
                break
            elif play_again == "y":
                playgame()
            break

playgame()