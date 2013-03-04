import sys
from arraystack import ArrayStack
Stack = ArrayStack

operations = {
	'+' : lambda a,b: a+b,
	'-' : lambda a,b: a-b,
	'*' : lambda a,b: a*b,
	'/' : lambda a,b: a/b,
	'%' : lambda a,b: a%b
}

class Dijkstra(object):
	def __init__(self):
		self.values = Stack()
		self.operators = Stack()

	def __call__(self, str):
		return self.evaluate(str)

	def evaluate(self, str):	
		for c in str:
			if self.is_operator(c):	self.operators.push(c)
			elif c.isdigit():		self.values.push(int(c))
			elif c == ')':			self.perform_operation()
			elif c not in '( ':		self.indicate_error(str, c)
		while not self.operators.is_empty(): 
			self.perform_operation()
		return self.values.pop()

	def is_operator(self, character):
		return character in operations.keys()

	def perform_operation(self):
		b,a = self.values.pop(),self.values.pop()
		operation = operations[self.operators.pop()]
		result = operation(a,b)
		self.values.push(result)

	def indicate_error(self, string, character):
		"""Generates an error message like: 
		Dafuq did I just read?
		( + 1 ( * 5 4 )c )
		---------------^"""
		indicator_arrow = arrow(string, character)
		message = "Dafuq did I just read?\n%s\n%s" % (string, indicator_arrow)
		raise Exception(message)

	def arrow(self, input, character):
		return ''.join((input.index(character)) * ['-']) + '^'

dijkstra = Dijkstra()

if __name__ == '__main__':
	try:
		input = ' '.join(sys.argv[1:])
		print dijkstrasAlgorithm(input)
	except Exception as e:
		print e