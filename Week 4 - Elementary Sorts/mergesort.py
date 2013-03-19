from sort import *
from copy import deepcopy
def mergeSort(data, step=step):
	
	def merge(a, aux, lo, mid, hi):
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

	def sort(a, aux, lo, hi):
		if hi <= lo: return
		mid = lo + (hi - lo) / 2
		sort(a, aux, lo, mid)
		sort(a, aux, mid+1, hi)
		merge(a, aux, lo, mid, hi)

	data = deepcopy(data)
	aux = deepcopy(data)
	sort(data, aux, 0, len(data)-1)
	return data