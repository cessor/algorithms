from nose.tools import *
from arraystackfixedsize import ArrayStackFixedSize

Stack = ArrayStackFixedSize

def test_new_stack_is_empty():
	s = Stack()
	assert_true(s.is_empty())
	assert_equal(s.capacity, 1)

def test_an_element_can_be_pushed_on_the_stack():
	s = Stack()
	s.push(1)
	assert_false(s.is_empty())

def test_an_element_can_be_popped_from_the_stack():
	s = Stack()
	s.push(5)
	x = s.pop()
	assert_equal(x, 5)

def test_two_elements_can_be_pushed_on_the_stack():
	s = Stack()
	s.push(1)
	s.push(2)
	assert_equal(s.pop(), 2)
	assert_equal(s.pop(), 1)
	assert_true(s.is_empty())

def test_underflow_cant_pop_empty_stack():
	s = Stack()
	assert_equal(s.pop(), None)

def test_a_full_stack_should_resize():
	s = Stack()
	assert_equal(s.capacity, 1)
	s.push(1)
	assert_equal(s.capacity, 1)
	s.push(2)
	assert_equal(s.capacity, 2)
	s.push(3)
	assert_equal(s.capacity, 4)
	s.push(4)
	assert_equal(s.capacity, 4)
	s.push(5)
	assert_equal(s.capacity, 8)

def test_a_draining_stack_should_shrink():
	
	# Filling: _ (None)
	s = Stack() 				# _ 				(1)
	s.push(1) 					# 1 				(1)
	s.push(2)					# 1 2 				(2)
	s.push(3)					# 1 2 3 _			(4)
	s.push(4)					# 1 2 3 4			(4)
	s.push(5)					# 1 2 3 4 5 _ _ _   (8)
	assert_equal(s.capacity, 8) # 1 2 3 4 5 _ _ _ 	(8)
	assert_equal(s.pop(), 5) 	# 1 2 3 4 _ _ _ _ 	(8)
	assert_equal(s.pop(), 4)	# 1 2 3 _ _ _ _ _ 	(8)
	assert_equal(s.pop(), 3) 	# 1 2 _ _ _ _ _ _ 	(8) --> Resize
	assert_equal(s.capacity, 4) # 1 2 _ _ 			(4) --> Resize
	assert_equal(s.pop(), 2)	# 1 _ _ _ 			(4) --> Resize
	assert_equal(s.capacity, 2) # 1 _  				(2) --> Resize
	assert_equal(s.pop(), 1)	# 1   				(1)
	assert_equal(s.capacity, 1) # _					(1)
	assert_true(s.is_empty())

		
def test_lines_from_course():
	s = Stack()	
	buffer = []
	dsl = 'to be or not to - be - - that - - - is'.split()
	for word in dsl:
		if word == '-':
			buffer.append(s.pop())
		else:
			s.push(word)
	assert_equal(' '.join(buffer), 'to be not that or be')