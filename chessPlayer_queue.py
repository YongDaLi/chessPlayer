#Yong Da Li
#Sunday, March 3, 2019
#Professor Nebu Mathai
#CSC190

#queue class, for level order traversal

#enqueue, add to end
#dequeue, remove from start
class Queue():
	def __init__(self):
		self.store = []

	#add to end
	def enqueue(self, val):
		self.store = self.store + [val]

	#remove from start
	def dequeue(self):
		if self.isEmpty() == False:
			deleted = self.store[0]
			self.store = self.store[1: len(self.store)]
			return deleted

		else:
			return False


	#returns True if empty queue
	def isEmpty(self):
		if len(self.store) == 0:
			return True
		else:
			return False


	#displays queue
	def print(self):
		print("\nqueue:")
		print(self.store)