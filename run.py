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

    board = []    

    for _ in range(5):
        board.append(["0"] * 5)

    def print_board(board):
        for row in board:
            print(" ".join(row))

# def populate_board()

# def computer_guess()
    
# def start_game()

    num_ships = 4
    board_size = 5
    print("Welcome to Battleships. Are you ready to go to war? Enlist below if you are.")
    player_name = input("Enter your name soldier: \n")
    print(f"Glad to have you aboard {player_name}. The board size is {board_size} x {board_size}, you have {num_ships} ships to protect and {num_ships} ships to eliminate.\nBest of luck comrade, you're going to need it out there.")
    print("+" * 35)
    print(f"{player_name}'s Board:")
    print_board(board)
    print("Computer's Board:")
    print_board(board)
    print("+" * 35)
    

# start_game()