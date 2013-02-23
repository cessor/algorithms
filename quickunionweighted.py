class QuickUnionWeighted(object):
	def __init__(self, elements):
		self.nodes = range(elements)
		self.sizes = [1] * elements

	def connected(self, a, b):
		return self.root(a) == self.root(b)

	def root(self, element):
		if self.nodes[element] == element:
			return element
		return self.root(self.nodes[element])

	def union(self, a, b):
		u = self.root(a)
		v = self.root(b)
		self.nodes[v] = u

	def size(self, a):
		return self.sizes[a]