import random

# Connect Four Board Class
class ConnectFourBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]

    def print_board(self):
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print('+---------------+')
        print(' 0  1  2  3  4  5  6')

    def is_valid_move(self, col):
        return 0 <= col < 7 and self.board[0][col] == ' '

    def make_move(self, col, player):
        for row in reversed(self.board):
            if row[col] == ' ':
                row[col] = player
                return True
        return False

# Simple Heuristic Function for AI
def heuristic(board, player):
    if board.is_valid_move(3):
        return 3  # Prefer center
    valid_moves = [col for col in range(7) if board.is_valid_move(col)]
    return random.choice(valid_moves) if valid_moves else None

# Main Game Loop - User and AI Interaction
def main():
    board = ConnectFourBoard()
    print("Starting Connect Four Board:")
    board.print_board()

    try:
        user_move = int(input("\nYour turn! Enter a column (0-6) to place 'O': "))
        if board.is_valid_move(user_move):
            board.make_move(user_move, 'O')
        else:
            print("Invalid move. AI will start instead.")
    except ValueError:
        print("Invalid input. AI will start instead.")

    board.print_board()

    print("\nAI is making its move...")
    ai_move = heuristic(board, 'X')
    if ai_move is not None:
        board.make_move(ai_move, 'X')
        print(f"AI placed at column {ai_move}")
    else:
        print("No valid moves left.")

    board.print_board()

if __name__ == "__main__":
    main()
