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
		''' *) '''
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



'''
*)

# This is the code people want me to write, but I can't 
int i = root(p);
int j = root(q)

if(sz[i] < sz[j]) { id[i] = j; sz[j] += sz[i];}
else  			  { id[j] = j; sz[i] += sz[j];}

To me this reads like SZSZSZZSZSZSZIISZISIZSIZISZISIZISSIJSJZISJZIJSISJZISJ. 
'''