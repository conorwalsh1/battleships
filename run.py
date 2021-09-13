from random import randint 

class Board:

    def __init__(self, num_ships, player_name, board_size, turn):
		self.num_ships = num_ships
		self.player_name = player_name
		self.board_size = board_size
		self.turn = turn
        self.ships = []
        self.guesses = []