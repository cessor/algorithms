from sort import *
from copy import deepcopy

def selectionSort(data, step = lambda d: d):
	data = deepcopy(data)
	for i in range(len(data)):
		min = i
		for j in range(i+1, len(data)):
			if data[j] < data[min]:
				min = j
		step(data)
		swap(data, i, min)
	return data	