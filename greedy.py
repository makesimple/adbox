from heaps import HeapItem, BinaryHeap
from collections import defaultdict

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
		self.symb_code = defaultdict(str) # dict mapping symbol to code
		self.code_symb = defaultdict(str) # dict mapping code to symbol
		self.symb_f = defaultdict(int)

	def show_coding(self):
		print('Symbol\tFrequency\tCode')
		for symb in self.symb_code:
			print("%s\t%s\t%s" % (symb, self.symb_f[symb], self.symb_code[symb]))

	def encode(self, txt):
		for symb in txt:
			self.symb_f[symb] += 1

		pq = BinaryHeap()
		for symb, f in self.symb_f.items():
			#print('f:%s' %f)
			pq.insert(f, [symb])

		while pq.length() > 1:
			m1 = pq.del_min()
			m2 = pq.del_min()

			print(m1.key, m2.key)

			for symb in m1.value:
				self.symb_code[symb] = '0' + self.symb_code[symb]
			for symb in m2.value:
				self.symb_code[symb] = '1' + self.symb_code[symb]

			k = m1.key + m2.key
			val = m1.value + m2.value
			pq.insert(k, val)

		for symb, code in self.symb_code.items():
			self.code_symb[code] = symb

	def decode(self, txt):
		pass





