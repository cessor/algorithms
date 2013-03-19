import sys 
def swap(array, left, right):
	array[left],array[right] = array[right],array[left]

def step(array):
	pass

def printstep(array):
	print array

def load_numbers(filename):
	content = ''
	with open(filename, 'r') as f:
		content = f.read()
		return content.split(',')