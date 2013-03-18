class QuickFindUF(object):
	def __init__(self, n):
		self.items = range(n)

	def connected(self, p, q):
		return self.items[p] == self.items[q]

	def union(self, p, q): 
		ppointer,qpointer = self.items[p], self.items[q]
		for index,pointer in enumerate(self.items):
			if self.items[index] == ppointer:
				self.items[index] = qpointer