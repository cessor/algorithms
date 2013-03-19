import pygame
import sys
from copy import deepcopy
import random
from pygame.locals import *

gray = pygame.Color(100, 100, 100)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)


def swap(array, left, right):
	array[left],array[right] = array[right],array[left] 

def selectionSort(data, step = lambda data: data):
	data = deepcopy(data)
	for i in range(len(data)):
		min = i
		for j in range(i+1, len(data)):
			if data[j] < data[min]:
				min = j
		swap(data, i, min)
		step(data)
	return data

def handleEvents():
	for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

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

	def draw(self, position_x, dimensions, surface):
		x = position_x * dimensions.space_for_each_element + dimensions.padding
		y = (self.height / float(dimensions.max)) * (dimensions.height - 2 * dimensions.padding)
		bottom = (x, dimensions.height - dimensions.padding)
		top = (x, dimensions.height - dimensions.padding - y) 
		pygame.draw.line(surface, gray, bottom, top, dimensions.bar_width)

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

	def visualize(self):
		selectionSort(chaos, self.draw)
		while True:
			handleEvents()

	def draw(self, array): 
		self.surface.fill(white)
		for position_x,size in enumerate(array):
			handleEvents()
			bar = Bar(size)
			bar.draw(position_x, self.dimensions, self.surface)
			pygame.display.flip()
		self.clock.tick(20)
		
if __name__ == "__main__":
	
	chaos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
	chaos.reverse()
	Visualize(chaos).visualize()


	#x = random.randint(0,width)
	#y = random.randint(0,height)

	
	
	