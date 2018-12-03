import random
import pygame
from pygame import Color
from pygame.locals import *
from ScratchSprite import *

#####################################################################
# DESIGN YOUR SPRITES												#
#####################################################################


class Stage(Stage):
	def __init__(self, game):
		super().__init__(game)
		self.time = 5000

	def update(self):
		self.time -= 1


class car_one(ScratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume)

		self.points = 0
		self.speed = 0

	def update(self):
		self.show()
		self.move(10 + self.speed)
		if self.game.keyList[K_w]:	# if w key pressed
			self.speed = 5
		elif self.game.keyList[K_s]:
			self.speed = -5
		else:
			self.speed = 0
		if self.game.keyList[K_a]:
			self.direc -= 3 - self.speed / 5
		if self.game.keyList[K_d]:
			self.direc += 3 - self.speed / 5

		if self.touching(racecourse):
			self.hide()
			self.goto(380, 520)
			self.direc = 90
			self.wait(100)


class car_two(ScratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume)

		self.points = 0
		self.speed = 0

	def update(self):
		self.show()
		self.move(10 + self.speed)
		if self.game.keyList[K_UP]:	# if w key pressed
			self.speed = 5
		elif self.game.keyList[K_DOWN]:
			self.speed = -5
		else:
			self.speed = 0
		if self.game.keyList[K_LEFT]:
			self.direc -= 3 - self.speed / 5
		if self.game.keyList[K_RIGHT]:
			self.direc += 3 - self.speed / 5

		if self.touching(racecourse):
			self.hide()
			self.goto(440, 540)
			self.direc = 90
			self.wait(100)


class course(ScratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume)

	def update(self):
		pass

	def broadcast(self, message):
		if message == "Test":
			pass


#####################################################################

width = 1000				# Width of the window
height = 600				# Height of the window
game = Game(width, height)


game.bg_color = Color("white")		# Background color
game.background = "Racetrack.png"

game.show_hit_box = False	# For Testing purposes

#####################################################################
# Add sprites here													#
#####################################################################

Stage(game)

racecourse = course(game, 0, 0)
racecourse.costume = "Racetrack2.png"

red_car = car_one(game, 380, 520)
red_car.costume = "red_car.png"
red_car.size = 10

blue_car = car_two(game, 440, 540)
blue_car.costume = "blue_car.png"
blue_car.size = 10


#####################################################################

game.run()