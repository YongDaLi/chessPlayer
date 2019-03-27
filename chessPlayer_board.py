#Yong Da Li
#Tuesday, February 12, 2019
#Professor Nebu Mathai
#CSC190

#assignment A - chess player
#board class, responsible for visual interface and updating board

'''
WP      white pawn
WN      white knight
WB      white bishop
WR      white rook
WQ      white queen
WK      white king

BP      black pawn
BN      black knight
BB      black bishop
BR      black rook
BQ      black queen
BK      black king
'''

from chessPlayer import*


class Board:
    def __init__ (self):
        self.state = [  
        13, 11, 12, 15, 14, 12, 11, 13,
        10, 10, 10, 10, 10, 10, 10, 10,
        0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,
        20, 20, 20, 20, 20, 20, 20, 20,
        23, 21, 22, 25, 24, 22, 21, 23
        ]

    #returns value at index
    def get(self, i):
        return self.state[i]


    #returns board as a integer list
    def get_list(self):
        temp_list = self.state.copy()
        return temp_list


    #accepts integer list and sets the board equal to that list
    def set(self, board_list):
        #set it to a copy of the original list data type
        temp_list = board_list.copy()
        self.state = temp_list
        return True


    #returns duplicate board, not using pointers to list
    def copy(self):
        copy = Board()
        copy.state = self.state.copy()
        return copy


    #used for displaying board
    def convert_to_piece (self, num):
        switch = {
            0: "  ",

            10: "WP",
            11: "WN",
            12: "WB",
            13: "WR",
            14: "WQ",
            15: "WK",

            20: "BP",
            21: "BN",
            22: "BB",
            23: "BR",
            24: "BQ",
            25: "BK",
            }
        return switch [num]


    #display the board in a grid, with alphaumeric axis
    def print(self):
        j = 0
        row = 1
        line = str(row) + "* | "
        for i in self.state:
            line = line + self.convert_to_piece(i) + " | "

            j = j + 1;

            if j%8 == 0:
                row = row + 1
                print(line)
                print(" * " + "-"*41);
                line = str(row) + "* | "

        print(" "*3 + "* H  * G  * F  * E  * D  * C  * B  * A  *")
        print("val:", self.eval())


    #returns value of piece
    def get_piece_value(self, num):
        switch = {
            0: 0,

            10: 10,
            11: 30,
            12: 30,
            13: 50,
            14: 90,
            15: 900,

            20: -10,
            21: -30,
            22: -30,
            23: -50,
            24: -90,
            25: -900
        }
        return switch[num]


    #returns value of piece in a certain position
    def get_pos_value (self, i):
        pawnEvalBlack = [
            0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
            5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
            1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
            0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
            0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
            0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
            0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
            0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0
        ]

        knightEval = [
            -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
            -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
            -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
            -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
            -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
            -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
            -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
            -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0
        ]

        bishopEvalBlack = [
             -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
             -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
             -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
             -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
             -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
             -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
             -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
             -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0
        ]

        rookEvalBlack = [
              0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
              0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
             -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
             -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
             -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
             -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
             -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
              0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0
        ]

        evalQueen =[
             -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
             -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
             -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
             -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
              0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
             -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
             -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
             -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0
        ]

        kingEvalBlack = [
             -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
             -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
             -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
             -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
             -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
             -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
              2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
              2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 
        ]

        pawnEvalWhite = pawnEvalBlack[::-1]
        bishopEvalWhite = bishopEvalBlack[::-1]
        rookEvalWhite = rookEvalBlack[::-1]
        kingEvalWhite = kingEvalBlack[::-1]

        piece = self.state[i]

        #white pawn
        if piece == 10:
            return pawnEvalWhite[i]

        #black pawn
        elif piece == 20:
            return -pawnEvalBlack[i]

        #white knight
        elif piece == 11:
            return knightEval[i]

        #black knight
        elif piece == 21:
            return -knightEval[i]

        #white bishop
        elif piece == 12:
            return bishopEvalWhite[i]

        #black bishop
        elif piece == 22:
            return -bishopEvalBlack[i]

        #white rook
        elif piece == 13:
            return rookEvalWhite[i]

        #black rook
        elif piece == 23:
            return -rookEvalBlack[i]

        #white queen
        elif piece == 14:
            return evalQueen[i]

        #black queen
        elif piece == 24:
            return -evalQueen[i]

        #white king
        elif piece == 15:
            return kingEvalWhite[i]

        #black king
        elif piece == 25:
            return -kingEvalBlack[i]

        else:
            return 0


    def eval(self):
        score = 0
        for i in range (0, len(self.state)):
            score = score + self.get_piece_value(self.state[i])
            score = score + self.get_pos_value(i)

        return score


    def move(self, start, end):
        if start<64 and start > -1 and end<64 and end > -1:
            if start == end:
                return
            else:
                self.state[end] = self.state[start]
                self.state[start] = 0