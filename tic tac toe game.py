def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)
    players = ['X', 'O']
    player_index = 0
    game_over = False

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not game_over:
        player = players[player_index]
        row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            print_board(board)

            if check_win(board, player):
                print(f"Player {player} wins!")
                game_over = True
