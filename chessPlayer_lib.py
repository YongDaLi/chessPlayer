#Yong Da Li
#Tuesday, February 12, 2019
#Professor Nebu Mathai
#CSC190

#assignment A - chess player
#chess move library, defines the chess game

import chessPlayer as cp

#return list of legal pawn moves
def pawnMoves(board, i):
    legal = []

    #white
    if isWhite(board, i):
        #forward 1
        if isOnBoard(i+8) and isOpen(board, i+8):
            legal = legal + [i+8]

        #take along diagonal, to piece's left

        if i%8 == 0: #special case for left border
            if isOnBoard(i+9) and isBlack(board, i+9):
                legal = legal + [i+9]

        elif i%8 < 7: #standard cases, in middle board, both left and right take
            if isOnBoard(i+7) and isBlack(board, i+7):
                legal = legal + [i+7]
            if isOnBoard(i+9) and isBlack(board, i+9):
                legal = legal + [i+9]

        elif i%8 == 7: #special case for right border
            if isOnBoard(i+7) and isBlack(board, i+7):
                legal = legal + [i+7]

    #black
    elif isBlack(board, i):
        #forward 1
        if isOnBoard(i-8) and isOpen(board, i-8):
            legal = legal + [i-8]

        #take along diagonal, to piece's left

        if i%8 == 0: #special case for left border
            if isOnBoard(i-7) and isWhite(board, i-7):
                legal = legal + [i-7]

        elif i%8 < 7: #standard cases, in middle board, both left and right take
            if isOnBoard(i-7) and isWhite(board, i-7):
                legal = legal + [i-7]
            if isOnBoard(i-9) and isWhite(board, i-9):
                legal = legal + [i-9]

        elif i%8 == 7: #special case for right border
            if isOnBoard(i-9) and isWhite(board, i-9):
                legal = legal + [i-9]

    return legal


#returns list of legal knight moves
def knightMoves(board, i):
    legal = []

    if isWhite(board, i):
        #case left border
        if i%8 == 0:
            #tall L
            if isWhiteMove(board, i-15):
                legal = legal + [i-15]
            if isWhiteMove(board, i+17):
                legal = legal + [i+17]

        #case 2nd column, 1 away from border
        elif i%8 == 1:
            #tall L
            if isWhiteMove(board, i-15):
                legal = legal + [i-15]
            if isWhiteMove(board, i+17):
                legal = legal + [i+17]
            if isWhiteMove(board, i+15):
                legal = legal + [i+15]
            if isWhiteMove(board, i-17):
                legal = legal + [i-17]

            #wide L
            if isWhiteMove(board, i-6):
                legal = legal + [i-6]
            if isWhiteMove(board, i+10):
                legal = legal + [i+10]

        #case right border
        elif i%8 == 7:
            #tall L
            if isWhiteMove(board, i-17):
                legal = legal + [i-17]
            if isWhiteMove(board, i+15):
                legal = legal + [i+15]

        #case 7th column, 1 away from right border
        elif i%8 == 6:
            #tall L
            if isWhiteMove(board, i-17):
                legal = legal + [i-17]
            if isWhiteMove(board, i+15):
                legal = legal + [i+15] 
            if isWhiteMove(board, i+17):
                legal = legal + [i+17]
            if isWhiteMove(board, i-15):
                legal = legal + [i-15] 

            #wide L
            if isWhiteMove(board, i-10):
                legal = legal + [i-10]
            if isWhiteMove(board, i+6):
                legal = legal + [i+6]

        #case middle of board, all 8 moves
        else:
            if isWhiteMove(board, i-15):
                legal = legal + [i-15]
            if isWhiteMove(board, i+15):
                legal = legal + [i+15]

            if isWhiteMove(board, i-6):
                legal = legal + [i-6]
            if isWhiteMove(board, i+6):
                legal = legal + [i+6]

            if isWhiteMove(board, i-17):
                legal = legal + [i-17]
            if isWhiteMove(board, i+17):
                legal = legal + [i+17]

            if isWhiteMove(board, i-10):
                legal = legal + [i-10]
            if isWhiteMove(board, i+10):
                legal = legal + [i+10]

    #if black knight
    elif isBlack(board, i):
        #case left border
        if i%8 == 0:
            #tall L
            if isBlackMove(board, i-15):
                legal = legal + [i-15]
            if isBlackMove(board, i+17):
                legal = legal + [i+17]

        #case 2nd column, 1 away from border
        elif i%8 == 1:
            #tall L
            if isBlackMove(board, i-15):
                legal = legal + [i-15]
            if isBlackMove(board, i+17):
                legal = legal + [i+17]
            if isBlackMove(board, i-17):
                legal = legal + [i-17]
            if isBlackMove(board, i+15):
                legal = legal + [i+15]

            #wide L
            if isBlackMove(board, i-6):
                legal = legal + [i-6]
            if isBlackMove(board, i+10):
                legal = legal + [i+10]

        #case right border
        elif i%8 == 7:
            #tall L
            if isBlackMove(board, i-17):
                legal = legal + [i-17]
            if isBlackMove(board, i+15):
                legal = legal + [i+15]

        #case 7th column, 1 away from right border
        elif i%8 == 6:
            #tall L
            if isBlackMove(board, i-17):
                legal = legal + [i-17]
            if isBlackMove(board, i+15):
                legal = legal + [i+15]
            if isBlackMove(board, i+17):
                legal = legal + [i+17]
            if isBlackMove(board, i-15):
                legal = legal + [i-15] 

            #wide L
            if isBlackMove(board, i-10):
                legal = legal + [i-10]
            if isBlackMove(board, i+6):
                legal = legal + [i+6]

        #case middle of board, all 8 moves
        else:
            if isBlackMove(board, i-15):
                legal = legal + [i-15]
            if isBlackMove(board, i+15):
                legal = legal + [i+15]

            if isBlackMove(board, i-6):
                legal = legal + [i-6]
            if isBlackMove(board, i+6):
                legal = legal + [i+6]

            if isBlackMove(board, i-17):
                legal = legal + [i-17]
            if isBlackMove(board, i+17):
                legal = legal + [i+17]

            if isBlackMove(board, i-10):
                legal = legal + [i-10]
            if isBlackMove(board, i+10):
                legal = legal + [i+10]

    return legal


