import chess


board = chess.Board()


while not board.is_game_over():
    
    move = input("White's move (SAN format): ")
    
    try:
        
        board.push_san(move)
        
        if board.is_check():
            print("Check!")
        
        # himanshu
        if board.is_attacked_by(chess.BLACK, chess.E8):
            print("Black king is under attack!(himanshu)")
        
       
        if board.attackers(chess.WHITE, chess.F6):
            attacker_square = board.attackers(chess.WHITE, chess.F6).pop()
            if board.piece_at(attacker_square).symbol() == "B":
                print("White bishop on c4 is attacking the black knight on f6!")
        
        
        print(board)
        print()
        
        if board.is_game_over():
            break
        
       
        move = input("Black's move (SAN format): ")
        
        board.push_san(move)
        

        if board.is_check():
            print("Check!")
        
    
        if board.is_attacked_by(chess.WHITE, chess.E1):
            print("White king is under attack!(himanshu)")
        
   
        if board.attackers(chess.BLACK, chess.F3):
            attacker_square = board.attackers(chess.BLACK, chess.F3).pop()
            if board.piece_at(attacker_square).symbol() == "B":
                print("Black bishop on c4 is attacking the white knight on f3!")
        
   
        print(board)
        print()
        
    except ValueError:
       
        print("Invalid move, please enter a valid move in SAN format.")






