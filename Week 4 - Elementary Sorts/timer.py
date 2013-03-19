import time


def load_numbers(filename):
	content = ''
	with open(filename, 'r') as f:
		content = f.read()
		return content.split(',')


from selectionsort import selectionSort as sort

numbers = load_numbers('random.txt')
print 'Sorting', len(numbers), 'Numbers'

start = time.time()
result = sort(numbers)
stop = time.time()

print 'Duration:', stop - start
print [v for i,v in enumerate(result) if i < 10],'...'
