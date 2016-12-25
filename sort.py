from collections import deque

def bubble_sort(seq):
	'''
	Bubble sort.
	Time complexity: O(n^2).
	'''
	for end in reversed(range(len(seq))):
		for i in range(end):
			if seq[i] > seq[i+1]:
				tmp = seq[i]
				seq[i] = seq[i+1]
				seq[i+1] = tmp

	return seq


def insertion_sort(seq):
	'''
	Insertion sort.
	Time complexity: O(n^2).
	'''
	for i in range(len(seq)):
		key = seq[i]
		pos = i - 1

		while pos >= 0:
			if seq[pos] > key:
				seq[pos+1] = seq[pos]
				pos = pos -1
			elif seq[pos] <= key:
				seq[pos+1] = key
				break

		if pos == -1:
			seq[0] = key

	return seq


def selection_sort(seq):
	'''
	Selection sort.
	Time complexity: O(n^2).
	'''

	for i in range(len(seq)):
		smallest = seq[i]
		pos = i
		for j in range(i+1, len(seq)):
			if seq[j] < smallest:
				smallest = seq[j]
				pos = j
		seq[pos] = seq[i]
		seq[i] = smallest

	return seq


def merge(seq1, seq2):
	'''
	Merge two sorted sequences into a single sequence.
	'''
	q1 = deque(seq1)
	q2 = deque(seq2)
	q3 = []

	while len(q1) != 0 and len(q2) != 0:
		a = q1[0]
		b = q2[0]
		if a < b:
			q3 = q3 + [a]
			q1.popleft()
		else:
			q3 = q3 + [b]
			q2.popleft()

	while len(q1) != 0:
		a = q1.popleft()
		q3 = q3 + [a]

	while len(q2) != 0:
		b = q2.popleft()
		q3 = q3 + [b]

	return q3


def merge_sort(seq):
	'''
	Merge sort.
	Worst time complexity: O(nlogn).
	Best time complexity: O(nlogn) typical.
	Average time complexity: O(nlogn). 

	It's a divide-and-conquer algorithm with T(n) = 2T(n/2) + O(n).
	'''
	if len(seq) == 1:
		return seq

	else:
		mid = len(seq) // 2

		seq1 = merge_sort(seq[:mid])
		seq2 = merge_sort(seq[mid:])

		return merge(seq1, seq2)


def partition(seq):
	pivot = seq[0]
	left_ = 1
	right_ = len(seq) - 1
	located = False

	while located == False:
		while left_ <= right_ and seq[left_] <= pivot:
			left_ = left_ + 1
		while left_ <= right_ and seq[right_] >= pivot:
			right_ = right_ - 1
		if left_ > right_:
			located = True
		else:
			tmp = seq[left_]
			seq[left_] = seq[right_]
			seq[right_] = tmp

	seq[0] = seq[right_]
	seq[right_] = pivot

	return right_


def quick_sort(seq):
	'''
	Quick sort.
	Worst time complexity: O(n^2).
	Best time complexity: O(nlogn).
	Average time complexity: O(nlogn).

	It's a divide-and-conquer algorithm.
	'''
	if len(seq) == 0 or len(seq) == 1:
		return seq

	point = partition(seq)
	quick_sort(seq[:point]) # pass by reference
	quick_sort(seq[point+1:])

	return seq


def shell_sort(seq):
	pass


def heap_sort(seq):
	pass