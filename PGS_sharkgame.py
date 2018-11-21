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
			self.visible = False
			self.game.broadcast("Bite")
			bruce.points += 5
			self.delete = True
			
		
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
			self.visible = False
			self.game.broadcast("Bite Yuck")
			bruce.points -= 10
			self.goto_random()
			self.wait(500)

		
	def broadcast(self, message):
		if message == "Test":
			pass


class shark(scratchSprite):
	def __init__(self, game, x=None, y=None, size=100, costume=None):
		super().__init__(game, x, y, size, costume)

		self.points = 0
		self.reset_costume = 0

	def update(self):
		if self.reset_costume <= 0:
			self.costume = "shark-a.png"
		else:
			self.reset_costume -= 1

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
			self.reset_costume = 10
		if message == "Bite Yuck":
			self.costume = "shark-c.png"
			self.reset_costume = 30


#####################################################################

width = 1000				# Width of the window
height = 600				# Height of the window
game = game(width, height)


game.bg_color = Color("white")		# Background color
game.background = "Underwater.png"	# Background image

#####################################################################
# Add sprites here													#
#####################################################################

stage(game)

bruce = shark(game)
bruce.costume = "shark-a.png"
bruce.rotation_style = "left_right"

bad_fish_one = chasing_bad_fish(game, 100, 100, size=70, costume="fish4.png")

#####################################################################

game.run()