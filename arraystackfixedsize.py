class ArrayStackFixedSize(object):
	def __init__(self):
		self.items = [None]
		self.N = 0

	def push(self, item):
		if self.capacity == self.N:
			self.resize(2 * self.capacity)
		self.items[self.N] = item
		self.N += 1

	def resize(self, capacity):
		print 
		print 'Resize to', capacity
		print self.items
		x = [None] * capacity
		print 'new', x
		for i,v in enumerate(self.items):
			x[i] = v
		print x
		self.items = x

	def pop(self):
		if self.is_empty(): return None
		self.N -= 1
		item = self.items[self.N]
		self.items[self.N] = None
		if self.N > 0 and (self.N == self.capacity / 4):
			self.resize(self.capacity / 2)
		print 
		print self.items
		return item

	def is_empty(self):
		return self.N == 0

	def capacity():
	    def fget(self):
	        return len(self.items)
	    return locals()
	capacity = property(**capacity())