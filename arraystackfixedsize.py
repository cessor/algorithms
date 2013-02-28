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
		temp = [None] * capacity
		for index,value in enumerate(self.items):
			if value == None: continue
			temp[index] = value
		self.items = temp

	def pop(self):
		if self.is_empty(): return None
		self.N -= 1
		item = self.items[self.N]
		self.items[self.N] = None
		if self.N >= 0 and self.N == self.capacity // 4:
			self.resize(self.capacity // 2)
		return item

	def is_empty(self):
		return self.N == 0

	def capacity():
	    def fget(self):
	        return len(self.items)
	    return locals()
	capacity = property(**capacity())