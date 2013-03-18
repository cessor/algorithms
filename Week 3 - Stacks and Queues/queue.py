class Queue(object):
	def __init__(self):
		self.first = None
		self.last = None

	def enque(self, value):
		oldlast = self.last
		self.last = [value, None]

		if self.is_empty():
			self.first = self.last
		else:
			oldlast[1] = self.last

	def deque(self):
		value,self.first = self.first
		if self.is_empty():
			self.last = None
		return value

	def is_empty(self):
		return self.first == None