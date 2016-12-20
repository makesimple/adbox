
class TreeNode(object):
	def __init__(self, key, value, parent=None, left=None, right=None):
		self.key = key
		self.value = value
		self.parent = parent
		self.left = left
		self.right = right
		self.visited = False


	def is_left_child(self):
		return self.parent and self.parent.left == self

	def is_right_child(self):
		return self.parent and self.parent.right == self

	def is_root(self):
		return not self.parent

	def is_leaf(self):
		return not (self.left or self.right)

	def has_one_child(self):
		return (self.left or self.right) and not(self.left and self.right)

	def has_two_children(self):
		return self.left and self.right

	def update(self, key, value, left, right):
		self.key = key
		self.value = value
		self.left = left
		self.right = right

		if self.left:
			self.left.parent = self
		if self.right:
			self.right = self


class BinarySearchTree(object):
	'''
	Binary search tree.
	There may be some issues with the deletion implementation!!!
	'''
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def in_order_traversal(self):
		'''print the binary search tree with ascending key order'''
		if not self.root:
			raise ValueError('Empty BST.')

		self.traversal_(self.root)

	def traversal_(self, node):
		if node.left and node.left.visited == False:
			self.traversal_(node.left)
		elif node.left and node.left.visited == True:
			node.visited = True
			print('key: %s, value: %s'%(node.key, node.value))
			if node.right:
				self.traversal_(node.right)
		elif not node.left and node.visited == False:
			node.visited = True
			print('key: %s, value: %s'%(node.key, node.value))
			if node.right:
				self.traversal_(node.right)

	def insert(self, key, value):
		if not self.root:
			# if there is no root, put it to the root
			self.root = TreeNode(key, value)
			self.size = 1
		else:
			# search the right place to place the new node
			current = self.root
			found = False
			while not found:
				if key == current.key:
					raise ValueError('Key already exists!')
				elif key < current.key and not current.left:
					found = True
					node = TreeNode(key, value)
					current.update(current.key, current.value, node, current.right)
					self.size = self.size + 1
				elif key < current.key and current.left:
					current = current.left
				elif key > current.key and not current.right:
					found = True
					node = TreeNode(key, value)
					current.update(current.key, current.value, current.left, node)
					self.size = self.size + 1
				else:
					current = current.right

	def search(self, key):
		if self.size == 0:
			raise ValueError('Empty BST.')

		current = self.root
		while current:
			if key == current.key:
				return current.value
			elif key < current.key:
				current = current.left
			elif key > current.key:
				current = right

		raise ValueError('Key not found.')

	def delete(self, key):
		'''
		Delection is much more complex than other methods.
		'''
		if self.size == 0:
			raise ValueError('Empty BST.')

		# the tree only has the root
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size = 0
		elif self.size == 1 and self.root.key != key:
			raise ValueError('Key not in the tree.')

		else:
			current = self.root
			found = False
			while not Found:
				if current.key == key:
					found = True
					self.size = self.size - 1

					# I. the matched node is a leaf
					if current.is_leaf():
						parent = current.parent
						if parent.left == current:
							parent.update(parent.key, parent.value, None, parent.right)
						else:
							parent.update(parent.key, parent.value, parent.left, None)

					# II. the matched node has a single child, there are six cases
					if current.has_one_child():
						if current.is_left_child(): # current node is the left child
							if current.left:
								current.left.parent = current.parent
								current.parent.left = current.left
							else:
								current.right.parent = current.parent
								current.parent.left = current.right
						elif current.is_right_child():
							if current.left:
								current.left.parent = current.parent
								current.parent.right = current.left
							else:
								current.right.parent = current.parent
								current.parent.right = current.right
						else: # current node is the root
							if current.left:
								root = TreeNode(current.left.key, current.left.value, 
									current.left.left, current.left.right)
								self.root = root
							else:
								root = TreeNode(current.right.key, current.right.value, 
									current.right.left, current.right.right)
								self.root = root

					# III. the matched node has both children
					# this is the hardest part
					# 1. find the minimum the value in the right subtree
					# 2. replace the node to be removed with the founded minimum node
					# 	 , now the right subtree contains a duplicate
					# 3. remove the duplicate (note that the minimum node has no left child)
					else:
						min_node = self.find_right_subtree_minimum(current)
						current.update(min_node.key, min_node.value, min_node.left, min_node.right)
						self.splice_out(min_node)

				elif key < current.key:
					current = current.left
				else:
					current = current.right

			if not found:
				raise ValueError('Key not in the tree.')

	
	def find_right_subtree_minimum(self, current):
		'''find the minimum node of the right subtree of node current'''
		min_node = current
		while min_node.left:
			min_node = min_node.left
		return min_node

	def splice_out(self, min_node):
		'''remove the minimum node in the right subtree'''
		parent = min_node.parent
		if min_node.is_leaf():
			parent.update(parent.key, parent.value, None, parent.right)
		elif min_node.has_one_child() and min_node.is_right_child():
			parent.update(parent.key, parent.value, parent.left, min_node.right)
		else:
			parent.update(parent.key, parent.value, min_node.right, parent.right)
