class ListStack(object):
	def __init__(self):
		self.head = None

	def push(self, value):
		self.head = (value, self.head)

	def pop(self):
		if self.is_empty(): return None
		value,self.head = self.head
		return value

	def is_empty(self):
		return self.head == None