from nose.tools import *
import sys
from arraystack import ArrayStack
from dijkstra import dijkstra

dijkstrasAlgorithm = dijkstra
Stack = ArrayStack

def test_addition():
	code = '(1 + 1)'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, 2)

def test_dijkstra_more():
	code = '(2 + 2)'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, 4)

def test_multiply():
	code = '(2 * 6)'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, 12)

def test_substract():
	code = '(2 - 2)'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, 0)

def test_substract_order_positive():
	code = '(4 - 2)'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, 2)

def test_substract_order_negative():
	code = '(2 - 4)'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, -2)

def test_divide():
	code = '(2 / 2)'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, 1)

def test_mod():
	code = '(2 % 2)'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, 0)

@raises(Exception)
def test_mod():
	code = '(2 % 2) g'
	result = dijkstrasAlgorithm(code)
	result(assert_raises, 0)

def test_items_from_course():
	code = '(1 + (2 + 3) * (4 * 5)))'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, 101)

def test_brackets_are_not_necessary():
	code = ' 1 + 2'
	result = dijkstrasAlgorithm(code)
	assert_equal(result, 3)