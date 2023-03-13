import chess

board = chess.Board()

while not board.is_game_over():
   
    print(board.unicode(invert_color=True))

  
    legal_moves = [move for move in board.legal_moves]

    # himanshu
    if board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition():
        print("Draw!")
        break

   
    if board.is_checkmate():
        print("Checkmate! {} wins!".format("Black" if board.turn == chess.WHITE else "White"))
        break
    elif board.is_stalemate():
        print("Stalemate!")
        break

   
    for move in legal_moves:
        print(board.san(move))

    while True:
        user_input = input("(made by himzo)Enter your move: ")
        try:
            move = chess.Move.from_uci(user_input)
            if move in legal_moves:
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

  
    board.push(move)





