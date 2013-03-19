from copy import deepcopy
from sort import step

def quickSort(data, step=step):
	if len(data) <= 1:
		return data
	pivot = data.pop()
	left =  [l for l in data if l < pivot]
	right = [r for r in data if r >= pivot]
	tmp = quickSort(left, step) + [pivot] + quickSort(right, step)
	step(tmp)
	return tmp

#def qs(data, step):
#	data = deepcopy(data)
#	return quickSort(data, step)

#quickSort = qs