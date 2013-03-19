from sort import swap
from random import randint
from copy import deepcopy

def shuffle(data):
	data = deepcopy(data)
	length = len(data)
	for index in xrange(length):
		random_position = randint(0, index)
		swap(data, index, random_position)
	return data