#returns list of legal bishop moves
def bishopMoves(board, pos):
    legal = []

    if isWhite(board, pos):
        #check 4 diagonals, expand outward until no more moves

        # / = up to right
        i = pos
        while ( isWhiteMove(board, i-7)):
            #already on right edge
            if i%8 == 7:
                break

            legal = legal + [i-7]
            i = i - 7
            #prevent running off the borders
            #can only take 1 piece
            if i%8 == 7 or isOccupied(board, i):
                break

        # / = down to left
        i = pos
        while ( isWhiteMove(board, i+7)):
            #already on left edge
            if i%8 == 0:
                break

            legal = legal + [i+7]
            i = i + 7
            #prevent running off the borders
            #can only take 1 piece
            if i%8 == 0 or isOccupied(board, i):
                break

        # \ = up to left
        i = pos
        while ( isWhiteMove(board, i-9)):
            #already on left edge
            if i%8 == 0:
                break

            legal = legal + [i-9]
            i = i - 9
            #prevent running off the borders
            #can only take 1 piece
            if i%8 == 0 or isOccupied(board, i):
                break

        # \ = down to right
        i = pos
        while ( isWhiteMove(board, i+9)):
            #already on right edge
            if i%8 == 7:
                break

            legal = legal + [i+9]
            i = i + 9
            #prevent running off the borders
            #can only take 1 piece
            if i%8 == 7 or isOccupied(board, i):
                break

    elif isBlack(board, pos):
        #check 4 diagonals, expand outward until no more moves

        # / = up to right
        i = pos
        while ( isBlackMove(board, i-7)):
            #already on right edge
            if i%8 == 7:
                break

            legal = legal + [i-7]
            i = i - 7
            #prevent running off the borders
            #can only take 1 piece
            if i%8 == 7 or isOccupied(board, i):
                break

        # / = down to left
        i = pos
        while ( isBlackMove(board, i+7)):
            #already on left edge
            if i%8 == 0:
                break

            legal = legal + [i+7]
            i = i + 7
            #prevent running off the borders
            #can only take 1 piece
            if i%8 == 0 or isOccupied(board, i):
                break

        # \ = up to left
        i = pos
        while ( isBlackMove(board, i-9)):
            #already on left edge
            if i%8 == 0:
                break

            legal = legal + [i-9]
            i = i - 9
            #prevent running off the borders
            #can only take 1 piece
            if i%8 == 0 or isOccupied(board, i):
                break

        # \ = down to right
        i = pos
        while ( isBlackMove(board, i+9)):
            #already on right edge
            if i%8 == 7:
                break
                
            legal = legal + [i+9]
            i = i + 9
            #prevent running off the borders
            #can only take 1 piece
            if i%8 == 7 or isOccupied(board, i):
                break


    return legal


