from heaps import HeapItem, BinaryHeap


class Huffman(object):
	'''
	Huffman encoding.

	Input: An array f[1...n] of frequencies
	Output: An full Binary encoding tree with n leaves

	The cost of a tree is the sum of the frequencies of all leaves and 
	internal nodes, except the root. The frequency of an internal node 
	is defined as the sum of the frequencies of its two children.

	1. Sart with n frequencies f1, f2, ..., fn, find the two smallest 
	frequencies, say f1 and f2, make them two children of a new node
	2. Now the problem recuded to minimize [f1+f2 + Huffman(f1+f2, f3, ..., fn)]

	Here we implement it using Binary Heap. This gives us a time complexity 
	O(nlog n).

	credit: https://rosettacode.org/wiki/Huffman_coding#Python
	'''
	def __init__(self):
		pass


