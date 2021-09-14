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


    # guess + insert ships

# create boards

board = []    

for i in range(5):
    board.append(["O"] * 5)

def print_player_board(board):
    for row in board:
        print(" ".join(row))

def print_computer_board(board):
    for row in board:
        print(" ".join(row))

x = randint(0, len(board) - 1)
y = randint(0, len(board) - 1)

# populate board with ships

def populate_board():
    player_ships = [(x, y), (x, y), (x, y), (x, y)]
    comp_ships = [(x, y), (x, y), (x, y), (x, y)]

# random coordinates

def random_row(board):
    randint(0, len(board) - 1)

def random_column(board):
    randint(0, len(board) - 1)

# def player_guess()

# def computer_guess()

# def check_correct

# def next_round
    
def start_game():

    num_ships = 4
    board_size = 5
    print("Welcome to Battleships. Are you ready to go to war? Enlist below if you are.")
    player_name = input("Enter your name soldier: \n")
    print(f"Glad to have you aboard {player_name}. The board size is {board_size} x {board_size}, you have {num_ships} ships to protect and {num_ships} ships to eliminate.")
    print(f"When you are prompted {player_name}, enter which row and then which column you would like to strike.\nThe first coordinate on the board will be row: 0, column: 0. The last coordinate on the board will be row: 4, column: 4.")
    print("Best of luck comrade, you're going to need it out there.")
    print("+" * 35)
    print(f"{player_name}'s Board:")
    print_player_board(board)
    print("Computer's Board:")
    print_computer_board(board)
    print("+" * 35)

    # computer_board = Board(board_size, num_ships, "Computer", type="computer")
    # player_board = Board(board_size, num_ships, player_name, type="player")
    
start_game()