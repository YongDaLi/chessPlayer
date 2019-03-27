#returns true if position is under threat
#player 10 = white
#player 20 = black
def isPositionUnderThreat_long(board, pos, player):
    #pos can be threatened by pawn, knight, bishop, rook, (queen, king -> already accounted for)
    threat = False

    #white
    if player == 10:

        #case 1, left border
        if pos%8 == 0:
            #pawn
            if isOnBoard(pos+9) and board.get(pos+9) == 20:
                threat = True 
                return threat

            #knight
            #up tall L
            elif isOnBoard(pos-15) and board.get(pos-15) == 21:
                threat = True 
                return threat

            #up wide L
            elif isOnBoard(pos-6) and board.get(pos-6) == 21:
                threat = True 
                return threat

            #down wide L
            elif isOnBoard(pos+10) and board.get(pos+10) == 21:
                threat = True 
                return threat

            #down tall L
            elif isOnBoard(pos+17) and board.get(pos+17) == 21:
                threat = True 
                return threat


        #case 2, right border
        if pos%8 == 7:
            #pawn
            if isOnBoard(pos+7) and board.get(pos+7) == 20:
                threat = True 
                return threat

            #knight
            #up tall L
            elif isOnBoard(pos-17) and board.get(pos-17) == 21:
                threat = True 
                return threat

            #up wide L
            elif isOnBoard(pos-10) and board.get(pos-10) == 21:
                threat = True 
                return threat

            #down wide L
            elif isOnBoard(pos+6) and board.get(pos+6) == 21:
                threat = True 
                return threat

            #down tall L
            elif isOnBoard(pos+15) and board.get(pos+15) == 21:
                threat = True 
                return threat

        #case 3, middle of board
        else:
            if isOnBoard(pos+7) and board.get(pos+7) == 20:
                threat = True 
                return threat

            elif isOnBoard(pos+9) and board.get(pos+9) == 20:
                threat = True 
                return threat

            #knight
            #to right
            #up tall L
            elif isOnBoard(pos-15) and board.get(pos-15) == 21:
                threat = True 
                return threat

            #up wide L
            elif isOnBoard(pos-6) and board.get(pos-6) == 21:
                threat = True 
                return threat

            #down wide L
            elif isOnBoard(pos+10) and board.get(pos+10) == 21:
                threat = True 
                return threat

            #down tall L
            elif isOnBoard(pos+17) and board.get(pos+17) == 21:
                threat = True 
                return threat

            #to left
            #up tall L
            elif isOnBoard(pos-17) and board.get(pos-17) == 21:
                threat = True 
                return threat

            #up wide L
            elif isOnBoard(pos-10) and board.get(pos-10) == 21:
                threat = True 
                return threat

            #down wide L
            elif isOnBoard(pos+6) and board.get(pos+6) == 21:
                threat = True 
                return threat

            #down tall L
            elif isOnBoard(pos+15) and board.get(pos+15) == 21:
                threat = True 
                return threat

        #bishop
        # / = up to right
        i = pos
        while isOnBoard(i-7):
            if board.get(i-7) == 22:
                threat = True 
                return threat
            if isOccupied(board, i-7) or pos%8 == 7:
                break
            i = i -7

        # \ = down to right
        i = pos
        while isOnBoard(i+10):
            if board.get(i+10) == 22:
                threat = True 
                return threat
            if isOccupied(board, i+10) or pos%8 == 7:
                break
            i = i + 10

        # \ = up to left
        i = pos
        while isOnBoard(i-9):
            if board.get(i-9) == 22:
                threat = True 
                return threat
            if isOccupied(board, i-9) or pos%8 == 0:
                break
            i = i - 9

        # / = down to left
        i = pos
        while isOnBoard(i+7):
            if board.get(i+7) == 22:
                threat = True 
                return threat
            if isOccupied(board, i+7) or pos%8 == 0:
                break
            i = i + 7

        #rook
        #up
        i = pos
        while isOnBoard(i-8):
            if board.get(i-8) == 23:
                threat = True 
                return threat
            if isOccupied(board, i-8):
                break
            i = i - 8

        #down
        i = pos
        while isOnBoard(i+8):
            if board.get(i+8) == 23:
                threat = True 
                return threat
            if isOccupied(board, i+8):
                break
            i = i + 8

        # <-- = to left, prevent looping around
        i = pos
        while isOnBoard(i-1) and pos%8 != 0:
            if board.get(i-1) == 23:
                threat = True 
                return threat
            if isOccupied(board, i-1):
                break
            i = i - 1

        # --> = to right, prevent looping around
        i = pos
        while isOnBoard(i+1) and pos%8 != 7:
            if board.get(i+1) == 23:
                threat = True 
                return threat
            if isOccupied(board, i+1):
                break
            i = i + 1

        #queen and king
        queenPos = 0
        kingPos = 0

        #find position
        for i in range (0, 64):
            if board.get(i) == 24:
                queenPos = i
            if board.get(i) == 25:
                kingPos = i

        #find their legal moves
        kingRange = kingMoves(board, kingPos)
        queenRange = queenMoves(board, queenPos)

        #if pos is in legal moves of King and Queen, threat is true
        totalRange = kingRange + queenRange
        for i in totalRange:
            if pos == i:
                threat = True 
                return threat

    #black
    elif player == 20:

        #case 1, left border
        if pos%8 == 0:
            #pawn
            if isOnBoard(pos-7) and board.get(pos-7) == 10:
                threat = True 
                return threat

            #knight
            #up tall L
            elif isOnBoard(pos-15) and board.get(pos-15) == 11:
                threat = True 
                return threat

            #up wide L
            elif isOnBoard(pos-6) and board.get(pos-6) == 11:
                threat = True 
                return threat

            #down wide L
            elif isOnBoard(pos+10) and board.get(pos+10) == 11:
                threat = True 
                return threat

            #down tall L
            elif isOnBoard(pos+17) and board.get(pos+17) == 11:
                threat = True 
                return threat


        #case 2, right border
        if pos%8 == 7:
            #pawn
            if isOnBoard(pos-9) and board.get(pos-9) == 10:
                threat = True 
                return threat

            #knight
            #up tall L
            elif isOnBoard(pos-17) and board.get(pos-17) == 11:
                threat = True 
                return threat

            #up wide L
            elif isOnBoard(pos-10) and board.get(pos-10) == 11:
                threat = True 
                return threat

            #down wide L
            elif isOnBoard(pos+6) and board.get(pos+6) == 11:
                threat = True 
                return threat

            #down tall L
            elif isOnBoard(pos+15) and board.get(pos+15) == 11:
                threat = True 
                return threat

        #case 3, middle of board
        else:
            if isOnBoard(pos-7) and board.get(pos-7) == 10:
                threat = True 
                return threat

            elif isOnBoard(pos-9) and board.get(pos-9) == 10:
                threat = True 
                return threat

            #knight
            #to right
            #up tall L
            elif isOnBoard(pos-15) and board.get(pos-15) == 11:
                threat = True 
                return threat

            #up wide L
            elif isOnBoard(pos-6) and board.get(pos-6) == 11:
                threat = True 
                return threat

            #down wide L
            elif isOnBoard(pos+10) and board.get(pos+10) == 11:
                threat = True 
                return threat

            #down tall L
            elif isOnBoard(pos+17) and board.get(pos+17) == 11:
                threat = True 
                return threat

            #to left
            #up tall L
            elif isOnBoard(pos-17) and board.get(pos-17) == 11:
                threat = True 
                return threat

            #up wide L
            elif isOnBoard(pos-10) and board.get(pos-10) == 11:
                threat = True 
                return threat

            #down wide L
            elif isOnBoard(pos+6) and board.get(pos+6) == 11:
                threat = True 
                return threat

            #down tall L
            elif isOnBoard(pos+15) and board.get(pos+15) == 11:
                threat = True 
                return threat

        #bishop
        # / = up to right
        i = pos
        while isOnBoard(i-7):
            if board.get(i-7) == 12:
                threat = True 
                return threat
            if isOccupied(board, i-7) or pos%8 == 7:
                break
            i = i -7

        # \ = down to right
        i = pos
        while isOnBoard(i+10):
            if board.get(i+10) == 12:
                threat = True 
                return threat
            if isOccupied(board, i+10) or pos%8 == 7:
                break
            i = i + 10

        # \ = up to left
        i = pos
        while isOnBoard(i-9):
            if board.get(i-9) == 12:
                threat = True 
                return threat
            if isOccupied(board, i-9) or pos%8 == 0:
                break
            i = i - 9

        # / = down to left
        i = pos
        while isOnBoard(i+7):
            if board.get(i+7) == 12:
                threat = True 
                return threat
            if isOccupied(board, i+7) or pos%8 == 0:
                break
            i = i + 7

        #rook
        #up
        i = pos
        while isOnBoard(i-8):
            if board.get(i-8) == 13:
                threat = True 
                return threat
            if isOccupied(board, i-8):
                break
            i = i - 8

        #down
        i = pos
        while isOnBoard(i+8):
            if board.get(i+8) == 13:
                threat = True 
                return threat
            if isOccupied(board, i+8):
                break
            i = i + 8

        # <-- = to left, prevent looping around
        i = pos
        while isOnBoard(i-1) and pos%8 != 0:
            if board.get(i-1) == 13:
                threat = True 
                return threat
            if isOccupied(board, i-1):
                break
            i = i - 1

        # --> = to right, prevent looping around
        i = pos
        while isOnBoard(i+1) and pos%8 != 7:
            if board.get(i+1) == 13:
                threat = True 
                return threat
            if isOccupied(board, i+1):
                break
            i = i + 1

        #queen and king
        queenPos = 0
        kingPos = 0

        #find white king and queen position
        for i in range (0, 64):
            if board.get(i) == 14:
                queenPos = i
            if board.get(i) == 15:
                kingPos = i

        #find their legal moves
        kingRange = kingMoves(board, kingPos)
        queenRange = queenMoves(board, queenPos)

        #if pos is in legal moves of King and Queen, threat is true
        totalRange = kingRange + queenRange
        for i in totalRange:
            if pos == i:
                threat = True 
                return threat
   
    return threat