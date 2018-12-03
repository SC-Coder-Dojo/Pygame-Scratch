import random
import pygame
from pygame import Color
from pygame.locals import *
from ScratchSprite import *

#####################################################################
# DESIGN YOUR SPRITES												#
#####################################################################

class example_sprite(ScratchSprite):
	def __init__(self, game, x, y):
		super().__init__(game, x, y) # Keep This
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


class Stage(Stage):
	def __init__(self, game):
		super().__init__(game)

	def update(self):
		pass


class fish(ScratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume) # Keep This
		self.start_game = False
		self.hide()

		self.command_list = [[self.move, 20], [self.left, 10]]

	def update(self):
		self.show()

		for com, var in self.command_list:
			com(var)
		

	def broadcast(self, message):
		if message == "Start Game":
			self.show()
			self.start_game = True


class shark(ScratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume)

	def update(self):
		if self.game.keyList[pygame.K_w]:	# if w key pressed
			self.y -= 5
		if self.game.keyList[pygame.K_s]:
			self.y += 5
		if self.game.keyList[pygame.K_a]:
			self.x -= 5
			self.direc = -90
		if self.game.keyList[pygame.K_d]:
			self.x += 5
			self.direc = 90

	def broadcast(self, message):
		if message == "Test":
			pass


#####################################################################


width = 1000				# Width of the window
height = 600				# Height of the window
game = Game(width, height)

game.bg_color = Color("white")		# Background color

#####################################################################
# Add sprites and variable here										#
#####################################################################

example_variable = 10
score = 0

Stage(game)

# Example cat sprtie
# cat = example_sprite(game, 400, 400)	# Create an example_sprite named cat
# #game.add_sprite(cat)					# Add the sprite to the game
# cat.upload_costume("Scratch_cat.png")	# Load a costume to the cat
# cat.rotation_style = "all_around"		# Set the cat rotation style
# cat.size = 10							# Set the size of the cat
# cat.dir = 20							# Set the direction of the cat

shark = shark(game, 400, 400)
shark.costume = "shark-a.png"
shark.rotation_style = "left_right"

good_fish = fish(game, 100, 100)
good_fish.costume = "fish2.png"
good_fish.size = 50

fish_clones = []

for i in range(4):
	fish_clones.append(fish(game, size=30, costume="fish2.png"))
	# fish_clones[i].rotation_style = "left_right"

#####################################################################

game.run()