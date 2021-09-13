from random import randint 

class Board:

    def __init__(self, num_ships, player_name, board_size, turn):
        self.num_ships = num_ships
        self.player_name = player_name
        self.board_size = board_size
        self.turn = turn
        self.ships = []
        self.guesses = []
    
def start_game():

    num_ships = 4
    board_size = 5
    print("Welcome to Battleships. Are you ready to go to war? Enlist below if you are.")
    player_name = input("Enter your name soldier: \n")
    print(f"Glad to have you aboard {player_name}. The board size is {board_size} x {board_size}, you have {num_ships} ships to protect and {num_ships} ships to eliminate.\nBest of luck comrade, you'll need it out there.")

start_game()