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
        board[x][y] = 'O'

    return board

def create_player_board():

    global player_board
    player_board = []    

    for i in range(board_size):
        player_board.append(["O"] * board_size)

    for i in range(num_ships):
        global place
        place = get_random_coordinates(board_size)
        x = place[0]
        y = place[1]
        player_board[x][y] = '@'

    return player_board




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

    ships_remaining = 5
    ships_remaining = ships_remaining - 1
    
    guess_row = None
    while True:
        print(f"Please choose a number between 0 and {board_size - 1}")
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
        print(f"Please choose a number between 0 and {board_size - 1}")
        guess_col = input("Guess Column: ")
        print("+" * 35)
        if guess_col.isdigit():
            guess_col = int(guess_col)
            if guess_row > 4 or guess_row < 0:
                continue
            break
        else:
            continue

    if guess_row == place[0] and guess_col == place[1]:
        print(f"BOOM! Good hit! Computer has {ships_remaining} ships remaining. Onwards comrade!")
        board[guess_row][guess_col] = '$'
    else:
        print("MISS. Reload the cannons and try again on the next round.") 
        board[guess_row][guess_col] = 'X'


# Computer Guess

def computer_guess():

    ships_remaining = 5
    ships_remaining = ships_remaining - 1
    
    comp_guess_row = randint(0, board_size - 1)
    comp_guess_col = randint(0, board_size - 1)
    
    global guessed_previously
    guessed_previously = []

    current_guess = [comp_guess_row, comp_guess_col]
    
    while current_guess in guessed_previously:
        print("PC try again")
    
    print(f"Computer has guessed Row: {comp_guess_row}, Column: {comp_guess_col}")
    if comp_guess_row == place[0] and comp_guess_col == place[1]:
        print(f"WE TOOK A HIT!!! Our fleet has {ships_remaining} ships remaining. Keep battling!")
        player_board[comp_guess_row][comp_guess_col] = '$'
        guessed_previously.append([comp_guess_row, comp_guess_col])
    else:
        print("PHEW. Computer has guessed incorrectly.")
        player_board[comp_guess_row][comp_guess_col] = 'X'
        guessed_previously.append([comp_guess_row, comp_guess_col])
    nxt_round = input("Press any key to move on to the next round: ")
    print(guessed_previously)
    next_round()

    
def next_round():
    print("+" * 35)
    print("Computer's Board: ")
    print_board(board)
    print(f"{player_name}'s Board: ")
    print_board(player_board)
    print("+" * 35)
    player_guess()
    computer_guess()
    
def start_game():

    global num_ships
    num_ships = 2
    global board_size
    board_size = 2
    global player_name

    print("Welcome to Battleships. Are you ready to go to war? Enlist below if you are.")
    player_name = input("Enter your name soldier: \n")
    print("+" * 35)
    print(f"Glad to have you aboard {player_name}. The board size is {board_size} x {board_size}, you have {num_ships} ships to protect and {num_ships} ships to eliminate.")
    print(f"When you are prompted, enter which row and then which column you would like to strike.\nThe first coordinate on the board will be row: 0, column: 0. The last coordinate on the board will be row: {board_size - 1}, column: {board_size - 1}.")
    print("Best of luck comrade, you're going to need it out there.")
    print("Map Legend:")
    print("O = Unchecked Spaces")
    print("X = Checked Spaces")
    print("$ = Confirmed Hit")
    print("@ = Your Remaining Ships")
    print("+" * 35)

def main():

    start_game()
    get_random_coordinates(board_size)
    player_board = create_player_board()
    computer_board = create_board()
    print("Computer's Board: ")
    print_board(computer_board)
    print(f"{player_name}'s Board: ")
    print_board(player_board)
    print("+" * 35)
    player_guess()
    computer_guess()
    next_round()

main()

