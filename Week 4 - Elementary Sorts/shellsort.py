from sort import *
from copy import deepcopy

def shellSort(data, step=step):
	data = deepcopy(data)
	
	N = len(data)
	h = 1
	while h < (N/3):
		h = 3 * h + 1

	while h >= 1:
		for i in xrange(h,N):
			j = i
			while j >= h and data[j] < data[j-h]:
				swap(data, j, j-h)
				step(data)
				j -= h
		h = h / 3
	step(data)
	return data