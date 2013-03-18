class ArrayStack(object):
	def __init__(self):
		self.items = []
		self.N = 0

	def push(self, item):
		self.items.append(item)
		self.N += 1

	def pop(self):
		if self.is_empty(): return None
		self.N -= 1
		item = self.items[self.N]
		del self.items[self.N]
		return item

	def is_empty(self):
		return self.N == 0