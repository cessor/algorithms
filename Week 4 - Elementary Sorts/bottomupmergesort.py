from sort import *
from copy import deepcopy
def bottomUpMergeSort(data, step=step):
	data = deepcopy(data)
	aux = deepcopy(data)

	def merge(a, lo, mid, hi):
		for k in xrange(lo, hi+1):
			aux[k] = a[k]
		i = lo
		j = mid + 1
		for k in xrange(lo, hi+1):
			if i > mid:
				a[k] = aux[j]
				j += 1
			elif j > hi:
				a[k] = aux[i]
				i += 1
			elif aux[j] < aux[i]:
				a[k] = aux[j]
				j += 1
			else:
				a[k] = aux[i]
				i += 1
			step(a)

	N = len(data)
	
	sz = 1
	while sz < N:
		lo = 0
		while lo < N - sz:
			merge(data,lo,lo+sz-1, min(lo+sz+sz-1, N-1))
			lo += sz+sz
		sz = sz+sz


	return data