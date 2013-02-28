from nose.tools import *
from queue import Queue

def test_new_Queue_is_empty():
	q = Queue()
	assert_true(q.is_empty())

def test_enque():
	q = Queue()
	q.enque(1)
	assert_false(q.is_empty())

def test_deque():
	q = Queue()
	q.enque(1)
	assert_equal(q.deque(), 1)
	assert_true(q.is_empty())


def test_deque_many_elements():
	q = Queue()
	q.enque(1)
	q.enque(2)
	q.enque(3)
	q.enque(4)
	assert_equal(q.deque(), 1)
	assert_equal(q.deque(), 2)
	assert_equal(q.deque(), 3)
	assert_equal(q.deque(), 4)	