#Yong Da Li
#Sunday, March 3, 2019
#Professor Nebu Mathai
#CSC190

#test file for queue class, for level order traversal

#enqueue, add to end
#dequeue, remove from start

from chessPlayer_queue import *


def main():
	x = Queue()

	for i in range (0, 5):
		x.enqueue(i)

	x.print()

	for i in range (0,6):
		r = x.dequeue()
		print("r: ", r)
		x.print()

main()