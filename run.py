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
        board[x][y] = '@'

    return board

def create_comp_board():

    global comp_board
    comp_board = []    

    for i in range(board_size):
        comp_board.append(["O"] * board_size)

    for i in range(num_ships):
        place = get_random_coordinates(board_size)
        x = place[0]
        y = place[1]
        comp_board[x][y] = 'O'

    return comp_board




def print_board(board):
    for row in board:
        print(" ".join(row))

def get_random_coordinates(board_size):
    global ship_row
    ship_row = randint(0, board_size - 1)
    global ship_col
    ship_col = randint(0, board_size - 1)
    return ship_row, ship_col

# Player Guess

def player_guess():
    
    guess_row = None
    while True:
        print(f"Please choose a number between 0 and {board_size - 1}")
        guess_row = input("Guess Row: ")
        if guess_row.isdigit():
            guess_row = int(guess_row)
            if guess_row > 3 or guess_row < 0:
                continue
            break
        else:
            continue

    guess_col = None
    while True:
        print(f"Please choose a number between 0 and {board_size - 1}")
        guess_col = input("Guess Column: ")
        if guess_col.isdigit():
            guess_col = int(guess_col)
            if guess_row > 3 or guess_row < 0:
                continue
            break
        else:
            continue

    # global player_board
    # player_board = [guess_row][guess_col]

    if guess_row == ship_row and guess_col == ship_col:
        print("BOOM! Good hit.")
        board[guess_row][guess_col] = '*'
    else:
        print("MISS. Reload the cannons and try again on the next round.") 
        board[guess_row][guess_col] = 'X'


# Computer Guess

def computer_guess():
    
    comp_guess = get_random_coordinates(board_size)

    print(f"Computer has guessed Row, Column: {comp_guess}")
    if comp_guess == ship_row and ship_col:
        print("WE TOOK A HIT!!! Computer has guessed correctly")
        board[comp_guess] = '*'
    else:
        print("PHEW. Computer has guessed incorrectly.")
        board.append('X')
    print(f"{player_name} has blank ships remaining.")
    print("Computer has blank ships remaining.") 
    next_round = input("To proceed to the next round, press 'y' key: ")
    next_round()

    
def next_round():
    print("+" * 35)
    print(f"{player_name}'s Board: ")
    print_board(player_board)
    print("Computer's Board: ")
    print_board(computer_board)
    print("+" * 35)
    player_guess()
    computer_guess()
    
def start_game():

    global num_ships
    num_ships = 3
    global board_size
    board_size = 3
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
    player_board = create_board()
    computer_board = create_comp_board()
    print(f"{player_name}'s Board: ")
    print_board(player_board)
    print("Computer's Board: ")
    print_board(computer_board)
    print("+" * 35)
    player_guess()
    computer_guess()
    next_round()

main()

