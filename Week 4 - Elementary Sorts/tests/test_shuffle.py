from nose.tools import *
from copy import deepcopy
import random
from sort import swap

def shuffle(data):
	data = deepcopy(data)
	length = len(data)
	for index in xrange(length):
		random_position = random.randint(0, index)
		swap(data, index, random_position)
	return data

def test_sort():
	order = [0, 0, 1, 1, 1, 1, 2, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 11, 11, 12, 12, 13, 14, 14, 15, 16, 16, 16, 16, 16, 17, 18, 18, 19, 19, 19, 19, 20, 20, 20]
	order = range(10)
	result = shuffle(order)
	assert_not_equal(result, order)