class Queue(object):
	def __init__(self):
		self.first = None
		self.last = None

	def enque(self, value):
		if self.is_empty():
			self.first = self.last = (value, None)
		self.last = (value, self.last)

	def deque(self):
		value = self.first[0]
		self.first = None
		return value

	def is_empty(self):
		return self.last == self.first == None