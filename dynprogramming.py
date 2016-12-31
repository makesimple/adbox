
from graph import *

# I. shortest paths in DAG
# DAG, implicitly, lies in the heart of dynamic programming.
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
	
	Subproblem:
	E(i, j) = min{1+E(i-1, j), 1+E(i, j-1), diff(str1[i], str2[j]) + E(i-1, j-1)}

	Time complexity 0(mn)
	'''
	m = len(str1) + 1
	n = len(str2) + 1

	E = [[0 for j in range(n)] for i in range(m)]

	for i in range(1, m):
		E[i][0] = i
	for j in range(1, n):
		E[0][j] = j
	for i in range(1, m):
		for j in range(1, n):
			E[i][j] = min(E[i-1][j]+1, E[i][j-1]+1, E[i-1][j-1]+1-(str1[i-1]==str2[j-1]))

	return E[m-1][n-1]



# III. knapsack
# During a robbery, a burglar finds much more loot than he had expected 
# and has to decide what to take. His bag (or “knapsack”) will hold a 
# total weight of at most W pounds. The burglar has to choose an optimal 
# combination of loots to maxmize the value while subject to the weight limit.
def knapsack_with_repetition(W, ws, vs):
	'''
	The burglar is allowed to pick an item multiple times.

	@param:
		W: knapsack weight limit
		ws: weights, a list
		vs: values, a list

	Subproblem:
	K[w] is the maximum value achievable when the knapsack's weight limit is w
	K[w] = max(K[w - ws[i]] + vs[i]: vs[i] <= w)

	Time complexity: O(nW), where n is the number of distinct items.
	'''
	n = len(ws)

	K = [0 for i in range(W+1)]
	for w in range(1, W+1):
		sub = []
		for i in range(n):
			if ws[i] <= w:
				sub.append(K[w - ws[i]] + vs[i])
		if sub: 
			K[w] = max(sub)
		else:
			K[w] = K[w-1]

	return K[W]


def knapsack_without_repetition(W, ws, vs):
	'''
	The burglar can pick an item no more than once.

	Subproblem:
	K(w, j) is the maximum value achievable when the knapsack's capacity is w, and
	the burglar chooses item from 1, ..., j.
	K(w, j) = max{K(w-ws[j], j-1)+vs[j], K(w, j-1)}

	Time complexity: O(nW)
	'''
	n = len(ws)

	K = [[0 for j in range(n+1)] for w in range(W+1)]
	for w in range(1, W+1):
		for j in range(1, n+1):
			if ws[j-1] <= w and K[w-ws[j-1]][j-1] + vs[j-1] > K[w][j-1]:
				K[w][j] = K[w-ws[j-1]][j-1] + vs[j-1]
			else:
				K[w][j] = K[w][j-1]

	return K[W][n]