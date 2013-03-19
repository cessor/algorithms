from sort import *
from copy import deepcopy

def selectionSort(data, step=step):
	data = deepcopy(data)
	for i in xrange(len(data)):
		min = i
		for j in xrange(i+1, len(data)):
			if data[j] < data[min]:
				min = j
		step(data)
		swap(data, i, min)
	return data	