from copy import deepcopy
from sort import step, swap

# This is the cheating version!
def fakeqs(data, step=step):
	if len(data) <= 1:
		return data
	pivot = data.pop()
	left =  [l for l in data if l < pivot]
	right = [r for r in data if r >= pivot]
	temp = quickSort(left, step) + [pivot] + quickSort(right, step)
	step(temp)
	return temp

def quickSort(data, step=step):
	data = deepcopy(data)
	def partition(a,lo, hi):
		i = lo
		j = hi+1
		while True:
			i += 1
			while a[i] < a[lo]:
				if i == hi:
					break
				i += 1

			j -= 1
			while a[lo] < a[j]:
				if j == lo:
					break
				j -= 1

			if i >= j:
				break
			swap(a, i, j)
			step(a)
		swap(a, lo, j)
		step(a)
		return j

	def sort(a, lo, hi):
		if hi <= lo: return
		j = partition(a, lo, hi)
		sort(a, lo, j-1)
		sort(a, j+1, hi)

	sort(data, 0, len(data) - 1)
	return data

#def qs(data, step):
#	data = deepcopy(data)
#	return quickSort(data, step)

#quickSort = qs