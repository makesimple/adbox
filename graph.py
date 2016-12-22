# credits: http://interactivepython.org/runestone/static/pythonds/index.html

from collections import deque

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

	def add_edge(self, f, t, w=1):
		if f not in self.vertex_list:
			self.add_vertex(f)
		if t not in self.vertex_list:
			self.add_vertex(t)

		self.vertex_list[f].add_neighbor(self.vertex_list[t], w)

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
		'''
		for v in self.vertex_list.values():
			v.visited = False

		d = deque()
		v = self.search_vertex(st)
		v.visited = True
		d.appendleft(v)
		print(st)

		while d:
			v = d[len(d)-1]
			for nbr in v.connections:
				if nbr.visited == False:
					nbr.visited = True
					d.appendleft(nbr)
					print(nbr.id)
			d.pop()









