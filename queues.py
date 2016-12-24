
class HeapItem(object):
	'''Item in a heap'''
	def __init__(self, key, value, pos=None):
		self.key = key
		self.value = value
		self.pos = pos # position of the heap item in the Binary Heap (Priority Queue)


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
		self.queue = [HeapItem(0, '')] # just to occupy a place for convenience in position calculation
		self.size = 0

	def is_empty(self):
		if self.size == 0:
			return True
		else:
			return False

	def length(self):
		return self.size

	def traversal(self):
		if self.size == 0:
			return
		for i in range(1, self.size+1):
			print('key: %s, value: %s'%(self.queue[i].key, self.queue[i].value))

	def peek_min(self):
		if self.size == 0:
			raise ValueError('Empty Binary Heap.')
		return (self.queue[1].key, self.queue[1].value)

	def search_key(self, key):
		'''returns the pos and value'''
		pass

	def insert(self, key, value=''):
		'''
		To insert a new node into the Binary Heap, first hang it at the last of the heap,
		swap it with its parent if it is smaller than its parent, repeat until Binary Heap 
		property holds
		'''
		self.size += 1
		hi = HeapItem(key, value, self.size)
		if self.size == 0:
			self.queue = self.queue + [hi]
			return
		else:
			self.queue = self.queue + [hi]
			self._swap_up(self.size)
		return hi

	def _swap_up(self, i):
		if i == 1:
			return

		parent = self.queue[i // 2]
		child = self.queue[i]
		if parent.key > child.key:
			tmp = child
			self.queue[i] = parent
			self.queue[i // 2] = tmp
			self.queue[i].pos = i
			self.queue[i // 2].pos = i // 2
			self._swap_up(i//2)
		else:
			return

	def del_min(self):
		'''
		To delete the minimum node from the heap, move the last node to the root of the heap.
		Swap it with its minimum child, repeat until Binary Heap property holds.
		'''
		if self.size == 0:
			raise ValueError('Empty Binary Heap.')

		hp_min = self.queue[1]
		if self.size == 1:
			self.queue = [HeapItem(0, '')]
			self.size = 0
		else:
			self.queue[1] = self.queue[self.size]
			self.queue[1].pos = 1
			self.size -= 1
			self._swap_down(1)

		hp_min.pos = None
		return hp_min

	def _swap_down(self, i):
		if 2*i > self.size: # has no child, reached the bottom level
			return

		mc, pos = self.min_child(i)
		if mc.key < self.queue[i].key:
			self.queue[pos] = self.queue[i]
			self.queue[i] = mc
			self.queue[pos].pos = pos
			self.queue[i].pos = i
			self._swap_down(pos)
		else:
			return


	def min_child(self, i):
		'''Return the key and position of the minimum child.'''
		lc = self.queue[2*i]

		if 2*i+1 > self.size: # has only the left child
			return lc, 2*i
		else:
			rc = self.queue[2*i+1]
			if lc.key < rc.key:
				return lc, 2*i
			else:
				return rc, 2*i+1

	def decrease_key(self, new_key, hi):
		'''
		Change the key of value to new_key (decrease)
		currently, this method can only be used in graph.py prim_mst method.
		'''
		if new_key > hi.key:
			raise ValueError('New key should be smaller than the original key.')
			
		hi.key = new_key
		self._swap_up(hi.pos)
