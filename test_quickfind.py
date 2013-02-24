from nose.tools import *

class UnionFind(object):
	def __init__(self, n):
		self.items = range(n)

	def connected(self, p, q):
		return self.items[p] == self.items[q]

	def union(self, p, q): 
		ppointer,qpointer = self.items[p], self.items[q]
		for index,pointer in enumerate(self.items):
			if self.items[index] == ppointer:
				self.items[index] = qpointer

def test_connections_are_reflexive():
	uf = UnionFind(10)
	assert_true(uf.connected(1,1))

def test_connections_are_symmetric():
	uf = UnionFind(10)
	uf.union(0,1)
	assert_true(uf.connected(0,1))
	assert_true(uf.connected(1,0))

def test_connections_are_transitive():
	uf = UnionFind(10)
	uf.union(0,1)
	uf.union(1,2)
	assert_true(uf.connected(0,2))

def test_some_more_elements():
	''' Example as taken from the course
	0  1--2  3--4  
    |     |  |  |
	5--6  7  8  9
	''' 
	uf = UnionFind(10)

	# Connected Component I 
	uf.union(0,5)
	uf.union(5,6)

	# Connected Component II 
	uf.union(1,2)
	uf.union(2,7)

	# Connected Component III 
	uf.union(3,4)
	uf.union(3,8)
	uf.union(4,9)

	# I is not connected to II 
	assert_false(uf.connected(0,1))
	# I is not connected to III 
	assert_false(uf.connected(0,8))
	# II is not connected to III 
	assert_false(uf.connected(1,8))

	# Some transitives
	assert_true(uf.connected(0,6))
	assert_true(uf.connected(1,7))
	assert_true(uf.connected(8,9))

def test_test():
	u = UnionFind(10)
	u.union(0, 7)
	u.union(3, 7)
	u.union(1, 9)
	u.union(7, 6)
	u.union(4, 8)
	u.union(6, 5)
	print u.items