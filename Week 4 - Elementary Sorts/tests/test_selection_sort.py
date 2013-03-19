from nose.tools import *
from copy import deepcopy
from sort import swap
from selectionsort import selectionSort as sort

def test_sort():
	chaos = [12, 8, 8, 16, 4, 18, 6, 5, 16, 13, 17, 19, 5, 4, 7, 8, 4, 20, 5, 1, 19, 16, 12, 20, 4, 7, 1, 0, 6, 9, 11, 19, 4, 5, 14, 16, 1, 20, 5, 14, 18, 10, 0, 19, 11, 1, 2, 5, 15, 16]
	order = [0, 0, 1, 1, 1, 1, 2, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 11, 11, 12, 12, 13, 14, 14, 15, 16, 16, 16, 16, 16, 17, 18, 18, 19, 19, 19, 19, 20, 20, 20]
	result = sort(chaos)
	assert_equal(result, order)