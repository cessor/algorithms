import pygame
import sys
from copy import deepcopy
import random
from pygame.locals import *

gray = pygame.Color(100, 100, 100)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)


def start():
	chaos = [49, 41, 19, 33, 16, 13, 32, 7, 22, 0, 39, 48, 27, 15, 36, 31, 30, 28, 34, 47, 1, 3, 5, 35, 10, 29, 23, 2, 25, 20, 44, 43, 24, 17, 38, 21, 11, 6, 26, 42, 12, 9, 8, 45, 40, 37, 18, 4, 14, 46]
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
			bar = Bar(size)
			bar.draw(position_x, self.dimensions, self.surface)

#from selectionsort import selectionSort as sort
from insertionsort import insertionSort as sort

if __name__ == "__main__":
	start()