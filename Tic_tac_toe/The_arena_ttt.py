import sys
import random as rng
import numpy as np

board = [[0]*3]*3
board = np.array(board)
tur = 2


def winner(board,a):
    board_check_1 = board == a
    row = np.any(np.sum(board_check_1,axis = 0) == 3)
    column = np.any(np.sum(board_check_1,axis = 1) == 3)
    diag = np.trace(board_check_1) == 3
    off_diag = np.trace(np.flip(board_check_1,1)) == 3
    if row or column or diag or off_diag == True:
        return a
    elif np.all(board != 0):
        return 'Tie'

def cheater(i,j):
    if board[i,j] != 0:
        return True
    return False

i = 0
j = 0

def player1(board,tur):
    if np.all(board == 0):
        return rng.randint(0,2),rng.randint(0,2)
    for i in [2,1,0]:
        for j in [2,1,0]:
            if cheater(i,j) == False:
                return i,j

def player2(board,tur):
    if np.all(board == 0):
        return 0,0
    board_check_1 = board == 1
    row = np.any(np.sum(board_check_1,axis = 0) == 2)
    column = np.any(np.sum(board_check_1,axis = 1) == 2)
    diag = np.trace(board_check_1) == 2
    off_diag = np.trace(np.flip(board_check_1,1)) == 2
    if row or column or diag or off_diag == True:
        return a
    

def The_game(player1,player2):
    tur = 1
    while winner(board,1) == None and winner(board,2) == None:
        if tur ==1:
            tur = 2
        elif tur == 2:
            tur = 1
        if tur == 1:
            i,j = player1(board,tur)
        if tur == 2:
            i,j = player2(board,tur)

        if cheater(i,j) == True:
            return tur, False
        board[i,j] = tur
        print(board)
        if winner(board,1) == True:
            return 1, True
        elif winner(board,2) == True:
            return 2, True
    return 0, True
    

print(The_game(player1,player1))
