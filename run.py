from random import randint 

class Board:

    def __init__(self, num_ships, player_name, board_size, type):
        self.num_ships = num_ships
        self.board = board
        self.player_name = player_name
        self.board_size = board_size
        self.type = type
        self.ships = []
        self.guesses = []

    # def guess(self, x, y):
    #     self.guesses.append((x,y))
    #     self.board[x][y] = "X"

    #     if (x,y) in self.ships:
    #         self.board[x][y] = "$"
    #         return "BOOM"
    #     else:
    #         return "MISS"

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


# populate board with ships

# def populate_board():
#     for i in range(4):
#         while True:
#             x = randint(0, len(board) - 1)
#             y = randint(0, len(board) - 1) 

#             if board[y][x] == 'taken':
#                 ships = 1
#                 break
#             else:
#                 continue

def get_random_coordinates(board_size):
    ship_row = randint(0, board_size - 1)
    ship_col = randint(0, board_size - 1)
    return ship_row, ship_col




# random coordinates

def random_row(board):
    randint(0, len(board) - 1)

def random_column(board):
    randint(0, len(board) - 1)

# Player Guess

def guess():
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))
    if guess_row >= 5 or guess_col >= 5:
        print("Please choose a number between 0 and 4")
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Column: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("BOOM! Good hit.")
    else:
        print("MISS. Reload the cannons and try again on the next round.") 

# def computer_guess()

# def next_round
    
def start_game():

    global num_ships
    num_ships = 2
    global board_size
    board_size = 3
    global player_name

    print("Welcome to Battleships. Are you ready to go to war? Enlist below if you are.")
    player_name = input("Enter your name soldier: \n")
    print("\n")
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

