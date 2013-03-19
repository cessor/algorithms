from nose.tools import *
from copy import deepcopy
from sort import *
from quicksort import quickSort

sort = quickSort

def test_sort():
	chaos = [43,35,48,46,1,18,39,15,13,30,44,11,38,12,40,24,45,49,0,33,16,17,36,21,42,27,32,6,20,9,7,8,28,37,10,25,5,4,31,19,23,2,26,14,29,47,22,41,34,3]
	order = range(50)
	result = sort(chaos)
	assert_equal(result, order)