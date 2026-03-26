import os
import sys

def print_board(board):
    """Print the Tic Tac Toe board"""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Check if the player has won"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Check if the board is full"""
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    """Get a list of empty cells"""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    """Minimax algorithm for AI player"""
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    """Get the best move for the AI player using minimax"""
    best_score = -float("inf")
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def play_game():
    """Main game loop"""
    print("Welcome to Tic Tac Toe!")
    print("You are X and the AI is O")
    print("You can play first or let the AI start")

    # Initialize board
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Choose who goes first
    first = input("Do you want to play first? (y/n): ").lower()
    current_player = "X" if first == "y" else "O"

    while True:
        print_board(board)

        if current_player == "X":
            # Human player's turn
            print("Your turn (X)")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))

                if row not in range(3) or col not in range(3):
                    print("Invalid coordinates. Try again.")
                    continue

                if board[row][col] != " ":
                    print("Cell already occupied. Try again.")
                    continue

                board[row][col] = "X"

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

        else:
            # AI player's turn
            print("AI's turn (O)")
            row, col = get_best_move(board)
            board[row][col] = "O"
            print(f"AI plays at row {row}, column {col}")

        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break

        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

def main():
    """Main function"""
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()