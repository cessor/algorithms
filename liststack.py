class ListStack(object):
	def __init__(self):
		self.head = None

	def push(self, item):
		self.head = (item, self.head)

	def pop(self):
		if self.is_empty(): return None
		value,pointer = self.head
		self.head = pointer
		return value

	def is_empty(self):
		return self.head == None