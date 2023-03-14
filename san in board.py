import chess

def print_board(board):
    print("      BLACK      ")
    print("  a b c d e f g h")
    print("8 " + " ".join(board.piece_at(square).symbol() if board.piece_at(square) is not None else "." for square in range(56, 64)) + " 8")
    print("7 " + " ".join(board.piece_at(square).symbol() if board.piece_at(square) is not None else "." for square in range(48, 56)) + " 7")
    print("6 " + " ".join(board.piece_at(square).symbol() if board.piece_at(square) is not None else "." for square in range(40, 48)) + " 6")
    print("5 " + " ".join(board.piece_at(square).symbol() if board.piece_at(square) is not None else "." for square in range(32, 40)) + " 5")
    print("4 " + " ".join(board.piece_at(square).symbol() if board.piece_at(square) is not None else "." for square in range(24, 32)) + " 4")
    print("3 " + " ".join(board.piece_at(square).symbol() if board.piece_at(square) is not None else "." for square in range(16, 24)) + " 3")
    print("2 " + " ".join(board.piece_at(square).symbol() if board.piece_at(square) is not None else "." for square in range(8, 16)) + " 2")
    print("1 " + " ".join(board.piece_at(square).symbol() if board.piece_at(square) is not None else "." for square in range(0, 8)) + " 1")
    print("  a b c d e f g h")
    print("      WHITE     ")

# Create an empty chess board
board1 = chess.Board(fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")  # Starting position without pieces


# Print the two chess boards
print("Board 1:")
print_board(board1)

print("")

print("SAN code")

print("            BLACK             ")
print("    a  b  c  d  e  f  g  h    ")
print("")
print(" 8  a8 b8 c8 d8 e8 f8 g8 h8  8")
print(" 7  a7 b7 c7 d7 e7 f7 g7 h7  7")
print(" 6  a6 b6 c6 d6 e6 f6 g6 h6  6")
print(" 5  a5 b5 c5 d5 e5 f5 g5 h5  5")
print(" 4  a4 b4 c4 d4 e4 f4 g4 h4  4")
print(" 3  a3 b3 c3 d3 e3 f3 g3 h3  3")
print(" 2  a2 b2 c2 d2 e2 f2 g2 h2  2")
print(" 1  a1 b1 c1 d1 e1 f1 g1 h1  1")
print("")
print("    a  b  c  d  e  f  g  h    ")
print("             WHITE            ")


print("")
print("made by himanshu")
print("")
print("to move black left side first pawn you need to give san code as a7a6 -> it move one step upward, to move two step you need to give san code as a7a5")
print("")
print("p->Pawn , n->Knight , b->Bishop , r->Rook , k->king  , q->queen ")
print("")
print("points -> Pawn: 1 point (or pawn) ,Knight: 3 points ,Bishop: 3 points,Rook: 5 points ,Queen: 9 points")