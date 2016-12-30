
from graph import *

def _topological_sorting_util(v, linear_ord):
	v.visited = True

	for nbr in v.connections:
		if not nbr.visited:
			_topological_sorting_util(nbr, linear_ord)

	linear_ord.insert(0, v) # insert at the front of the list


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
	'''
