#Yong Da Li
#Tuesday, February 12, 2019
#Professor Nebu Mathai
#CSC190

#assignment A - chess player
#tree store board, board evaluation, white/black player, and all sub-boards

import time
from chessPlayer_board import*
from chessPlayer_lib import*
from chessPlayer_queue import*
import chessPlayer as cp

class Tree:
    #player 10 = white
    #player 20 = black
    def __init__ (self, board, val, player):
        self.board = board
        self.val = val
        self.player = player

        self.start = -1
        self.end = -1
        self.store = []


    #creates new Tree object to store state of board in node's store[]
    def add(self, board, val, player, start, end):
        temp = Tree(board, val, player)
        temp.start = start
        temp.end = end

        self.store = self.store + [temp]


    #accepts node and adds to store
    def add_node(self, node, start, end):
        temp = node
        temp.start = start
        temp.end = end

        self.store = self.store + [temp]

    #copy lists to recreate same node
    def copy(self):
        board_copy = board.copy()
        temp = Tree(board_copy, self.val, self.player)
        temp.start = self.start
        temp.end = self.end
        temp.store = temp.store.copy()

        return temp


    #calculate and add nodes for 1 level deeper, for 1 node
    #node is Tree class
    def calc_new_level(self, node):
        board = node.board.copy()
        player = node.player

        positions = cp.GetPlayerPositions(board, player)
        for start in positions:
            moves = cp.GetPieceLegalMoves(board, start)
            for move in moves:

                #start = starting position of piece
                #move = ending position of piece
                temp = board.copy()
                temp.move(start, move)
                val = temp.eval()

                #add values to node's store[]
                node.add(temp, val, 30-player, start, move)


    def calculate_tree(self, node, depth):
        if depth == 0:
            return True

        else:
            #no children, make sure there is something in node.store
            if len(node.store) == 0:
                self.calc_new_level(node)
            
            for child in node.store:
                self.calculate_tree(child, depth-1)
            

    #returns best score and associated move = [start, end]
    def minimax(self, node, depth, player):
        if depth == 0:
            next_move = [self.start, self.end]
            return [node.val, next_move]

        #white = maximizing player
        if player == 10:
            score = -999999
            for state in node.store:
                if self.minimax(state, depth-1, 30-player)[0] > score:
                    next_move = [state.start, state.end]
                score = self.max(score, self.minimax(state, depth-1, 30-player)[0])
                
            return [score, next_move]

        #black = minimizing player
        elif player == 20:
            score = 999999
            for state in node.store:
                if self.minimax(state, depth-1, 30-player)[0] < score:
                    next_move = [state.start, state.end]
                score = self.min(score, self.minimax(state, depth-1, 30-player)[0])

            return [score, next_move]


    #only returns best move
    def get_best_move(self, node, depth):
        self.calculate_tree(node, depth)
        minimax = self.minimax(node, depth, node.player)
        move = minimax[1]
        return move

    #returns best move, candidate moves, and eval tree in 3-list
    def get_move_candidateMove_evalTree(self, node, depth):
        self.calculate_tree(node, depth)
        minimax = self.minimax(node, depth, node.player)

        candidateMoves = self.get_candidate_moves(node)
        evalTree = self.get_eval_tree(node)

        move = minimax[1]

        #print("\n\tminimax stats")
        #print("minimax score:", minimax[0])
        #print("minimax move:", move[0], move[1])
                
        return [move, candidateMoves, evalTree]


    def max(self, a, b):
        if a<=b:
            return b
        else:
            return a

    def min(self, a, b):
        if a>=b:
            return b
        else:
            return a


    #returns all possible moves from this board state, and its value
    def get_candidate_moves(self, node):
        candid = []
        for child in node.store:
            move = [child.start, child.end]
            val = child.val

            move_package = [move, val]
            candid = candid + [move_package]

        return candid


    #returns all board states as integer list
    def get_eval_tree(self, node):
        eval_tree = []
        level_order = self.get_level_order(node)

        for node in level_order:

            #eval tree
            board_list = node.board.get_list()
            eval_tree = eval_tree + [board_list]

        return eval_tree


    #returns list of tree nodes of all calculated states
    def get_level_order(self, node):
        x = Queue()
        x.enqueue(node)
        traversal = []
        while x.isEmpty() == False:
            r = x.dequeue()
            traversal = traversal + [r]
            for child in r.store:
                x.enqueue(child)

        return traversal


    #accessor functions
    def get_board(self):
        return self.board

    def get_val(self):
        return self.val

    def get_player(self):
        return self.player

    def get_store(self):
        return self.store

    def print(self):
        
        print("board:")
        self.board.print()

        #board.print() already prints val
        print("player:", self.player)
        print("start:", self.start);
        print("end:", self.end)
        print("store:", self.store)