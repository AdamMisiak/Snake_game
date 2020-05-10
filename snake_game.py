import pygame
import random


class Snake(object):
	body = []
	turns = {}

	def __init__(self, color, position):
		pass

	def move(self):
		pass

	def reset(self, pos):
		pass

	def addCube(self, surface):
		pass


	def draw(self, surface):
		pass


class Cube(object):

	def __init__(self, start, dirnx = 1, dirny = 1, color=(255,0,0)):
		pass

	def move(self, dirnx, dirny):
		pass

	def draw(self, surface, eyes=False):
		pass


def drawGrid(width, rows, window):
	gap = width // rows
	x_pos = 0
	y_pos = 0
	for line in range(rows):
		x_pos = x_pos + gap
		y_pos = y_pos + gap
		pygame.draw.line(window, (255, 255, 255), (x_pos, 0), (x_pos, width))
		pygame.draw.line(window, (255, 255, 255), (0, y_pos), (width, y_pos))

def redrawWindow(window):
	window.fill((0,0,0))
	drawGrid(width, rows, window)
	pygame.display.update()

def randomSnack(rows, item):
	pass

def message_box(subject, content):
	pass


def main():
	global width, rows, window
	width = 500
	rows = 20
	window = pygame.display.set_mode((width, width))
	flag = True

	clock = pygame.time.Clock()

	while flag:
		pygame.time.delay(50)
		clock.tick(10)
		redrawWindow(window)





main()