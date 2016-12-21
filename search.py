from numpy.random import choice


def linear_search(seq, key):
	'''
	Linear search algorithm. It returns the position of the key.
	Time complexity O(n).
	'''
	if len(seq) == 0:
		raise ValueError('Empty sequence.')

	for i in range(len(seq)):
		if seq[i] == key:
			return(i)

	raise ValueError('Key not in the sequence.') # key not found



def binary_search(seq, key):
	'''
	Binary search. Input must be sorted (ascending).
	Time complexity is O(log n).
	'''
	if len(seq) == 0:
		raise ValueError('Empty sequence.')

	start = 0
	end = len(seq) - 1

	while start <= end:
		mid = (start + end) // 2
		if seq[mid] == key:
			return(mid)
		elif key < seq[mid]:
			end = mid - 1
		elif key > seq[mid]:
			start = mid + 1

	raise ValueError('Key not in the sequence.') # key not found


def rank_search(seq, k):
	'''
	It returns the k_th smallest element of the sequence.
	This is a divide-and-conquer algorithm.
	It's average time complexity is O(n), and the worst time complexity is O(n^2).
	'''
	if len(seq) == 0:
		raise ValueError('Empty sequence.')

	pivot = choice(seq, 1)[0]
	S_L = []
	S_R = []
	S_M = []

	for v in seq:
		if v < pivot:
			S_L = S_L + [v]
		elif v == pivot:
			S_M = S_M + [v]
		else:
			S_R = S_R + [v]

	if k <= len(S_L):
		return rank_search(S_L, k)
	elif len(S_L) < k and k <= len(S_L) + len(S_M):
		return pivot
	else:
		return rank_search(S_R, k - len(S_L) - len(S_M))


def hashing():
	pass