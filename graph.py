# credits: http://interactivepython.org/runestone/static/pythonds/index.html

from collections import deque
from Queue import ProrityQueue

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
		Prim's algorithm for finding a minimum spanning tree of an undirected graph.
		'''
		if self.size == 0:
			raise ValueError('Empty graph.')
		if self.size == 1:
			return self.vertex_list.keys()

		S.set(list(self.vertex_list.keys())[0:1]) 
		X = set() # edges of the MST
		tree_size = 0 # number of edges

		while tree_size < self.size-1:
			













