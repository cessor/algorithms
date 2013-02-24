from nose.tools import *
from quickunionweighted import QuickUnionWeighted

Union = QuickUnionWeighted # Rename, motherfucker

def test_union():
	u = Union(10)
	u.union(0,1)
	assert_equal(u.nodes[1], 0)

def test_union():
	u = Union(10)
	u.union(0,1)
	assert_equal(u.root(1), 0)

def test_connections_are_reflexive():
	u = Union(10)
	assert_true(u.connected(0, 0))

def test_nodes_are_their_own_root():
	u = Union(10)
	assert_equal(u.root(0), 0)

def test_two_elements_should_not_be_connected():
	u = Union(10)
	assert_false(u.connected(0,1))

def test_two_elements_should_be_connected():
	u = Union(10)
	u.union(0,1)
	assert_true(u.connected(0,1))

def test_the_connection_is_symmetric():
	u = Union(10)
	u.union(0,1)
	assert_true(u.connected(0,1))
	assert_true(u.connected(1,0))

def test_unconnected_elements_are_trees_of_size_1():
	u = Union(10)
	assert_equal(u.sizes[0], 1)

def test_connected_subtrees_grow_in_size():
	u = Union(10)
	u.union(0, 1)
	assert_equal(u.sizes[0], 2)	

def test_unconnected_elements_are_trees_of_size_3():
	"""
   2     6
  / \   / \
 1   7 0   5 
	"""
	u = Union(10)
#	Left
	u.union(2,1)
	u.union(7,2)

	assert_equal(u.nodes[2], 2)
	assert_equal(u.nodes[1], 2)
	assert_equal(u.nodes[7], 2)

#	Right
	u.union(6, 5)
	u.union(5, 0)
	assert_equal(u.nodes[6], 6)
	assert_equal(u.nodes[0], 6)
	assert_equal(u.nodes[5], 6)

# 	Connect
	"""
   6
  /|\
 0 2 5 
  / \  
 1   7 
	"""
	u.union(6,1)
	assert_equal(u.nodes[2], 6)
	

def test_elements_should_be_transitively_connected():
	"""A deep tree:

	  4 	    7 
	 / \       / \
	0   2     8   9
	   / \   / \
	  1   3 5   6
	"""
	u = Union(10)
	
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

	# Interarboreal Relations
	assert_false(u.connected(1,6))
	assert_false(u.connected(4,7))
	assert_false(u.connected(0,9))


def test_example_from_the_book():
	"""A deep tree:

	  4 	    7 
	 / \       / \
	0   2     8   9
	   / \   / \
	  1   3 5   6
	"""
	u = Union(10)
	u.union(4,3)
	u.union(3,8)
	u.union(6,5)
	u.union(9,4)
	u.union(2,1)
	u.union(5,0)
	u.union(7,2)
	u.union(6,1)
	u.union(7,3)

	control = [6,2,6,4,6,6,6,2,4,4]
	for i,v in enumerate(control):
		assert_equal(v, u.nodes[i])