#returns list of legal rook moves
def rookMoves(board, pos):
    legal = []

    if isWhite(board, pos):
        #check 4 directions, expand out from i until no more moves

        # --> = to right
        i = pos
        while ( isWhiteMove(board, i+1) and i%8 !=7):
            legal = legal + [i+1]
            i = i + 1
            #prevent running off the side, looping around
            #can only take 1 piece
            if i%8 == 7 or isOccupied(board, i):
                break

        # <-- = to left
        i = pos
        while ( isWhiteMove(board, i-1) and i%8 != 0):
            legal = legal + [i-1]
            i = i - 1
            #prevent running off the side, looping around
            #can only take 1 piece
            if i%8 == 0 or isOccupied(board, i):
                break

        #no need to worry about looping around for top/bottom

        # ^ = upward
        i = pos
        while ( isWhiteMove(board, i-8)):
            legal = legal + [i-8]
            i = i - 8
            #can only take 1 piece
            if isOccupied(board, i):
                break

        # downward
        i = pos
        while ( isWhiteMove(board, i+8)):
            legal = legal + [i+8]
            i = i + 8
            #can only take 1 piece
            if isOccupied(board, i):
                break

    
    elif isBlack(board, pos):
        #check 4 directions, expand out from i until no more moves

        # --> = to right
        i = pos
        while ( isBlackMove(board, i+1) and i%8 !=7):
            legal = legal + [i+1]
            i = i + 1
            #prevent running off the side, looping around
            #can only take 1 piece
            if i%8 == 7 or isOccupied(board, i):
                break

        # <-- = to left
        i = pos
        while ( isBlackMove(board, i-1) and i%8 != 0):
            legal = legal + [i-1]
            i = i - 1
            #prevent running off the side, looping around
            #can only take 1 piece
            if i%8 == 0 or isOccupied(board, i):
                break

        #no need to worry about looping around for top/bottom

        # ^ = upward
        i = pos
        while ( isBlackMove(board, i-8)):
            legal = legal + [i-8]
            i = i - 8
            #can only take 1 piece
            if isOccupied(board, i):
                break

        # downward
        i = pos
        while ( isBlackMove(board, i+8)):
            legal = legal + [i+8]
            i = i + 8
            #can only take 1 piece
            if isOccupied(board, i):
                break

    return legal


#returns list of legal queen moves
def queenMoves(board, i):
    legal = []

    legal = bishopMoves(board, i) + rookMoves(board, i)

    return legal


