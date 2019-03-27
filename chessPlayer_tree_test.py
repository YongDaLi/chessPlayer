#Yong Da Li
#Saturday, March 2, 2019
#Professor Nebu Mathai
#CSC190

#assignment A - chess player
#test file for decision making tree

from chessPlayer_tree import *
from chessPlayer_board import *

#create Tree node
def test1():
	board = Board()
	val = board.eval()
	player = 10

	root = Tree(board, val, 10)
	root.print()


#adding other nodes
def test2():
	board = Board()
	val = board.eval()
	player = 10
	root = Tree(board, val, player)

	start = 1
	end = 34

	new_board = Board()
	new_board.move(start, end)
	new_val = new_board.eval()
	new_player = 20
	child = Tree(new_board, new_val, new_player)

	root.add_node(child, start, end)

	print("\n*******root******\n")
	root.print()
	print("\n*******children******\n")
	child.print()


#calculating new level
def test3():
	board = Board()
	val = board.eval()
	player = 10
	root = Tree(board, val, player)

	root.calc_new_level(root)

	print("\n*******root******\n")
	root.print()

	print("\n*******children******\n")
	for child in root.store:
		child.print()


#calculating tree of specified depth
def test4():
	board = Board()
	val = board.eval()
	player = 10
	root = Tree(board, val, player)

	root.calculate_tree(root, 2)

	print("\n*******root******\n")
	root.print()

	print("\n*******children******\n")
	for child in root.store:
		child.print()

	print("\n*******sub-children******\n")
	for child in root.store:
		for subchild in child.store:
			subchild.print()


#check correct return value of minimax
def test5():
	board = Board()
	val = board.eval()
	player = 10
	root = Tree(board, val, player)

	root.calculate_tree(root, 2)

	print("\n*******root******\n")
	root.print()

	print("\n*******children******\n")
	for child in root.store:
		child.print()

	print("\n*******sub-children******\n")
	for child in root.store:
		for subchild in child.store:
			subchild.print()

	print("\n********end of boards*******\n")

	minimax = root.minimax(root, 2, player)
	print("max score:", minimax[0])


#does it return a legit move
def test6():
	board = Board()
	val = board.eval()
	player = 20
	root = Tree(board, val, player)

	print("\n*******root******\n")
	root.print()

	move = root.get_best_move(root, 1)

	print("******best move******\n")
	start = move[0]
	end = move[1]
	board.move(start,end)
	board.print()

	print("best move:", move)
	print("start:", convert_output(start))
	print("end:", convert_output(end))


#testing level order traversal
def test7():
	board = Board()
	val = board.eval()
	player = 10
	root = Tree(board, val, player)

	root.calculate_tree(root, 2)

	print("\n*******root******\n")
	root.print()

	print("\n*******children******\n")
	for child in root.store:
		child.print()

	level_order = root.get_level_order(root)
	print("\n*******level order******\n")
	print(level_order)


def main():
	#test1()
	#test2()
	#test3()
	#test4()
	#test5()
	#test6()
	test7()


main()

