board = [
    ['_', 'O', 'X'],
    ['X', 'O', 'O'],
    ['_', '_', 'X']
]

def check_winner(player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True

    # Diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

# 3 moves
turn = 0
while turn < 3:

    player = 'X' if turn % 2 == 0 else 'O'

    block = int(input(f"{player}'s turn - Enter block (1-9): "))

    row = (block - 1) // 3
    col = (block - 1) % 3

    if board[row][col] != '_':
        print("Block already occupied. Try again.")
        continue

    board[row][col] = player
    turn += 1
    if check_winner(player):
        print(player, "wins!")
        break
else:
    print("Game Draw!")
