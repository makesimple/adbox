# credits: http://interactivepython.org/runestone/static/pythonds/index.html

class Vertex(object):
	'''
	Represents each vertex in a Graph.
	Each vertex uses a dictionary to store its neighbor(s) and the 
	corresponding weight(s)
	'''
	def __init__(self, key):
		self.id = key
		self.connections = {} # the dictionary to store neighbor information

	def add_neighbor(self, nbr, w=1): # nbr is also a Vertex instance
		self.connections[nbr] = w

	def get_neigbhors(self):
		return self.connections.keys()

	def __str__(self):
		return str(self.id) + 'connected to' + str([x.id for x in self.connections])


class Graph(object):
	'''
	Contains a dictionary that maps vertex names to vertex objects.
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

	def add_edge(self, f, t, w):
		if f not in self.vertex_list:
			self.add_vertex(f)
		if t not in self.vertex_list:
			self.add_vertex(t)

		self.vertex_list[f].add_neighbor(self.vertex_list[t], w)

	def get_vertices(self):
		return self.vertex_list.keys()

	def __iter__(self):
		return iter(self.vertex_list.values())