#returns list of legal king moves
#assume king can go into position that's under threat
def kingMoves(board, i):
    legal = []

    if isWhite(board, i):
        #case 1, top left corner
        if i == 0:
            if isWhiteMove(board, 1):
                legal = legal + [1]
            if isWhiteMove(board, 8):
                legal = legal + [8]
            if isWhiteMove(board, 9):
                legal = legal + [8]

        #case 2, top right corner
        elif i == 7:
            if isWhiteMove(board, 4):
                legal = legal + [4]
            if isWhiteMove(board, 14):
                legal = legal + [14]
            if isWhiteMove(board, 15):
                legal = legal + [15]

        #case 3, bottom left corner
        elif i == 56:
            if isWhiteMove(board, 48):
                legal = legal + [48]
            if isWhiteMove(board, 49):
                legal = legal + [49]
            if isWhiteMove(board, 57):
                legal = legal + [57]

        #case 4, bottom right corner
        elif i == 63:
            if isWhiteMove(board, 55):
                legal = legal + [55]
            if isWhiteMove(board, 54):
                legal = legal + [54]
            if isWhiteMove(board, 62):
                legal = legal + [62]

        #case 5, top side
        elif i<7:
            if isWhiteMove(board, i-1):
                legal = legal + [i-1]
            if isWhiteMove(board, i+1):
                legal = legal + [i+1]
            if isWhiteMove(board, i+7):
                legal = legal + [i+7]
            if isWhiteMove(board, i+8):
                legal = legal + [i+8]
            if isWhiteMove(board, i+9):
                legal = legal + [i+9]

        #case 6, left side
        elif i%8 == 0:
            if isWhiteMove(board, i-8):
                legal = legal + [i-8]
            if isWhiteMove(board, i-7):
                legal = legal + [i-7]
            if isWhiteMove(board, i+1):
                legal = legal + [i+1]
            if isWhiteMove(board, i + 8):
                legal = legal + [i+8]
            if isWhiteMove(board, i + 9):
                legal = legal + [i+9]

        #case 7, right side
        elif i%8 == 7:
            if isWhiteMove(board, i-8):
                legal = legal + [i-8]
            if isWhiteMove(board, i-9):
                legal = legal + [i-9]
            if isWhiteMove(board, i-1):
                legal = legal + [i-1]
            if isWhiteMove(board, i + 8):
                legal = legal + [i+8]
            if isWhiteMove(board, i + 7):
                legal = legal + [i+7]

        #case 8, bottom side
        elif i>56:
            if isWhiteMove(board, i-1):
                legal = legal + [i-1]
            if isWhiteMove(board, i+1):
                legal = legal + [i+1]
            if isWhiteMove(board, i-7):
                legal = legal + [i-7]
            if isWhiteMove(board, i-8):
                legal = legal + [i-8]
            if isWhiteMove(board, i-9):
                legal = legal + [i-9]

        #case 9, middle
        else:
            if isWhiteMove(board, i-9):
                legal = legal + [i-9]
            if isWhiteMove(board, i-8):
                legal = legal + [i-8]
            if isWhiteMove(board, i-7):
                legal = legal + [i-7]
            if isWhiteMove(board, i-1):
                legal = legal + [i-1]
            if isWhiteMove(board, i+1):
                legal = legal + [i+1]
            if isWhiteMove(board, i+7):
                legal = legal + [i+7]
            if isWhiteMove(board, i+8):
                legal = legal + [i+8]
            if isWhiteMove(board, i+9):
                legal = legal + [i+9]


    elif isBlack(board, i):
        #case 1, top left corner
        if i == 0:
            if isBlackMove(board, 1):
                legal = legal + [1]
            if isBlackMove(board, 8):
                legal = legal + [8]
            if isBlackMove(board, 9):
                legal = legal + [8]

        #case 2, top right corner
        elif i == 7:
            if isBlackMove(board, 4):
                legal = legal + [4]
            if isBlackMove(board, 14):
                legal = legal + [14]
            if isBlackMove(board, 15):
                legal = legal + [15]

        #case 3, bottom left corner
        elif i == 56:
            if isBlackMove(board, 48):
                legal = legal + [48]
            if isBlackMove(board, 49):
                legal = legal + [49]
            if isBlackMove(board, 57):
                legal = legal + [57]

        #case 4, bottom right corner
        elif i == 63:
            if isBlackMove(board, 55):
                legal = legal + [55]
            if isBlackMove(board, 54):
                legal = legal + [54]
            if isBlackMove(board, 62):
                legal = legal + [62]

        #case 5, top side
        elif i<7:
            if isBlackMove(board, i-1):
                legal = legal + [i-1]
            if isBlackMove(board, i+1):
                legal = legal + [i+1]
            if isBlackMove(board, i+7):
                legal = legal + [i+7]
            if isBlackMove(board, i+8):
                legal = legal + [i+8]
            if isBlackMove(board, i+9):
                legal = legal + [i+9]

        #case 6, left side
        elif i%8 == 0:
            if isBlackMove(board, i-8):
                legal = legal + [i-8]
            if isBlackMove(board, i-7):
                legal = legal + [i-7]
            if isBlackMove(board, i+1):
                legal = legal + [i+1]
            if isBlackMove(board, i + 8):
                legal = legal + [i+8]
            if isBlackMove(board, i + 9):
                legal = legal + [i+9]

        #case 7, right side
        elif i%8 == 7:
            if isBlackMove(board, i-8):
                legal = legal + [i-8]
            if isBlackMove(board, i-9):
                legal = legal + [i-9]
            if isBlackMove(board, i-1):
                legal = legal + [i-1]
            if isBlackMove(board, i + 8):
                legal = legal + [i+8]
            if isBlackMove(board, i + 7):
                legal = legal + [i+7]

        #case 8, bottom side
        elif i>56:
            if isBlackMove(board, i-1):
                legal = legal + [i-1]
            if isBlackMove(board, i+1):
                legal = legal + [i+1]
            if isBlackMove(board, i-7):
                legal = legal + [i-7]
            if isBlackMove(board, i-8):
                legal = legal + [i-8]
            if isBlackMove(board, i-9):
                legal = legal + [i-9]

        #case 9, middle
        else:
            if isBlackMove(board, i-9):
                legal = legal + [i-9]
            if isBlackMove(board, i-8):
                legal = legal + [i-8]
            if isBlackMove(board, i-7):
                legal = legal + [i-7]
            if isBlackMove(board, i-1):
                legal = legal + [i-1]
            if isBlackMove(board, i+1):
                legal = legal + [i+1]
            if isBlackMove(board, i+7):
                legal = legal + [i+7]
            if isBlackMove(board, i+8):
                legal = legal + [i+8]
            if isBlackMove(board, i+9):
                legal = legal + [i+9]

    return legal


