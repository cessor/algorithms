from nose.tools import *

class QuickUnion(object):
	def __init__(self, n):
		self.items = range(n)

	def root(self, index):
		while not index == self.items[index]:
			index = self.items[index]
		return index

	def connected(self, p, q):
		return self.root(p) == self.root(q)

	def union(self, p, q): 
		i,j = self.root(p), self.root(q)
		self.items[i] = j

def test_connections_are_reflexive():
	qu = QuickUnion(10)
	assert_true(qu.connected(1,1))

def test_connections_are_symmetric():
	qu = QuickUnion(10)
	qu.union(0,1)
	assert_true(qu.connected(0,1))
	assert_true(qu.connected(1,0))

def test_connections_are_transitive():
	qu = QuickUnion(10)
	qu.union(0,1)
	qu.union(1,2)
	assert_true(qu.connected(0,2))

def test_some_more_elements():
	''' Example as taken from the course
	0  1--2  3--4  
    |     |  |  |
	5--6  7  8  9
	''' 
	qu = QuickUnion(10)

	# Connected Component I 
	qu.union(0,5)
	qu.union(5,6)

	# Connected Component II 
	qu.union(1,2)
	qu.union(2,7)

	# Connected Component III 
	qu.union(3,4)
	qu.union(3,8)
	qu.union(4,9)

	# I is not connected to II 
	assert_false(qu.connected(0,1))
	# I is not connected to III 
	assert_false(qu.connected(0,8))
	# II is not connected to III 
	assert_false(qu.connected(1,8))

	# Some transitives
	assert_true(qu.connected(0,6))
	assert_true(qu.connected(1,7))
	assert_true(qu.connected(8,9))

