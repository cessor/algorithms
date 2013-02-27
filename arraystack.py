class ArrayStack(object):
	def __init__(self):
		self.items = []
		self.N = 0

	def push(self, item):
		self.items.append(item)
		self.N = self.N + 1

	def pop(self):
		self.N = self.N - 1
		item = self.items[self.N]
		del self.items[self.N]
		return item

	def is_empty(self):
		return self.N == 0