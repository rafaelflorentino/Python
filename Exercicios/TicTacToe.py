import random

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|  " + "  |  ".join(row) + "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    while True:
        move = input("Entre com a sua jogada (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                break
            else:
                print("A célula já está ocupada. Tente novamente.")
        else:
            print("Movimento inválido. Porfavor entre com um número entre 1 e 9.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def check_victory(board, sign):
    # Check rows and columns
    for i in range(3):
        if all([cell == sign for cell in board[i]]) or all([board[j][i] == sign for j in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def computer_move(board):
    free_fields = make_list_of_free_fields(board)
    move = random.choice(free_fields)
    board[move[0]][move[1]] = 'X'

def tic_tac_toe():
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if check_victory(board, 'O'):
            print("Você ganhou!")
            break
        if check_draw(board):
            print("Empatou!")
            break

        computer_move(board)
        display_board(board)
        if check_victory(board, 'X'):
            print("Computador Ganhou.")
            break
        if check_draw(board):
            print("Empatou!")
            break

tic_tac_toe()
