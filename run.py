from random import randint 

# create boards

def create_board():

    global board
    board = []    

    for i in range(board_size):
        board.append(["O"] * board_size)

    for i in range(num_ships):

        place = get_random_coordinates(board_size)
        x = place[0]
        y = place[1]
        board[x][y] = 'X'
    
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def get_random_coordinates(board_size):
    global ship_row
    ship_row = randint(0, board_size - 1)
    global ship_col
    ship_col = randint(0, board_size - 1)
    return ship_row, ship_col


# random coordinates

# def random_row(board):
#     randint(0, len(board) - 1)

# def random_column(board):
#     randint(0, len(board) - 1)

# Player Guess

def guess():
    
    guess_row = None
    while True:
        print("Please choose a number between 0 and 4")
        guess_row = input("Guess Row: ")
        if guess_row.isdigit():
            guess_row = int(guess_row)
            if guess_row > 4 or guess_row < 0:
                continue
            break
        else:
            continue

    guess_col = None
    while True:
        print("Please choose a number between 0 and 4")
        guess_col = input("Guess Column: ")
        if guess_col.isdigit():
            guess_col = int(guess_col)
            if guess_row > 4 or guess_row < 0:
                continue
            break
        else:
            continue

    if guess_row == ship_row and guess_col == ship_col:
        print("BOOM! Good hit.")
    else:
        print("MISS. Reload the cannons and try again on the next round.") 

# Computer Guess

# def computer_guess():
    
# def next_round
    
def start_game():

    global num_ships
    num_ships = 4
    global board_size
    board_size = 5
    global player_name

    print("Welcome to Battleships. Are you ready to go to war? Enlist below if you are.")
    player_name = input("Enter your name soldier: \n")
    print("+" * 35)
    print(f"Glad to have you aboard {player_name}. The board size is {board_size} x {board_size}, you have {num_ships} ships to protect and {num_ships} ships to eliminate.")
    print(f"When you are prompted, enter which row and then which column you would like to strike.\nThe first coordinate on the board will be row: 0, column: 0. The last coordinate on the board will be row: {board_size - 1}, column: {board_size - 1}.")
    print("Best of luck comrade, you're going to need it out there.")
    print("+" * 35)

def main():

    start_game()
    get_random_coordinates(board_size)
    computer_board = create_board()
    player_board = create_board()
    computer_board = create_board()
    print(f"{player_name}'s Board: ")
    print_board(player_board)
    print("Computer's Board: ")
    print_board(computer_board)
    print("+" * 35)
    guess()

main()

