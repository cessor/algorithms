import time
from shuffle import shuffle

from selectionsort import selectionSort 
from insertionsort import insertionSort
from shellsort import shellSort
from quicksort import quickSort, fakeqs
from mergesort import mergeSort
from bottomupmergesort import bottomUpMergeSort

algorithms = {
	'selectionSort': selectionSort,
	'insertionSort': insertionSort,
	'shellSort': shellSort,
	'quickSort': quickSort,
	'fakeqs': fakeqs,
	'mergeSort': mergeSort,
	'bottomUpMergeSort': bottomUpMergeSort	
}

def simulate(algorithm):
	numbers = shuffle(range(100000))
	start = time.time()
	algorithm(numbers)
	stop = time.time()
	return stop - start

stats = {} 

for name,algorithm in algorithms.items():
	print 'Running',name
	durations = []
	for i in range(25):
		print '.', 
		durations.append(simulate(algorithm))
	print
	stats[name] = sum(durations) / 25.0

print
print 'Done. Results: '

for name in algorithms.keys():
	print '\t',name,':\t', stats[name]