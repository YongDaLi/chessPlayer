#Yong Da Li
#Tuesday, February 12, 2019
#Professor Nebu Mathai
#CSC190

#assignment A - chess player
#chess player functions
#   functions required by Prof. Mathai and computer decision making functions

import random
from chessPlayer_tree import*
from chessPlayer_board import*
from chessPlayer_lib import *


#returns data for grading
#[status, move, candidateMoves, evalTree]
# note: board argument is an integer list
def chessPlayer(board_list, player):
    depth = 3

    board = Board()
    board.set(board_list)

    status = True

    val = board.eval()
    root = Tree(board, val, player)
    move_candidateMoves_evalTree = root.get_move_candidateMove_evalTree(root, depth)

    move = move_candidateMoves_evalTree[0]
    candidateMoves = move_candidateMoves_evalTree[1]
    evalTree = move_candidateMoves_evalTree[2]

    #print("status:", status)")
    #print("move:", move)
    #print("candidate moves:", candidateMoves)
    #print("evalTree:", evalTree)
    #print("return:",[status, move, candidateMoves, evalTree])

    return [status, move, candidateMoves, evalTree]


#return list of positions that the player occupies
#player 10 = white
#player 20 = black
def GetPlayerPositions(board, player):
    rval = []
    if player == 10:
        for i in range (0, 64):
            if board.get(i)>0 and board.get(i)<20:
                rval = rval + [i]

    elif player == 20:
        for i in range (0, 64):
            if board.get(i)>=20:
                rval = rval + [i]

    return rval


#returns list of positions, excluding pawns
#player 10 = white
#player 20 = black
def GetPlayerPositions_noPawns(board, player):
    rval = []
    if player == 10:
        for i in range (0, 64):
            if board.get(i)>10 and board.get(i)<20:
                rval = rval + [i]

    elif player == 20:
        for i in range (0, 64):
            if board.get(i)>20:
                rval = rval + [i]

    return rval


#return all legal moves of the piece
#pawn, knight, bishop, rook, queen, king
def GetPieceLegalMoves(board, pos):
    legal = []
    piece = board.get(pos)%10

    #pawn
    if piece == 0:
        legal = pawnMoves(board, pos)

    #knight
    elif piece == 1:
        legal = knightMoves(board, pos)

    #bishop
    elif piece == 2:
        legal = bishopMoves(board, pos)

    #rook
    elif piece == 3:
        legal = rookMoves(board, pos)

    #queen
    elif piece == 4:
        legal = queenMoves(board, pos)

    #king
    elif piece == 5:
        legal = kingMoves(board, pos)

    return legal


#internal function
#converts "e4" move to index in list
def convert_input(move):
    letter = move[0]
    letter_switch = {
    "a": 7,
    "b": 6,
    "c": 5,
    "d": 4,
    "e": 3,
    "f": 2,
    "g": 1,
    "h": 0
    }

    num = int(move[1]) - 1

    return letter_switch[letter] + num * 8


#internal function
#converts index in list to "e4"
def convert_output(pos):
    letter = pos%8
    num = pos//8 + 1
    letter_switch = {
    0: "h",
    1: "g",
    2: "f",
    3: "e",
    4: "d",
    5: "c",
    6: "b",
    7: "a"
    }

    output = letter_switch[letter] + str(num)
    return output


#internal function
#requests move from user and updates board
def user_move(board):
    start = input("starting:\t")
    end = input("ending:\t\t")

    start = convert_input(start)
    end = convert_input(end)

    board.move(start, end)


#internal function
#requests move from user and updates board, only allows legal mvoes
def legal_user_move(board):
    legal = False
    while (legal == False):
        start = input("starting:\t")
        end = input("ending:\t\t")

        start = convert_input(start)
        end = convert_input(end)

        #end is valid legal move
        legal_pos = GetPieceLegalMoves(board, start)
        for i in legal_pos:
            if i == end:
                legal = True
        
        if (legal == False):
            print("\nMove is invalid, try again.\n")

    board.move(start, end)


#internal function
#requests position to evaluate legal moves
def print_legal_moves(board):
    pos = input("legal moves pos:\t")
    pos = convert_input(pos)

    legal_pos = GetPieceLegalMoves(board, pos)
    output = []
    for i in legal_pos:
        output.append(convert_output(i))

    print("legal moves:\t", legal_pos)
    print("legal moves:\t", output)


#internal funciton
#requests a position to display if the position is under threat
def print_is_pos_under_threat(board):
    pos = input("Threatned position: ")
    pos = convert_input(pos)

    player = input("player (10-white, 20-black): ")
    player = int(player)

    threat = isPositionUnderThreat(board, pos, player)

    print("threat: \t", threat)


#internal function
#driver for computer moving randomly
def random_computer_move(board):
    start = 0
    end = 0
    legal = []

    #computer is black
    pieces = GetPlayerPositions(board, 20)

    while len(legal) == 0:
        start = pieces[random.randint(0, len(pieces)-1)]
        legal = GetPieceLegalMoves(board, start)

    end = legal[random.randint(0, len(legal)-1)]

    board.move(start, end)

    start = convert_output(start)
    end = convert_output(end)
    print("computer move:\t", start, " --> ", end)


#internal function
#driver for minimax computer move, player is  black
def computer_move(board):
    player = 20
    depth = 3
    val = board.eval()

    root = Tree(board, val, player)
    move = root.get_best_move(root, depth)

    start = move[0]
    end = move[1]
    board.move(start,end)

    start = convert_output(start)
    end = convert_output(end)
    print("computer move:\t", start, " --> ", end)

    return True


#internal function
#displays check, stalemate, and checkmake
def display_status(board, player):
    #check returns [check (t/f), position of king]
    check = isInCheck(board, player) [0]
    stalemated = isStalemated(board, player)
    checkmated = isCheckmated(board, player)

    if player == 10:
        player = "White"
    elif player == 20:
        player = "Black"

    if check:
        print(player, "in check!")
    if stalemated:
        print("Game over: stalemate")
    if checkmated:
        print("Game over:", player, "is checkmated" )
