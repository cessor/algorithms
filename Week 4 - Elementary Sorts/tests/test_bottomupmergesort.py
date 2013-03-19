from nose.tools import *
from copy import deepcopy
from sort import *
from bottomupmergesort import bottomUpMergeSort as sort

def test_sort():
	chaos = [43,35,48,46,1,18,39,15,13,30,44,11,38,12,40,24,45,49,0,33,16,17,36,21,42,27,32,6,20,9,7,8,28,37,10,25,5,4,31,19,23,2,26,14,29,47,22,41,34,3]
	order = range(50)
	result = sort(chaos)
	assert_equal(result, order)

def test_sort_string():
	chaos = [c for c in 'MERGESORTEXAMPLE']
	order = [c for c in 'AEEEEGLMMOPRRSTX']
	result = sort(chaos)
	assert_equal(result, order)

def test_sort_more():
	t = [73,44,20,50,5,40,82,1,10,53,75,45,92,54,21,79,76,12,13,39,63,95,84,60,11,18,56,97,48,7,23,2,37,89,16,22,24,91,70,3,30,99,25,90,61,69,32,67,59,65,33,77,4,93,94,14,0,9,27,19,49,71,46,57,47,43,74,42,8,88,52,86,41,66,62,83,31,26,78,15,85,68,17,87,38,34,6,80,64,96,55,51,81,35,58,29,28,36,98,72]
	print sort(t)