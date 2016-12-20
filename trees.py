
class TreeNode(object):
	def __init__(self, key, value, parent=None, left=None, right=None):
		self.key = key
		self.value = value
		self.parent = parent
		self.left = left
		self.right = right

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
			self.right.parent = self


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

	def traversal(self, order='inorder'):
		'''tree traversal with one of the following methods:
		   1. inorder
		   2. preorder
		   3. postorder
		'''
		if not self.root:
			raise ValueError('Empty BST.')

		if order == 'inorder':
			self._inorder(self.root)
		elif order == 'preorder':
			self._preorder(self.root)
		elif order == 'postorder':
			self._postorder(self.root)
		else:
			raise ValueError('Wrong input.')

	def _inorder(self, current):
		if current:
			self._inorder(current.left)
			print('key: %s, value: %s'%(current.key, current.value))
			self._inorder(current.right)

	def _preorder(self, current):
		if current:
			print('key: %s, value: %s'%(current.key, current.value))
			self._preorder(current.left)
			self._preorder(current.right)

	def _postorder(self, current):
		if current:
			self._postorder(current.left)
			self._postorder(current.right)
			print('key: %s, value: %s'%(current.key, current.value))

	def insert(self, key, value):
		'''
		insert a node into the BST
		'''
		if self.root:
			self._insert(key, value, self.root)
		else:
			self.root = TreeNode(key, value)

		self.size = self.size + 1

	def _insert(self, key, value, current):
		if key < current.key:
			if current.left:
				self._insert(key, value, current.left)
			else:
				current.left = TreeNode(key, value, parent=current)
		elif key > current.key:
			if current.right:
				self._insert(key, value, current.right)
			else:
				current.right = TreeNode(key, value, parent=current)
		else:
			raise ValueError('Key already exists.')


	def search(self, key):
		if self.root:
			target = self._search(key, self.root)
			if target:
				return target.value
			else:
				return None
		else:
			return None

	def _search(self, key, current):
		if not current:
			return None
		elif current.key == key:
			return current
		elif key < current.key:
			self._search(key, current.left)
		else:
			self._search(key, current.right)

	def delete(self, key):
		'''
		Delection is much more complex than other methods.
		'''
		if self.size == 0:
			raise ValueError('Empty BST.')

		elif self.size == 1:
			if self.root.key == key:
				self.root = None
				self.size = 0
			else:
				raise ValueError('Key not in the BST.')

		else:
			node_to_remove = self._search(key, self.root)
			if node_to_remove:
				self.remove(node_to_remove)
				self.size = self.size - 1
			else:
				raise ValueError('Key no in the BST.')

	def remove(self, node):
		'''
		Remove a node from the tree. There are three situations.
		'''
		# the simplest case
		if node.is_leaf():
			if node.is_left_child():
				node.parent.left = None
			else:
				node.parent.right = None

		# a slightly tricker case
		# can be further divide into 6 smaller cases
		elif node.has_one_child():
			if node.left:
				if node.is_left_child()
					node.left.parent = node.parent
					node.parent.left = node.left
				elif node.is_right_child():
					node.left.parent = node.parent
					node.parent.right = node.left
				else: # node is the root
					node.update(node.left.key, node.left.value, 
						node.left.left, node.right.right)
			else:
				if node.is_left_child():
					node.right.parent = node.parent
					node.parent.left = node.right
				elif node.is_right_child():
					node.right.parent = node.parent
					node.parent.right = node.right
				else:
					node.update(node.right.key, node.right.value, 
						node.right.left, node.right.right)

		# the most challenging case, node has two children
		# find the successor of the node to be removed. replace node with 
		# the successor and delete the successor.
		else:
			succ = self._successor(node)
			self.splice_out(succ)
			node.key = succ.key
			node.value = succ.value


	def _successor(self, node):
		pass

	def splice_out(self):
		pass


