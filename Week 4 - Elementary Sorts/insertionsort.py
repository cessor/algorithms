from sort import *
from copy import deepcopy

def insertionSort(data, step=step):
	data = deepcopy(data)
	length = len(data)
	for i in xrange(length):
		for j in reversed(xrange(1,i+1)):
		 	if data[j] < data[j-1]:
		 		swap(data, j, j-1)
		 	else: 
		 		break
 		step(data)
	return data