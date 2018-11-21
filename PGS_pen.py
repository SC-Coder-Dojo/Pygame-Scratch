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
		self.num = 1

	def update(self):
		angle = 89

		self.move(self.num)
		self.left(angle)

		self.num += 1


#####################################################################

width = 1000				# Width of the window
height = 600				# Height of the window
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