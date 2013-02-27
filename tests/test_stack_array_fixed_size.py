from nose.tools import *
from arraystackfixedsize import ArrayStackFixedSize

Stack = ArrayStackFixedSize

def test_new_stack_is_empty():
	s = Stack(10)
	assert_true(s.is_empty())

def test_an_element_can_be_pushed_on_the_stack():
	s = Stack(10)
	s.push(1)
	assert_false(s.is_empty())

def test_two_elements_can_be_pushed_on_the_stack():
	s = Stack(10)
	s.push(1)
	s.push(2)
	assert_equal(s.pop(), 2)
	assert_equal(s.pop(), 1)
	assert_true(s.is_empty())

def test_underflow_cant_pop_empty_stack():
	s = Stack(10)
	assert_equal(s.pop(), None)

def test_an_element_can_be_popped_from_the_stack():
	s = Stack(10)
	s.push(5)
	x = s.pop()
	assert_equal(x, 5)

def test_lines_from_course():
	s = Stack(10)	
	buffer = []
	dsl = 'to be or not to - be - - that - - - is'.split()
	for word in dsl:
		if word == '-':
			buffer.append(s.pop())
		else:
			s.push(word)
	assert_equal(' '.join(buffer), 'to be not that or be')
	print s.items, s.N