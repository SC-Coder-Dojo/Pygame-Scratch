import random
import pygame
from pygame import Color
from pygame.locals import *
from ScratchSprite import *

#####################################################################
# DESIGN YOUR SPRITES												#
#####################################################################


class stage(stage):
	def __init__(self, game):
		super().__init__(game)

	def update(self):
		fish(game, size=50, costume="fish2.png")
		self.wait(1000)


class fish(scratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume) # Keep This
		self.hide()
		self.goto_random()

	def update(self):
		self.show()
		
		if self.distance_to(bruce) < 120:
			self.point_towards(bruce)
			self.right(180)
		else:
			self.right(random.randrange(-1, 1))

		self.move(8)
		self.edge_bounce()

		if self.touching(bruce):
			self.game.broadcast("Bite")
			self.delete = True
			bruce.points += 5
		
	def broadcast(self, message):
		if message == "Test":
			pass


class chasing_bad_fish(scratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume) # Keep This
		self.hide()

	def update(self):
		self.show()
		
		if self.distance_to(bruce) < 200:
			self.point_towards(bruce)
		else:
			self.right(random.randrange(-1, 1))

		self.move(5)
		self.edge_bounce()

		if self.touching(bruce):
			self.hide()
			self.goto_random()
			bruce.points -= 10
			self.wait(500)

		
	def broadcast(self, message):
		if message == "Test":
			pass


class shark(scratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume)

		self.points = 0

	def update(self):
		if self.game.keyList[K_w]:	# if w key pressed
			self.y -= 5
		if self.game.keyList[K_s]:
			self.y += 5
		if self.game.keyList[K_a]:
			self.x -= 5
			self.direc = -90
		if self.game.keyList[K_d]:
			self.x += 5
			self.direc = 90

	def broadcast(self, message):
		if message == "Bite":
			self.costume = "shark-b.png"
			print("Chomp")


#####################################################################

width = 1000				# Width of the window
height = 600				# Height of the window
game = game(width, height)


game.bg_color = Color("white")		# Background color
game.background = "Underwater.png"	# Background image

# game.show_hit_box = True

#####################################################################
# Add sprites here													#
#####################################################################

stage(game)

bruce = shark(game)
bruce.costume = "shark-b.png"
bruce.costume = "shark-a.png"
bruce.rotation_style = "left_right"

# good_fish_one = fish(game)
# good_fish_one.costume = "fish2.png"
# good_fish_one.size = 50

# for i in range(5):
# 	fish(game, size=50, costume="fish2.png")

bad_fish_one = chasing_bad_fish(game, 100, 100, size=70, costume="fish4.png")

#####################################################################

game.run()