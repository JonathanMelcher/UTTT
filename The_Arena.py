import sys
board = []
won = []
winner = 0
T = 0
tur = 1

### Laver bordet
for i in range(9):
    board.append([])
    won.append(0)
for i in range(9):
    for j in range(9):
        board[i].append(0)


def Player1(b, t):
    return t,4

def Player2(b,t):
    return t,3


while winner == 0:
    if tur ==1:
        a,b = Player1(board,T)
    elif tur == 2:
        a,b = Player2(board,T)
    if T !=0: ## tjekker om det er et gyldigt træk. Et træk kan være ugyldigt hvis, det ikke er på det tvungende minispil, feltet allerede er taget eller minispillet er vundet.
        if a != T:
            print(f'Player{tur} snyder')
            sys.exit()
    if board[a][b] != 0:
        print(f'Player{tur} prøver at tage et taget felt')
        sys.exit()
    if won[a] != 0:
        print(f'Player{tur} prøver at tage på et vundet mini spil')

    board[a][b] = tur # Trækket tages
    ### Tjekker om der er nogen der har vundet på mini borene 
    for i in range(9):
        if won[i] == 0:
            for j in range(3):
                if [board[i][j],board[i][j+1],board[i][j+2]] == [1,1,1]:
                    won[i] = 1
                    break
                elif [board[i][j],board[i][j+1],board[i][j+2]] == [2,2,2]:
                    won[i] = 2
                    break
                elif [board[i][j],board[i][j+3],board[i][j+6]] == [1,1,1]:
                    won[i] = 1
                    break
                elif [board[i][j],board[i][j+3],board[i][j+6]] == [2,2,2]:
                    won[i] = 2
                    break
            if [board[i][0],board[i][4],board[i][8]] == [1,1,1]:
                    won[i] = 1
                    break
            elif [board[i][0],board[i][4],board[i][8]] == [2,2,2]:
                    won[i] = 2
                    break
            elif [board[i][2],board[i][4],board[i][6]] == [1,1,1]:
                    won[i] = 1
                    break
            elif [board[i][2],board[i][4],board[i][6]] == [2,2,2]:
                    won[i] = 1
                    break
    for j in range(3):
        if [won[j],won[j+1],won[j+2]] == [1,1,1]:
            winner = 1
            break
        elif [won[j],won[j+1],won[j+2]] == [2,2,2]:
            winner = 2
            break
        elif [won[j],won[j+3],won[j+6]] == [1,1,1]:
            winner = 1
            break
        elif [won[j],won[j+3],won[j+6]] == [2,2,2]:
            winner = 2
            break
    if [won[0],won[4],won[8]] == [1,1,1]:
        winner = 1
    elif [won[0],won[4],won[8]] == [2,2,2]:
        winner = 2
    elif [won[2],won[4],won[6]] == [1,1,1]:
        winner = 1
    elif [won[2],won[4],won[6]] == [2,2,2]:
        winner = 2
    
    if tur ==1:
        tur = 2
    elif tur == 2:
        tur = 1
        
if winner != 0:
    print(f'AND THE WINNER IS ......... PLAYER {winner}')
