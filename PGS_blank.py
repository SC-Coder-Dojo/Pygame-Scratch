import random
import pygame
from pygame import Color
from pygame.locals import *
from ScratchSprite import *

#####################################################################
# DESIGN YOUR SPRITES												#
#####################################################################

class example_sprite(scratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size=size, costume=costume) # Keep This
		# This code runs when the sprite is created

		# add any new varible for this sprite
		self.health = 100	# Example of a variable


	def update(self):
		# This code runs every frame of the game
		self.move(20)		# x is increasing by 5 every update
		self.turn_right(1)
		self.edge_bounce()


	def broadcast(self, message):
		# This code runs when you broadcast a message
		if message == "Test":
			# This code runs if the message "Test" is broadcast
			pass


class stage(stage):
	def __init__(self, game):
		super().__init__(game)

	def update(self):
		pass


#####################################################################

width = 1000				# Width of the window
height = 600				# Height of the window
game = game(width, height)

game.bg_color = Color("white")		# Background color

#####################################################################
# Add sprites and variable here										#
#####################################################################

stage(game)

# Example cat sprtie
cat = example_sprite(game, 400, 400)	# Create an example_sprite named cat
cat.costume = "Scratch_cat.png"			# Load a costume to the cat
cat.size = 10							# Set the size of the cat


#####################################################################

game.run()