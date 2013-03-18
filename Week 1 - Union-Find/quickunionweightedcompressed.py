class QuickUnionWeightedCompressed(object):
	def __init__(self, elements):
		self.nodes = range(elements)
		self.sizes = [1] * elements

	def connected(self, a, b):
		return self.root(a) == self.root(b)

	def root(self, element):
		if self.nodes[element] == element:
			return element
		return self.root(self.compress(element))

	def compress(self, element):
		self.nodes[element] = self.nodes[self.nodes[element]] 
		return self.nodes[element]

	def union(self, a, b):
		left = self.root(a)
		right = self.root(b)
		if self.sizes[left] < self.sizes[right]:
			child,parent = left,right
		else:
			child,parent = right,left
		self.make(child, point_to = parent)

	def make(self, child, point_to):
		parent = point_to
		self.sizes[parent] += self.sizes[child]
		self.nodes[child] = parent