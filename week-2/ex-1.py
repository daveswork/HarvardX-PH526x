import numpy as np
import random
import time
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt

def create_board():
    return np.zeros(shape=(3,3), dtype=np.int)

def place(board, player, position):
    board[position] = player
    return board

def possibilities(board):
    available_positions = np.where(board == 0)
    available_locations = list(zip(available_positions[0], available_positions[1]))
    return available_locations

def random_place(board, player):
    position = random.choice(possibilities(board))
    return place(board, player, position)

def row_win(board, player):
    for row in board:
        win = True
        for place in row:
            if place != player:
                win = False
        if win == True:
            return win
    return win

def col_win(board, player):
    cols = np.transpose(board)
    for row in cols:
        if np.all(row == player):
            return True
    return False

def diag_win(board, player):
    first_diag = np.diag(board)
    second_diag = np.diag(np.fliplr(board))
    if np.all(first_diag == player) or np.all(second_diag == player):
        return True
    return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board, player):
            winner = player
        elif col_win(board, player):
            winner = player
        elif diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    game_board = create_board()
    turn = True
    playable = 0
    while playable == 0:
        if turn:
            random_place(game_board,1)
            turn = not(turn)
            playable = evaluate(game_board)
        else:
            random_place(game_board,2)
            turn = not(turn)
            playable = evaluate(game_board)
    #print(game_board)
    return playable

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            random_place(board,player)
            # use `random_place` to play a game, and store as `board`.
            # use `evaluate(board)`, and store as `winner`.
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


#board = create_board()

#place(board, 1, (1,1))

#print(board)
#print(possibilities(board))
#board = random_place(board, 2)

# play_results = []
# start_time = time.time()
# for i in range(1000):
#     play_results.append(play_game())
#
# total_time = time.time() - start_time
# print(total_time)
