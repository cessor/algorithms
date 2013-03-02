import sys
from arraystack import ArrayStack
Stack = ArrayStack

map = {
	'+' : lambda a,b: a+b,
	'-' : lambda a,b: a-b,
	'*' : lambda a,b: a*b,
	'/' : lambda a,b: a/b,
	'%' : lambda a,b: a%b,
}

def dijkstrasAlgorithm(str):
	values = Stack()
	operators = Stack()
	available_operators = map.keys()
	for c in str:
		if c in available_operators: 
			operators.push(c)
		elif c.isdigit(): 		
			values.push(int(c))
		elif c == ')':
			b,a = values.pop(),values.pop()
			result = map[operators.pop()](a,b)
			values.push(result)
		elif c not in '( ':
			arrow_to_show_error = ''.join((str.index(c) - 1) * ['-'])
			message = 'Dafuq did I just read?\n%s\n%s^' % (str, arrow_to_show_error)
			raise Exception(message, c)
	return values.pop()

if __name__ == '__main__':
	try:
		input = ' '.join(sys.argv[1:])
		print dijkstrasAlgorithm(input)
	except Exception as e: 
		print e.message