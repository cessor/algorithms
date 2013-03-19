from nose.tools import *
from copy import deepcopy
from sort import swap,step
from insertionsort import insertionSort

sort = insertionSort

def test_sort():
	#chaos = [6,8,5,3,2,1,4,0,9,7]
	#order = [0,1,2,3,4,5,6,7,8,9]

	chaos = [c for c in 'SORTEXAMPLE']
	order = [c for c in 'AEELMOPRSTX']
	result = sort(chaos)
	assert_equal(result, order)