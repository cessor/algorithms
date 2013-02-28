class Queue(object):
	def __init__(self):
		self.first = None
		self.last = None

	def enque(self, value):
		oldlast = self.last
		self.last = (value, None)
		oldlast[1] = self.last

	def deque(self):
		value,self.first = self.first
		return value

	def is_empty(self):
		return self.last == self.first == None