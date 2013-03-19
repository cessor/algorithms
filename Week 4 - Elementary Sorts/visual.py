import pygame
import sys
from copy import deepcopy
import random
from pygame.locals import *
from sort import load_numbers
from shuffle import shuffle

gray = pygame.Color(100, 100, 100)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

def start():
	Visualize(chaos).visualize(sort)

def exit():
	pygame.quit()
	sys.exit()

actions = { 
	K_F5 : start,
	K_q  : exit
}

def handleEvents():
	for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				actions[event.key]()

class Dimensions(object):
	def __init__(self, array):
		maxwidth = 800
		self.max = max(array)
		self.element_count = len(array)
		self.padding = self.space_for_each_element = 6
	 	self.width = self.height = (self.element_count * self.space_for_each_element + self.padding * 2) % maxwidth
	 	self.bar_width = self.space_for_each_element - 2

class Bar(object):
	def __init__(self, height):
		self.height = height

	def draw(self, position_x, dimensions, surface, color = gray):
		x = position_x * dimensions.space_for_each_element + dimensions.padding
		y = (self.height / float(dimensions.max)) * (dimensions.height - 2 * dimensions.padding)
		bottom = (x, dimensions.height - dimensions.padding)
		top = (x, dimensions.height - dimensions.padding - y) 
		pygame.draw.line(surface, color, bottom, top, dimensions.bar_width)

class Visualize(object):
	def __init__(self, array):
		self.array = array
		self.initialize_dimensions()
		self.initialize_graphics()

	def initialize_dimensions(self):
		self.dimensions = Dimensions(self.array)

	def initialize_graphics(self):
		dimensions = self.dimensions
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode((dimensions.width, dimensions.height), HWSURFACE | DOUBLEBUF)
		self.surface.fill(white)

	def visualize(self, sort):
		sort(self.array, self.draw)
		while True:
			handleEvents()

	def draw(self, array): 
		self.surface.fill(white)
		self.drawBars(array)
		pygame.display.flip()
		self.clock.tick(20)

	def drawBars(self, array):
		for position_x,size in enumerate(array):
			handleEvents()
			bar = Bar(int(size))
			bar.draw(position_x, self.dimensions, self.surface)


from selectionsort import selectionSort 
from insertionsort import insertionSort
from shellsort import shellSort
from quicksort import quickSort
from mergesort import mergeSort

algorithms = {
	'selectionSort': selectionSort,
	'insertionSort': insertionSort,
	'shellSort': shellSort,
	'quickSort': quickSort,
	'mergeSort': mergeSort	
}

chaos = shuffle(range(100))

if __name__ == "__main__":
	sort = selectionSort
	if len(sys.argv) == 2:
		param = sys.argv[1]
		sort = algorithms[[key for key in algorithms.keys() if param.lower() in key.lower()][0]]
	else: 
		print 'Algorithms: ', algorithms.keys()
		exit()
	start()