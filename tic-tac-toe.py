# Tic-Tac-Toe AI using Minimax with Alpha-Beta Pruning

# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")

# Function to check if the board is full
def is_full(board):
    return " " not in board

# Function to check if a player has won
def check_win(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player):
    scores = {
        "X": 1,
        "O": -1,
        "tie": 0
    }

    if check_win(board, "X"):
        return scores["X"]
    if check_win(board, "O"):
        return scores["O"]
    if is_full(board):
        return scores["tie"]

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using Minimax with Alpha-Beta Pruning
def find_best_move(board):
    best_move = None
    best_eval = float("-inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            eval = minimax(board, 0, False)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
while True:
    print_board(board)
    
    # Player's move
    while True:
        player_move = input("Enter your move (1-9): ")
        if player_move.isdigit() and 1 <= int(player_move) <= 9 and board[int(player_move) - 1] == " ":
            board[int(player_move) - 1] = "O"
            break
        else:
            print("Invalid move. Try again.")

    # Check if the player has won
    if check_win(board, "O"):
        print_board(board)
        print("Congratulations! You win!")
        break

    # Check if it's a tie
    if is_full(board):
        print_board(board)
        print("It's a tie!")
        break

    # AI's move
    ai_move = find_best_move(board)
    board[ai_move] = "X"

    # Check if the AI has won
    if check_win(board, "X"):
        print_board(board)
        print("AI wins! You lose.")
        break