#using previously defined functions
def isPositionUnderThreat(board, pos, player):
    opp = 30-player
    threat = False

    #get all opponent positions, except for pawns
    all_opp_pos = cp.GetPlayerPositions_noPawns(board, opp)

    #find all legal moves of opponent
    legal_moves = []
    for opp_pos in all_opp_pos:
        legal_moves = legal_moves + cp.GetPieceLegalMoves(board, opp_pos)

    #if opponent can go to pos, then threat is true
    for move in legal_moves:
        if move == pos:
            threat = True
            return threat

    #special case for pawns, since they take different from normal forward movement
    pawn_moves = []
    for opp_pos in all_opp_pos:
        #find all the pawn positions
        if opp_pos == opp:
            move = cp.GetPieceLegalMoves(board, opp_pos)
            #only add if it's a diagonal taking move
            if abs(move-pos) != 8:
                pawn_moves = pawn_moves + move

    #check for pawn threat
    for move in pawn_moves:
        if move == pos:
            threat = True
            return threat


    return threat


#returns true if king is in check and position of king
def isInCheck(board, player):
    #setup king piece
    king_piece = player + 5
    king_pos = 0

    board_list = board.get_list()

    #find king
    for i in board_list:
        if i == king_piece:
            king_pos = i

    check = isPositionUnderThreat(board, king_pos, player)
    return [check, king_pos]


#returns true if player is checkmated
def isCheckmated(board, player):
    #king is in check
    check = False #default false
    check = isInCheck(board, player) [0]
    king_pos = isInCheck(board, player) [1]

    #king has no moves
    no_moves = False #default false

    moves = kingMoves(board, king_pos)
    if len(moves) == 0:
        no_moves = True

    #king is in check and has no moves
    if check and no_moves:
        return True
    else:
        return False


#returns true if player is stalemated
def isStalemated(board, player):
    #king is in check
    check = False #default false
    check = isInCheck(board, player)[0]

    #player has no legal moves
    no_moves = False #default false
    moves = []

    #find all legal moves
    positions = cp.GetPlayerPositions(board, player)
    for pos in positions:
        moves = moves + cp.GetPieceLegalMoves(board, pos)

    #if no legal moves
    if len(moves) == 0:
        no_moves = True

    #king is not in check, but player has no moves
    if check == False and no_moves == True:
        return True
    else:
        return False


#returns true if valid move, still on board
def isOnBoard(i):
    if i < 64 and i>-1:
        return True
    else:
        return False


#returns true if iition is unoccupied
def isOpen(board, i):
    if board.get(i) == 0:
        return True
    else:
        return False


#returns true if iition is occupied
def isOccupied(board, i):
    return not isOpen(board, i)


#returns true if white piece
#returns false if black or unoccupied
def isWhite(board, i):
    if board.get(i) < 20 and board.get(i)>0:
        return True
    else:
        return False


#returns true if black piece
#returns false if white or unoccupied
def isBlack(board, i):
    if board.get(i) >= 20:
        return True
    else:
        return False


#returns true if white can go or take there
def isWhiteMove(board, i):
    if isOnBoard(i):
        if isBlack(board, i) or isOpen(board, i):
            return True
    else:
        return False


#returns true if black can go or take there
def isBlackMove(board, i):
    if isOnBoard(i):
        if isWhite(board, i) or isOpen(board, i):
            return True
    else:
        return False
