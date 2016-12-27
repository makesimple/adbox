# credits: http://interactivepython.org/runestone/static/pythonds/index.html

from collections import deque
import sys
from heaps import HeapItem, BinaryHeap

class Vertex(object):
	'''
	Represents each vertex in a Graph.
	Each vertex uses a dictionary to store its neighbor(s) and the 
	corresponding weight(s)
	'''
	def __init__(self, key):
		self.id = key
		self.connections = {} # the dictionary to store neighbor information
							  # the dictionary key is a vertex object
							  # the dictionary value is the weight

	def add_neighbor(self, nbr, w=1): # nbr is also a Vertex instance
		self.connections[nbr] = w

	def get_neigbhors(self):
		'''return the keys of all neighbors'''
		return self.connections.keys()

	def __str__(self):
		return str(self.id) + 'connected to' + str([x.id for x in self.connections])


class Graph(object):
	'''
	Contains a dictionary that maps vertex names (keys) to vertex objects.
	'''
	def __init__(self):
		self.vertex_list = {}
		self.size = 0

	def add_vertex(self, key):
		if key in self.vertex_list:
			raise ValueError('Vertex already exists.')

		new_vertex = Vertex(key)
		self.vertex_list[key] = new_vertex
		self.size += 1

	def add_edge(self, f, t, w=1, directed=False):
		if f not in self.vertex_list:
			self.add_vertex(f)
		if t not in self.vertex_list:
			self.add_vertex(t)

		self.vertex_list[f].add_neighbor(self.vertex_list[t], w)
		if directed == False:
			self.vertex_list[t].add_neighbor(self.vertex_list[f], w)

	def get_vertices(self):
		'''return the keys of all vertex objects'''
		return self.vertex_list.keys()

	def search_vertex(self, key):
		'''return the vertex object with the id matching key'''
		if key not in self.vertex_list:
			raise ValueError('Key not in the graph')
		return self.vertex_list[key]

	def __iter__(self):
		return iter(self.vertex_list.values())

	def bfs_traversal(self, st):
		'''
		Breadth first search traversal.
		Use queue for this task.
		0. Mark every vertex as unvisited
		1. Initialize the empty queue with st, the starting vertex, mark it as visited
		2. Choose the current node as the right most vertex in the queue
		3. Visit its neighbor who has never been visited before, mark it as visited
		4. Repeat step 3 until there is no unvisited neighbor
		5. Pop a vertex from the queue, and go to step 2; Stop algorithm is queue is empty
		'''
		for v in self.vertex_list.values():
			v.visited = False

		q = deque() # queue
		v = self.search_vertex(st)
		v.visited = True
		q.appendleft(v)
		print(st)

		while q:
			v = q[len(q)-1]
			for nbr in v.connections:
				if nbr.visited == False:
					nbr.visited = True
					q.appendleft(nbr)
					print(nbr.id)
			q.pop()

	def dfs_traversal(self, st):
		'''
		Depth first search traveral.
		Use stack for this task.
		0. Mark every vertex as unvisited
		1. Initialize the empty stack with st, the starting vertex, mark i as visited
		2. Choose the top vertex as the current vertex
		3. Visit one of the current vertex's neighbors, whose state is unvisited, mark it as visited
		4. Go to step 2, if the current vertex has no unvisited neighbor, pop the stack, go to 2 again
		5. Stop if the stack is empty
		'''
		for v in self.vertex_list.values():
			v.visited = False

		s = deque() # stack
		v = self.search_vertex(st)
		v.visited = True
		s.append(v)
		print(st)

		while s:
			v = s[len(s)-1]
			all_visited = True # assume all v's neighbors have been visited
			for nbr in v.connections:
				if nbr.visited == False:
					nbr.visited = True
					s.append(nbr)
					print(nbr.id)
					all_visited = False
					break
			if all_visited == True:
				s.pop()

	def prim_mst(self):
		'''
		Prim's algorithm for finding a minimum spanning tree in an UNDIRECTED graph.
		At each time, the edge set of the partial mst is X, divide the graph G = (V, E) 
		into two sets: S and V - S, where S consists of the nodes of the partial mst, 
		find the lightest edge e connecting S and V - S, and grow the tree by one 
		edge: X = X union {e}, S = S union {endpoint of e that outside of S}

		Prim's algorithm time complexity depends on its implementation method.
		Here we implement it using Binary Heap and adjacency list, which makes a time compelxity 
		O((|v|+|e|log|v|)) = O(|e|log|v|).
		'''
		if self.size == 0:
			raise ValueError('Empty graph.')
		
		pq = BinaryHeap()
		for v in self.vertex_list.values():
			v.pred = None
			v.hi = pq.insert(sys.maxsize, v) # a reference to the heap item

		while not pq.is_empty():
			v = pq.del_min().value # a vertex object
			for nbr in v.connections:
				if nbr.hi.pos:
					if v.connections[nbr] < nbr.hi.key: # nbr is a neighbor and it is in the queue
						nbr.pred = v
						pq.decrease_key(v.connections[nbr], nbr.hi)


	def kruskal_mst(self):
		'''
		Kruskal's algorithm for finding a minimum spanning tree in an UNDIRECTED graph.
		'''
		pass

	def dijkstra(self, s):
		'''
		Dijkstra algorithm for finding the shortest path from s to any other vertex in the graph.
		Using Binary Heap, the implementation is very similar to Prim's algorithm.

		At time t, let S denote the set of nodes whose shortest paths have been determined, 
		a next candidate for S is any node in V - S, such that their previous nodes all belong to S,
		choose the one v that has the shortest path length from s to it, 
		merge S = S union {v}.

		Dijkstra algorithm's running time depends on the priority queue implementation method.
		Here we implement it using Binary Heap and adjacency list, which makes a time complexity
		O((|V|+|E|)log |V|)
		'''
		if self.size == 0:
			raise ValueError('Empty graph.')

		if s not in self.vertex_list:
			raise ValueError('Vertex does not exist.')

		pq = BinaryHeap()
		for v_k in self.vertex_list:
			v = self.vertex_list[v_k]
			v.pred = None
			if v_k == s:
				v.hi = pq.insert(0, v)
			else:
				v.hi = pq.insert(sys.maxsize, v)


		while not pq.is_empty():
			m_hi = pq.del_min()
			k = m_hi.key
			v = m_hi.value
			for nbr in v.connections:
				if nbr.hi.pos:
					if v.connections[nbr] + k < nbr.hi.key:
						nbr.pred = v
						pq.decrease_key(v.connections[nbr] + k, nbr.hi)



	def strongly_connected(self):
		pass












