import pygame


class Snake(object):
	body = []
	turns = {}
	def __init__(self, color, position):
		self.color = color
		self.head = Cube(position)
		self.body.append(self.head)
		self.dirnx = 0
		self.dirny = 1

	def move(self):
		pass

	def reset(self, pos):
		pass

	def addCube(self, surface):
		pass

	def draw(self, surface):
		pass


class Cube(object):
	rows = 0
	w = 0

	def __init__(self, start, dirnx = 1, dirny = 1, color=(255,0,0)):
		pass

	def move(self, dirnx, dirny):
		pass

	def draw(self, color, pos):
		pass


def drawGrid(width, rows, surface):
	size_between = width // rows

	x = 0
	y = 0
	for i in range(rows):
		x = x + size_between
		y = y + size_between

		pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
		pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def redrawWindow(surface):
	global rows, width
	surface.fill((0, 0, 0))
	drawGrid(width, rows, surface)
	pygame.display.update()


def randomSnack(rows, items):
	pass


def message_box(subject, content):
	pass


def main():
	global width, rows
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width))
	s = Snake((255,0,0), (10, 10))
	flag = True

	clock = pygame.time.Clock()

	while flag:
		pygame.time.delay(50)
		clock.tick(10)

		redrawWindow(win)



main()