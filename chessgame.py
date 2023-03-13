import chess

# Create a new chess board
board = chess.Board()

# Play game
while not board.is_game_over():
    # Ask for the next move from White
    move = input("White's move (SAN format): ")
    
    try:
        # Push the move to the board
        board.push_san(move)
        
        # Check if the last move was a check
        if board.is_check():
            print("Check!")
        
        # Check if the black king is under attack
        if board.is_attacked_by(chess.BLACK, chess.E8):
            print("Black king is under attack!")
        
        # Check if the white bishop on c4 is attacking the black knight on f6
        if board.attackers(chess.WHITE, chess.F6):
            attacker_square = board.attackers(chess.WHITE, chess.F6).pop()
            if board.piece_at(attacker_square).symbol() == "B":
                print("White bishop on c4 is attacking the black knight on f6!")
        
        # Print the current board position
        print(board)
        print()
        
        if board.is_game_over():
            break
        
        # Ask for the next move from Black
        move = input("Black's move (SAN format): ")
        
        # Push the move to the board
        board.push_san(move)
        
        # Check if the last move was a check
        if board.is_check():
            print("Check!")
        
        # Check if the white king is under attack
        if board.is_attacked_by(chess.WHITE, chess.E1):
            print("White king is under attack!")
        
        # Check if the black bishop on c4 is attacking the white knight on f6
        if board.attackers(chess.BLACK, chess.F3):
            attacker_square = board.attackers(chess.BLACK, chess.F3).pop()
            if board.piece_at(attacker_square).symbol() == "B":
                print("Black bishop on c4 is attacking the white knight on f3!")
        
        # Print the current board position
        print(board)
        print()
        
    except ValueError:
        # If the move is invalid, ask again for the next move
        print("Invalid move, please enter a valid move in SAN format.")






# pip install chess