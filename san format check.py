import chess

board = chess.Board()

while not board.is_game_over():
    # Print the current state of the board with SAN codes
    print(board.unicode(invert_color=True))

    # Get all possible moves
    legal_moves = [move for move in board.legal_moves]

    # Check for draw by insufficient material or threefold repetition
    if board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition():
        print("Draw!")
        break

    # Check for checkmate or stalemate
    if board.is_checkmate():
        print("Checkmate! {} wins!".format("Black" if board.turn == chess.WHITE else "White"))
        break
    elif board.is_stalemate():
        print("Stalemate!")
        break

    # Print all possible moves
    for move in legal_moves:
        print(board.san(move))

    # Get user input for the move to play
    while True:
        user_input = input("Enter your move: ")
        try:
            move = chess.Move.from_uci(user_input)
            if move in legal_moves:
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

    # Make the move on the board
    board.push(move)





#SAN (Standard Algebraic Notation)