# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

# -------------Setting the board, players and hiding battleships-------------

board = []

for x in range(0,5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print("Let's play Battleship!")
print("This is a 2 player game")

player_1 = input("Enter first name: ")
player_2 = input("Enter second name: ")
players = [player_1, player_2]

def random_player(players):
    return random.choice(players)

def random_row(board):
  return random.randint(0,len(board)-1)

def random_col(board):
  return random.randint(0,len(board[0])-1)

if random_player(players) == player_1:
  print(player_1, "starts the game.")
else:
  print(player_2, "starts the game.")
  
ship_row_1 = random_row(board)
ship_col_1 = random_col(board)
# print (ship_row_1)
# print (ship_col_1)

ship_row_2 = random_row(board)
ship_col_2 = random_col(board)
# print (ship_row_2)
# print (ship_col_2)

print_board(board)