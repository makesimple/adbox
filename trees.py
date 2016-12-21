
class TreeNode(object):
	def __init__(self, key, value, parent=None, left=None, right=None):
		self.key = key
		self.value = value
		self.parent = parent
		self.left = left
		self.right = right
		self.bf = 0 # when a new node added to a tree, before rebalancing, 
					# as a leaf node, its balance factor is always 0

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

	def height(self):
		'''return the maximum height of the tree.'''
		if not self.root:
			return 0
		else:
			return self._height(self.root)

	def _height(self, node):
		if not node:
			return 0
		else:
			return 1 + max(self._height(node.left), self._height(node.right))

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

		if current.key == key:
			return current
		elif key < current.key:
			return self._search(key, current.left)
		else:
			return self._search(key, current.right)

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
				raise ValueError('Key not in the BST.')

	def remove(self, node):
		'''
		Remove a node from the tree. There are three situations.
		A better implementation whould be resursively delete a node.
		'''
		# I. the simplest case
		if node.is_leaf():
			if node.is_left_child():
				node.parent.left = None
			else:
				node.parent.right = None

		# II. a slightly trickier case
		# can be further divide into 6 smaller cases
		elif node.has_one_child():
			if node.left:
				if node.is_left_child():
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

		# III. the most challenging case, node has two children
		# find the successor of the node to be removed, which is either the minimum
		# node in the right subtree or the maximum node in the left subtree.
		# replace node with the successor and delete the successor.
		else:
			key, val = self.find_and_kill(node)
			node.key = key
			node.value = val

	def find_and_kill(self, node):
		'''find the minimum in the right subtree, return its key and value, and
		wipe it out'''
		target = node.right
		while target.left:
			target = target.left

		key = target.key
		val = target.value

		if target.is_leaf():
			if target.is_left_child():
				target.parent.left = None
			else:
				target.parent.right = None
		else: # target is not a leaf node, it has a child and it must be a right child
			if target.is_left_child():
				target.right.parent = target.parent
				target.parent.left = target.right
			else:
				target.right.parent = target.parent
				target.parent.right = target.right

		return (key, val)



class AVLTree(BinarySearchTree):
	'''
	A special type of Binary search tree for better algorithm performance.
	Balance factor = height(left_subtree) - height(right_subtree)
	A balanced BST has balance factor equals to -1, 0, or 1.
	The worst case searching time complexity for AVL tree is 1.44logn, where n is 
	the total number of nodes in the tree.

	The implementation is based on the following tutorial:
	http://interactivepython.org/runestone/static/pythonds/Trees/AVLTreeImplementation.html
	'''
	def _insert(self, key, val, current):
		if key < current.key:
			if current.left:
				self._insert(key, val, current.left)
			else:
				current.left = TreeNode(key, val, parent=current)
				self._update_balance_factor(current.left)
		elif key > current.key:
			if current.right:
				self._insert(key, val, current.right)
			else:
				current.right = TreeNode(key, val, parent=current)
				self._update_balance_factor(current.right)

	def _update_balance_factor(self, node):
		if node.bf > 1 or node.bf < -1:
			self.rebalance(node)
			return

		if not node.parent:
			if node.is_left_child():
				node.parent.bf += 1
			else:
				node.parent.bf -= 1

			if node.parent.bf != 0:
				self._update_balance_factor(node.parent)


	def rebalance(self, node):
		if node.bf > 0: # need right rotation
			if node.left.bf < 0: # if its left child is right heavy,
								 # first do a left rotation on that child
				self.left_rotate(node.left)
			self.right_rotate(node)
		else:
			if node.right.bf > 0:
				self.right_rotate(node.root)
			self.left_rotate(node)


	def left_rotate(self, root):
		'''left rotation'''
		pivot = root.right # promote the right child to the root
		root.right = pivot.left 

		if not pivot.left:
			pivot.left.parent = root

		pivot.parent = root.parent

		if root.is_root():
			self.root = pivot
		else:
			if root.is_left_child():
				root.parent.left = pivot
			else:
				root.parent.right = pivot

		pivot.left = root
		root.parent = pivot

		root.bf = root.bf + 1 - min(pivot.bf, 0)
		pivot.bf = pivot.bf + 1 + max(root.bf, 0)

	def right_rotate(self, root):
		'''right rotation'''
		pivot = root.left
		root.left = pivot.right

		if not pivot.right:
			pivot.right.parent = root

		pivot.parent = root.parent

		if root.is_root():
			self.root = pivot
		else:
			if root.is_left_child():
				root.parent.left = pivot
			else:
				root.parent.right = pivot

		pivot.right = root
		root.parent = pivot

		root.bf = root.bf -1 - max(pivot.bf, 0)
		pivot.bf = pivot.bf - 1 + min(root.bf, 0)


