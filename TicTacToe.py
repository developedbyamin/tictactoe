def check_draw(board):
    for row in board:
        if '_' in row:
            return False
    return True

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return board[i][0], True
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return board[0][i], True
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0], True
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2], True
    
    return None, False

gameboard = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

turn = True
while True:
    for row in gameboard:
        for dot in row:
            print(dot, end=' ')
        print()
    if turn:
        userX = int(input("X Turn: "))
        if(userX == 0):
            print('Game Restarted by X!')
            gameboard = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            continue
        
        if userX <= 3:
            if gameboard[0][userX - 1] == '_':
                gameboard[0][userX - 1] = "X"
            else:
                continue
        elif 3 < userX <= 6:
            if gameboard[1][userX - 1 - 3] == '_':
                gameboard[1][userX - 1 - 3] = "X"
            else:
                continue
        elif 6 < userX <= 9:
            if gameboard[2][userX - 1 - 6] == '_':
                gameboard[2][userX - 1 - 6] = "X"
            else:
                continue
        turn = False
    else:
        
        userO = int(input("O Turn: "))
        if(userO == 0):
            print('Game Restarted by O!')
            gameboard = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            continue
        
        if userO <= 3:
            if gameboard[0][userO - 1] == '_':
                gameboard[0][userO - 1] = "O"
            else:
                continue
        elif 3 < userO <= 6:
            if gameboard[1][userO - 1 - 3] == '_':
                gameboard[1][userO - 1 - 3] = "O"
            else:
                continue
        elif 6 < userO <= 9:
            if gameboard[2][userO - 1 - 6] == '_':
                gameboard[2][userO - 1 - 6] = "O"
            else:
                continue
        turn = True
    winner, is_win = check_win(gameboard)
    if is_win:
        print(f"{winner} wins!")
        break
    if check_draw(gameboard):
        print("It's a draw!")
        break

