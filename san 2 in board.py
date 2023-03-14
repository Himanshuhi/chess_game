import chess

def print_board(board):
    print("  a b c d e f g h")
    for i in range(8):
        rank = 8 - i
        row = ""
        for j in range(8):
            file = chess.FILE_NAMES[j]
            square = chess.parse_square(file + str(rank))
            piece = board.piece_at(square)
            if piece is not None:
                row += piece.symbol() + " "
            else:
                row += ". "
        print(str(rank) + " " + row + str(rank))
    print("  a b c d e f g h")

# Create an empty chess board
board = chess.Board(empty=True)

# Print the chess board with labels
print_board(board)
