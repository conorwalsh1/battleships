from random import randint

computer_guessed_previously = []
player_guessed_previously = []
player_ships_placed = []
computer_ships_placed = []
player_ships_remaining = 2
comp_ships_remaining = 2


# Create Computer Board


def create_board():

    global board
    board = []

    for _ in range(board_size):
        board.append(["O"] * board_size)

    for _ in range(num_ships):
        place = get_random_coordinates(board_size)
        x = place[0]
        y = place[1]
        ships_created = [x, y]
        if ships_created not in computer_ships_placed:
            computer_ships_placed.append([x, y])
        else:
            # Regenrate coordinates until they are new
            # So that in the end, correct number of ships are placed
            ship_there = True
            while ship_there:
                place = get_random_coordinates(board_size)
                x = place[0]
                y = place[1]
                ships_created = [x, y]
                if ships_created not in computer_ships_placed:
                    computer_ships_placed.append([x, y])
                    ship_there = False
    
    return board

# Create Player Board


def create_player_board():

    global player_board
    player_board = []

    for _ in range(board_size):
        player_board.append(["O"] * board_size)

    for _ in range(num_ships):
        place = get_random_coordinates(board_size)
        x = place[0]
        y = place[1]
        ships_created = [x, y]
        if ships_created not in player_ships_placed:
            player_board[x][y] = '@'
            player_ships_placed.append([x, y])
        else:
            ship_there = True
            while ship_there:
                place = get_random_coordinates(board_size)
                x = place[0]
                y = place[1]
                ships_created = [x, y]
                if ships_created not in player_ships_placed:
                    player_board[x][y] = '@'
                    player_ships_placed.append([x, y])
                    ship_there = False


    return player_board

# Print Boards


def print_board(board):
    for row in board:
        print(" ".join(row))

# Generate Random Coordinates


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
        guess_row = input("Guess Row:\n")
        if guess_row.isdigit():
            guess_row = int(guess_row)
            if guess_row > board_size or guess_row < 0:
                continue
            break
        else:
            continue

    guess_col = None
    while True:
        print(f"Please choose a number between 0 and {board_size - 1}")
        guess_col = input("Guess Column:\n")
        print("+" * 35)
        if guess_col.isdigit():
            guess_col = int(guess_col)
            if guess_col > board_size or guess_col < 0:
                continue
            break
        else:
            continue
    guess_location = [guess_row, guess_col]
    if guess_location not in player_guessed_previously:
    
        if guess_location in computer_ships_placed:
            
            global comp_ships_remaining
            comp_ships_remaining -= 1
            print("BOOM! Good hit!!!")
            print(f"Computer has {comp_ships_remaining} ships remaining.")
            board[guess_row][guess_col] = '$'
            player_guessed_previously.append([guess_row, guess_col])

        else:
            print("MISS. Reload the cannons and try again on the next round.")
            board[guess_row][guess_col] = 'X'
            player_guessed_previously.append([guess_row, guess_col])

    else:
        print("You have guessed already. Please try again!")
        player_guess()


# Computer Guess

def computer_guess():

    comp_guess_row = randint(0, board_size - 1)
    comp_guess_col = randint(0, board_size - 1)

    current_guess = [comp_guess_row, comp_guess_col]

    if current_guess not in computer_guessed_previously:
        print("Computer has guessed:")
        print(f"Row: {comp_guess_row}, Column: {comp_guess_col}")
        if current_guess in player_ships_placed:
            global player_ships_remaining
            player_ships_remaining -= 1
            print("WE TOOK A HIT!!!")
            print(f"Our fleet has {player_ships_remaining} ships remaining.")
            player_board[comp_guess_row][comp_guess_col] = '$'
            computer_guessed_previously.append([comp_guess_row, comp_guess_col])
            nxt_round = input("Press any key to move on to the next round: ")
            return nxt_round
        else:
            print("PHEW. Computer has guessed incorrectly.")
            player_board[comp_guess_row][comp_guess_col] = 'X'
            computer_guessed_previously.append([comp_guess_row, comp_guess_col])
            nxt_round = input("Press any key to move on to the next round: ")
            return nxt_round
    else:
        computer_guess()


def next_round():
    print("+" * 35)
    print("Computer's Board: ")
    print_board(board)
    print(f"{player_name}'s Board: ")
    print_board(player_board)
    print("+" * 35)

# Start Game Function


def start_game():

    global num_ships
    num_ships = 3
    global board_size
    board_size = 3
    global player_name
    global comp_ships_remaining
    comp_ships_remaining = 3
    global player_ships_remaining
    player_ships_remaining = 3

    print("Welcome to Battleships.")
    print("Are you ready to go to war? Enlist below if you are.")
    player_name = input("Enter your name soldier: \n")
    print("+" * 35)
    print(f"Glad to have you aboard {player_name}.")
    print(f"The board size is {board_size} x {board_size}.")
    print(f"You and computer have {num_ships} ships each.")
    print("When prompted, type which row and column you would like to strike.")
    print("The first coordinate on the board will be row: 0, column: 0.")
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
    print(player_ships_placed)
    computer_board = create_board()
    print(computer_ships_placed)
    print("Computer's Board: ")
    print_board(computer_board)
    print(f"{player_name}'s Board: ")
    print_board(player_board)
    print("+" * 35)


    while True:
        if player_ships_remaining > 0 and comp_ships_remaining > 0:
            player_guess()
            computer_guess()
            next_round()
        elif player_ships_remaining <= 0:
            print("GAME OVER. YOU WIN")
            break
        else:
            print("GAME OVER. COMPUTER WINS")
            break


main()
