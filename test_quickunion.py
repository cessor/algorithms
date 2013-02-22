from nose.tools import *

class QuickUnion(object):
	def __init__(self, elements):
		self.nodes = range(elements)

	def connected(self, a, b):
		return self.root(a) == self.root(b)

	def root(self, element):
		while(self.nodes[element] != element):
			element = self.nodes[element]
		return element

	def union(self, a, b):
		u = self.root(a)
		v = self.root(b)
		self.nodes[v] = u

def test_union():
	u = QuickUnion(10)
	u.union(0,1)
	assert_equal(u.nodes[1], 0)

def test_reflexivity():
	u = QuickUnion(10)
	assert_equal(u.root(0), 0)

def test_union():
	u = QuickUnion(10)
	u.union(0,1)
	assert_equal(u.root(1), 0)

def test_two_elements_should_not_be_connected():
	u = QuickUnion(10)
	assert_false(u.connected(0,1))

def test_two_elements_should_be_connected():
	u = QuickUnion(10)
	u.union(0,1)
	assert_true(u.connected(0,1))



def test_two_elements_elements_should_be_transitively_connected():
	"""A deep tree:

	  4 	    7 
	 / \       / \
	0   2     8   9
	   / \   / \
	  1   3 5   6
	"""
	u = QuickUnion(10)
	
	u.union(2,1)
	u.union(2,3)
	u.union(4,0)
	u.union(4,2)

	u.union(8,5)
	u.union(8,6)
	u.union(7,8)
	u.union(7,9)

	# Left 
	assert_true(u.connected(1,3))
	assert_true(u.connected(2,0))
	assert_true(u.connected(3,4))

	# Right
	assert_true(u.connected(5,6))
	assert_true(u.connected(8,9))
	assert_true(u.connected(7,5))

	#Roots
	assert_equal(u.root(7), 7)
	assert_equal(u.root(5), 7)
	assert_equal(u.root(4), 4)
	assert_equal(u.root(1), 4)

	# Interarboreal Relations
	assert_false(u.connected(1,6))
	assert_false(u.connected(4,7))
	assert_false(u.connected(0,9))