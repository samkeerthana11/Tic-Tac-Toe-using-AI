import random
def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_board_full(board):
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))
def available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
def minimax(board, is_maximizing):
    if check_winner(board, 'X'):
        return -1, None
    elif check_winner(board, 'O'):
        return 1, None
    elif is_board_full(board):
        return 0, None

    if is_maximizing:
        best_score = float('-inf')
        best_move = None
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            score, _ = minimax(board, False)
            board[move[0]][move[1]] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            score, _ = minimax(board, True)
            board[move[0]][move[1]] = ' '
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move
def play_game():
    board = init_board()
    current_player = 'X' 

    while True:
        print_board(board)
        if current_player == 'X':
            while True:
                move = input("Enter your move (row col): ").strip().split()
                row, col = int(move[0]), int(move[1])
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            _, best_move = minimax(board, True)
            row, col = best_move
            board[row][col] = 'O'
            print(f"AI placed 'O' on {row}, {col}")
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
play_game()
