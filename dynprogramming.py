
from graph import *

# I. shortest paths in DAG
def _topological_sorting_util(v, linear_ord):
	v.visited = True

	for nbr in v.connections:
		if not nbr.visited:
			_topological_sorting_util(nbr, linear_ord)

	linear_ord.append(v) # list as stack


def topological_sorting(dag):
	'''
	Find a linear order of a directed acylic graph (DAG).
	In topological sorting, for any vertex v, vertex u comes 
	before vertex v, for all edge starting from u to v.
	'''
	linear_ord = []
	for v in dag.vertex_list.values():
		v.visited = False

	for v in dag.vertex_list.values():
		if not v.visited:
			_topological_sorting_util(v, linear_ord)

	return linear_ord



def shortest_path_in_dag(dag, s):
	'''
	Find shortest paths from s to all vertices in the dag.
	time complexity: O(|V| + |E|)
	'''
	st = topological_sorting(dag)

	dist = {}
	for v in dag.vertex_list.values():
		dist[v] = sys.maxsize

	dist[dag.vertex_list[s]] = 0

	while st:
		v = st.pop()

		for nbr, w in v.connections.items():
			if dist[v] + w < dist[nbr]:
				dist[nbr] = dist[v] + w

	return dist



# II. edit distance
def edit_distance(str1, str2):
	'''
	Find the edit distance of two strings.
	time complexity 0(mn)
	'''
	m = len(str1)
	n = len(str2)

	E = [[0 for j in range(n)] for i in range(m)]

	for i in range(1, m):
		for j in range(1, n):
			E[i][j] = min(E[i-1][j]+1, E[i][j-1]+1, E[i-1][j-1]+1-(str1[i]==str2[j]))

	return E[m-1][n-1]