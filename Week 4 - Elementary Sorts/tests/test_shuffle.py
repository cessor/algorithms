from nose.tools import *
import random
from shuffle import shuffle

def test_shuffle():
	order = [0, 0, 1, 1, 1, 1, 2, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 11, 11, 12, 12, 13, 14, 14, 15, 16, 16, 16, 16, 16, 17, 18, 18, 19, 19, 19, 19, 20, 20, 20]
	result = shuffle(order)
	assert_not_equal(result, order)