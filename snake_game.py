import pygame
import random

class Cube():
	width = 500
	rows = 20

	def __init__(self, start, color=(0, 255, 0), direction_x=1, direction_y=0):
		self.position = start
		self.color = color
		self.direction_x = 1
		self.direction_y = 0

	def move(self, direction_x, direction_y):
		self.direction_x = direction_x
		self.direction_y = direction_y
		self.position = (self.position[0] + self.direction_y, self.position[1] + self.direction_x)

	def draw(self, window):
		distance = self.width // self.rows
		row = self.position[1]
		column = self.position[0]
		pygame.draw.rect(window, self.color, (row * distance + 1, column * distance + 1, distance - 1, distance - 1))


class Snake():
	width = 500
	rows = 20
	color = (255, 0, 0)
	body = []

	def __init__(self, start):
		self.position = start
		self.direction_x = 0
		self.direction_y = 0
		self.head = Cube(self.position, self.color, 1, 0)
		self.body.append(self.head)


	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			keys = pygame.key.get_pressed()

			for key in keys:
				if keys[pygame.K_w]:
					self.direction_x = 0
					self.direction_y = -1
				elif keys[pygame.K_s]:
					self.direction_x = 0
					self.direction_y = 1
				elif keys[pygame.K_a]:
					self.direction_x = -1
					self.direction_y = 0
				elif keys[pygame.K_d]:
					self.direction_x = 1
					self.direction_y = 0


		for cube in self.body:
			cube.move(self.direction_x, self.direction_y)
		#self.body[0].move(self.position[0] + self.direction_y, self.position[1] + self.direction_x)
		#self.position = (self.position[0] + self.direction_y, self.position[1] + self.direction_x)

		if self.direction_y == -1 and self.position[0] < 0:
			self.position = (self.rows - 1, self.position[1])
		elif self.direction_y == 1 and self.position[0] >= self.rows:
			self.position = (0, self.position[1])
		elif self.direction_x == -1 and self.position[1] < 0:
			self.position = (self.position[0], self.rows - 1)
		elif self.direction_x == 1 and self.position[1] >= self.rows:
			self.position = (self.position[0], 0)

	def addCube(self):
		tail = self.body[-1]
		self.body.append(Cube((tail.position[0], tail.position[1])))
		#tail_x = tail.

	def draw(self, window):
		for i, c in enumerate(self.body):
			c.draw(window)


def draw_grid(width, rows, window):
	gap = width // rows
	x_pos = 0
	y_pos = 0
	for line in range(rows):
		x_pos = x_pos + gap
		y_pos = y_pos + gap
		pygame.draw.line(window, (255, 255, 255), (x_pos, 0), (x_pos, width))
		pygame.draw.line(window, (255, 255, 255), (0, y_pos), (width, y_pos))


def random_snack(rows):
	x = random.randrange(rows)
	y = random.randrange(rows)
	return (x, y)


def redraw_window(window):
	global rows, width,snake, snack
	window.fill((0, 0, 0))
	snake.draw(window)
	#snack.draw(window)
	draw_grid(width, rows, window)
	pygame.display.update()


def main():
	global width, rows, window, snake, snack
	width = 500
	rows = 20
	window = pygame.display.set_mode((width, width))
	snake = Snake((5, 5))
	snack = Cube(random_snack(rows), (0, 255, 0), 1, 0)
	flag = True
	clock = pygame.time.Clock()

	while flag:
		pygame.time.delay(50)
		clock.tick(10)
		snake.move()

		if snake.position == snack.position:
			#snake.addCube()
			snack = Cube(random_snack(rows), (0, 255, 0), 1, 0)

		redraw_window(window)


main()
