from sort import *
from copy import deepcopy

import itertools

def sequence(generator, max):
	return itertools.takewhile(lambda x: x < max / 3, generator())

def knuth():
	h = 1
	while True:
		yield h
		h = 3 * h + 1 

def sedgewick():
	yield 1
	for i in itertools.count(2):
		yield 4**i - (3 * 2**i) + 1
		i -= 1
		yield (9 * 4**i) - (9 * 2**i) + 1

def shellSort(data, step=step):
	data = deepcopy(data)
	N = len(data)
	gaps = reversed(list(sequence(sedgewick, N)))
	for h in gaps:
		for j in xrange(h, N):
			while j >= h and data[j] < data[j-h]:
				swap(data, j, j-h)
				j -= h
			step(data)
	step(data)
	return data

# Print out the the sequences
if __name__ == '__main__':

	print 'Knuth'
	for i in sequence(knuth, 10000000):
		print i

	print '----------------'

	print 'Sedgewick'
	for i in sequence(sedgewick, 10000000):
		print i