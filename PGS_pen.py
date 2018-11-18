import random
import pygame
from pygame import Color
from ScratchSprite import *

#####################################################################
# DESIGN YOUR SPRITES												#
#####################################################################


class stage(stage):
	def __init__(self, game):
		super().__init__(game)

	def update(self):
		pass


class turtle(scratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume)

		self.pen_down()
		self.num = 6

	def update(self):
		if self.num > 0:
			self.angle = random.randint(70, 100)
			for i in range(20, 300):
				self.move(i)
				self.left(self.angle)
			self.pen = False
			self.goto_random()
			self.pen = True
			self.num -= 1


#####################################################################

width = 1000				# Width of the window
height = 800				# Height of the window
game = game(width, height)

game.bg_color = Color("white")		# Background color

#####################################################################
# Add sprites here													#
#####################################################################

stage(game)

bob = turtle(game)
bob.costume = "turtle.png"
bob.size = 50

#####################################################################

game.run()