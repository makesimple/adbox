

class BinaryHeap(object):
	'''
	Binary heap (Priority queue)
	The classical data sctructure to implement a priority queue. It allows
	us both enqueue and dequeue items in O(logn), faster than ordinary list
	insertion O(n) and list sorting O(nlogn).

	There are two variants: min heap and max heap. Here we implement the min heap.

	Though Heap is tree, it is a complete binary tree which makes it extremly easy 
	to implement as it can be implemented by using just list.
	'''
	def __init__(self):
		self.queue = [[0, '']]
		self.size = 0

	def length(self):
		return self.size

	def traversal(self):
		if self.size == 0:
			return
		for i in range(1, self.size+1):
			print('key: %s, value: %s'%(self.queue[i][0], self.queue[i][1]))

	def peek_min(self):
		if self.size == 0:
			raise ValueError('Empty Binary Heap.')
		return (self.queue[1][0], self.queue[1][1])

	def insert(self, key, value=''):
		if self.size == 0:
			self.queue = self.queue + [[key, value]]
			self.size = 1
			return
		else:
			self.queue = self.queue + [[key, value]]
			self.size += 1
			self._swap_up(self.size)

	def _swap_up(self, i):
		if i == 1:
			return

		parent = self.queue[i // 2]
		child = self.queue[i]
		if parent > child:
			tmp = child
			self.queue[i] = parent
			self.queue[i // 2] = tmp
			self._swap_up(i//2)
		else:
			return

	def del_min(self):
		if self.size == 0:
			raise ValueError('Empty Binary Heap.')

		hp_min = (self.queue[1][0], self.queue[1][1])
		if self.size == 1:
			self.queue = [[0, '']]
			self.size = 0
		else:
			self.queue[1] = self.queue[self.size]
			self.size -= 1
			self._swap_down(1)

		return hp_min

	def _swap_down(self, i):
		if 2*i > self.size: # has no child, reached the bottom level
			return

		mc, pos = self.min_child(i)
		self.queue[pos] = self.queue[i]
		self.queue[i] = mc
		self._swap_down(pos)


	def min_child(self, i):
		'''return the key and position of the minimum child'''
		lc = self.queue[2*i]

		if 2*i+1 > self.size: # has only the left child
			return lc, 2*i
		else:
			rc = self.queue[2*i+1]
			if lc[0] < rc[0]:
				return lc, 2*i
			else:
				return rc, 2*i+1


