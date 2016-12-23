

class Node(object):
	'''
	A node contains data and the pointer to the next node, and the
	pointer to the previous node (optional).
	'''
	def __init__(self, data, next_node=None, previous_node=None):
		self.data = data
		self.next_node = next_node
		self.previous_node = previous_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def get_previous(self):
		return self.previous_node

	def print_node(self):
		print('data: %s\nnext: %s\nprevious: %s\n'
			%(self.data, self.next_node, self.previous_node))

	def set_data(self, data):
		self.data = data

	def set_next(self, next_node):
		self.next_node = next_node

	def set_previous(self, previous_node):
		self.previous_node = previous_node



class SimpleLinkedList(object):
	'''
	Simple linked list.
	'''
	def __init__(self, head=None):
		self.head = head

	def is_empty(self):
		return self.head == None

	def size(self):
		'''count number of nodes'''
		counter = 0
		node = self.head
		while node:
			counter = counter + 1
			node = node.get_next()
		return counter

	def traversal(self):
		'''print all node data'''
		node = self.head
		while node:
			print(node.get_data())
			node = node.get_next()

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def search(self, data):
		found = False
		node = self.head

		while node and found == False:
			if node.get_data() == data:
				found = True
			else:
				node = node.get_next()
		if found == False:
			raise ValueError('Data not in the list.')
		return node

	def delete(self, data):
		found = False
		node = self.head
		previous = None

		while node and found == False:
			if node.get_data() == data:
				found = True
			else:
				previous = node
				node = node.get_next()

		if found == False:
			raise ValueError('Data not in the list.')
		if previous == None:
			self.head = node.get_next()
		else:
			previous.set_next(node.get_next())


	def reverse(self):
		pass


class DoublyLinkedList(object):
	'''
	Doubly linked list.
	'''
	pass

class CircularLinkedList(object):
	'''
	Circular linked list.
	'''
	pass