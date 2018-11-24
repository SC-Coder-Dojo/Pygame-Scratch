import pygame
from pygame import Color
import math
import os
import random
import time
from copy import copy

#########################################################################################
# game Class                                                                            #
#########################################################################################

class game():
	def __init__(self, width, height, background=None):
		self.sprites = []
		self.mainLoop = True
		self.width = width
		self.height = height
		self.size = (self.width, self.height)
		self.win = pygame.display.set_mode((width, height))
		self.clock = pygame.time.Clock()
		self.FPS = 60
		self.bg_color = Color("white")
		self.background = background
		self.keyList = None
		self.stage = None

		self.frame_count = 0

		self.pen_surface = pygame.surface.Surface((width, height))
		self.pen_surface.fill(Color("white"))

		self.show_hit_box = False

		self.default_costume = None
		self.load_default_costume()

		self.text_box_list = []


	@property
	def w(self):
		return self.width

	@property
	def h(self):
		return self.height
	
	@property
	def time(self):
		return pygame.time.get_ticks()
	
	@property
	def background(self):
		return self._background


	@background.setter
	def background(self, background):
		if background is None:
			self._background = background
		else:
			background_path = os.path.join("Background", background)
			if os.path.isfile(background_path):
				self._background = pygame.image.load(background_path)
				try:
					self._background = pygame.transform.smoothscale(self.background, self.size)
				except:
					self._background = pygame.transform.scale(self.background, self.size)
				self.pen_surface.blit(self.background, (0, 0))
			else:
				print("Background image {} missing, try:".format(background))
				list_backgrounds = os.listdir("Background")
				del list_backgrounds[-1]
				print(list_backgrounds)
	

	def run(self):
		pygame.init()
		while self.mainLoop:
			self.clock.tick(self.FPS)
			self.frame_count += 1
			self.events()
			self.update()
			self.sprites_draw()

	def broadcast(self, message):
		for s in self.sprites:
			s.broadcast(message)

	def events(self):
	    self.keyList = pygame.key.get_pressed()
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            self.mainLoop = False
	        if self.keyList[pygame.K_ESCAPE]:
	            self.mainLoop = False

	def update(self):
		if self.stage:
			if self.stage.waiting:
				self.stage.wait_tick()
			else:
				self.stage.update()

		for s in self.sprites:
			if s.waiting:
				s.wait_tick()
			else:
				s.update()
			if s.delete:
				self.sprites.remove(s)

	def sprites_draw(self):
		if self.background is None:
			self.win.fill(self.bg_color)
		else:
			self.win.blit(self.background, (0, 0))

		self.win.blit(self.pen_surface, (0, 0))

		for s in self.sprites:
			s.draw(self.win)

		for tb in self.text_box_list:
			tb.draw(self.win)

		pygame.display.update()	

	def add_sprite(self, sprite):
		self.sprites.append(sprite)

	def load_default_costume(self):
		default_costume = os.path.join("Costumes", "Scratch_Cat.png")

		if os.path.isfile(default_costume):
			self.default_costume = pygame.image.load(default_costume).convert_alpha()
		else:
			print("Scratch_Cat missing from \\Costumes folder")
			print("	 Make sure you have a Costumes folder")
			print("  that contains .png files of your costumes")


#########################################################################################
# scratchSprite Class                                                                   #
#########################################################################################


class scratchSprite():
	rotation_style = ["all_around", "left_right", "no_rotation"]

	def __init__(self, 
				 game, 
				 x=None, 
				 y=None, 
				 size=100, 
				 costume="Scratch_Cat.png", 
				 direc=90, 
				 color=(0,0,0)):
		
		self.game = game
		self.game.add_sprite(self)

		# Rectangle
		self.rect = pygame.Rect((0, 0), (100, 100))
		if x and y:
			self.x = x
			self.y = y
		else:
			self.center()

		self._direc = 90
		self._size = 100

		#Looks
		self.costumes = {}

		default_costume = "Scratch_Cat.png"
		self.load_costume(default_costume)

		self.costume = costume
		

		self.size = size
		self.direc = direc
		self.current_size = copy(self.size)

		self.pen = False
		self.pen_color = (0, 0, 0)
		self.pen_size = 1
		self.pen_shade = 1

		self.color = color
		
		self.rotation_style = "all_around"
		self.visible = True

		self.delete = False

		self.wait_time = 0
		self.waiting = False


	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def pos(self):
		return (int(self.x), int(self.y))
	
	@property
	def size(self):
		return self._size

	@property
	def costume(self):
		return self._costume

	@property
	def direc(self):
		return self._direc
	
	
	
	@x.setter
	def x(self, x):
		self.rect.centerx = x
		self._x = x

	@y.setter
	def y(self, y):
		self.rect.centery = y
		self._y = y

	@size.setter
	def size(self, size):
		# ADD SETTER TO SIZE
		self._size = size
		self.size_costume()

	@costume.setter
	def costume(self, costume_name):
		if costume_name is None:
			if self.game.default_costume is not None:
				self.costumes["Scratch_Cat.png"] = self.game.default_costume
				self._costume = self.costumes["Scratch_Cat.png"]
			else:
				self._costume = None
		elif costume_name in self.costumes:
			self._costume = self.costumes[costume_name]
		else:
			self.load_costume(costume_name)

		self.costume_rect = self.costume.get_rect()
		self.size_costume()
		self.rotate_costume()

	@direc.setter
	def direc(self, direc):
		direc = (direc + 180) % 360 - 180
		self._direc = direc
		self.rotate_costume()
	

	def load_costume(self, costume_name):
		costume_path = os.path.join("Costumes", costume_name)

		if os.path.isfile(costume_path):
			self.costumes[costume_name] = pygame.image.load(costume_path).convert_alpha()
			self._costume = self.costumes[costume_name]
		else:
			print("Invalid costume name {}, try".format(costume_name))
			list_costumes = os.listdir("Costumes")
			del list_costumes[-1]
			print(list_costumes)

			if self.game.default_costume is not None:
				self.costumes["Scratch_Cat.png"] = self.game.default_costume
				self._costume = self.costumes["Scratch_Cat.png"]
			else:
				self._costume = None


	def update(self):
		# Blank update function, for testing
		pass 

	def draw(self, win):
		if self.visible:
			if self.costume != None:
				# Blit costume to screen
				win.blit(self.costume_blit, self.rect.topleft)
			else:
				# Draw a rectangle to the screen
				default_rect = (self.rect.x, self.rect.y, 30, 30)
				pygame.draw.rect(win, Color("blue"), default_rect)

		if self.game.show_hit_box:
			rect_draw = (self.rect.x, self.rect.y, self.rect.w, self.rect.h)
			pygame.draw.rect(win, Color("red"), rect_draw, 3)
			pygame.draw.circle(win, Color("red"), self.pos, 3)
		else:
			# Invisible
			pass

	def size_costume(self):
		scale_w = int(self.costume_rect.w * self.size / 100)
		scale_h = int(self.costume_rect.h * self.size / 100)
		scale = (scale_w, scale_h)
		
		if self.size != 100:
			try:
				self.costume_size = pygame.transform.smoothscale(self.costume, scale)
			except:
				self.costume_size = pygame.transform.scale(self.costume, scale)
		else:
			self.costume_size = copy(self.costume)

		self.costume_blit = copy(self.costume_size)
		
		self.mask_align()
		

	def rotate_costume(self):
		if self.rotation_style == "no_rotation":
			self.costume_blit = copy(self.costume_size)
		elif self.rotation_style == "left_right":
			if -180 < self.direc < 0:
				self.costume_blit = pygame.transform.flip(self.costume_size, 1, 0)
			else:
				self.costume_blit = copy(self.costume_size)
		else:
			rotate_angle = (self.direc - 90) * -1
			self.costume_blit = pygame.transform.rotate(self.costume_size, rotate_angle)
		
		self.mask_align()


	# Looks

	def show(self):
		self.visible = True

	def hide(self):
		self.visible = False

	def mask_align(self):
		self.rect.size = self.costume_blit.get_rect().size
		self.mask = pygame.mask.from_surface(self.costume_blit)
		self.rect.center = self.pos
		

	# Motion

	def move(self, steps):
		self.start_pen = self.pos

		moveX, moveY = scratchSprite.from_angle(self.direc)
		self.x += int(moveX * steps / 2)
		self.y += int(moveY * steps / 2)

		if self.pen:
			self.pen_line()


	def turn_right(self, deg):
		self.direc += deg

	def right(self, deg):
		self.turn_right(deg)

	def turn_left(self, deg):
		self.direc -= deg

	def left(self, deg):
		self.turn_left(deg)

	def point_in_direc(self, deg):
		self.direc = deg % 360

	def point_towards(self, other):
		self.point_in_direc(self.direction_to(other))

	def goto(self, x, y=None):
		if y is None:
			self.x, self.y = x
		else:
			self.x = x
			self.y = y

	def goto_random(self):
		self.x, self.y = self.random_pos()

	def random_pos(self):
		border = int(math.sqrt(self.rect.w**2 + self.rect.h**2))
		rand_x = random.randint(border, self.game.w - border)
		rand_y = random.randint(border, self.game.h - border)
		return (rand_x, rand_y)

	def center(self):
		self.x = self.game.w / 2
		self.y = self.game.h / 2


	def edge_bounce(self):
		padding = -10
		if self.rect.left <= padding:
			self.direc *= -1
			self.x += 5

		if self.rect.right >= self.game.w - padding:
			self.direc *= -1
			self.x -= 5

		if self.rect.top <= padding:
			if self.direc > 0:
				self.direc = 180 - self.direc
			else:
				self.direc = -180 - self.direc
			self.y += 5

		if self.rect.bottom >= self.game.h - padding:
			if self.direc > 0:
				self.direc = 180 - self.direc
			else:
				self.direc = -180 - self.direc
			self.y -= 5

	def edge_collision(self):
		if self.rect.right >= self.game.w:
			return True
		if self.rect.left <= 0:
			return True
		if self.rect.bottom >= self.game.height:
			return True
		if self.rect.top <= 0:
			return True
		return False

	def distance_to(self, other):
		dist_x = other.rect.centerx - self.rect.centerx
		dist_y = other.rect.centery - self.rect.centery
		distance = math.sqrt(dist_x ** 2 + dist_y ** 2)
		return distance

	def touching(self, other):
		if self.rect.colliderect(other.rect) and self.visible:
			# Pixel perfect collision
			offset = (other.rect.x - self.rect.x, other.rect.y - self.rect.y)
			result = self.mask.overlap(other.mask, offset)
			if result is None:
				return False
			else:
				return True
		else:
			return False

	def broadcast(self, message):
		pass

	def from_angle(angle):
		angle -= 90
		radAngle = math.radians(angle)
		returnVec = [math.cos(radAngle), math.sin(radAngle)]
		if angle % 90 == 0:
			if returnVec[0] == 1 or returnVec[0] == -1:
				returnVec[1] = 0
			if returnVec[1] == 1 or returnVec[1] == -1:
				returnVec[0] = 0
		return returnVec


	# Pen

	def clear(self):
		self.pen_surface.blit(self.background, (0, 0))

	def stamp(self):
		self.pen_surface.blit(self.costume_blit, self.rect.topleft)

	def pen_down(self):
		self.pen = True

	def pen_up(self):
		self.pen = False

	def pen_line(self):
		end_pen = self.pos
		pygame.draw.aaline(self.game.pen_surface, 
						   self.pen_color, 
						   self.start_pen, 
						   end_pen, 
						   True)


	# Control

	def wait_tick(self):
		if self.wait_time <= self.game.time:
			self.waiting = False

	def wait(self, time):
		self.wait_time = self.game.time + time
		self.waiting = True


	# Sensing

	def direction_to(self, other):
		new_pos = (self.x - other.x, self.y - other.y)
		returnAngle = math.degrees(math.atan2(new_pos[1], new_pos[0]))
		# returnAngle *= -1
		returnAngle -= 90
		return returnAngle


#########################################################################################
# stage class                                                                           #
#########################################################################################


class stage():
	def __init__(self, game):
		self.game = game
		self.game.stage = self

		self.wait_time = 0
		self.waiting = False

	def wait_tick(self):
		if self.wait_time <= self.game.time:
			self.waiting = False

	def wait(self, time):
		self.wait_time = self.game.time + time
		self.waiting = True


class text_box():
	def __init__(self, game, text, other, variable, x, y, size = 40, color = Color("black")):
		self.game = game
		self.text = text
		self.other = other
		self.variable = variable
		self.x = x
		self.y = y
		self.size = size
		self.color = color

		self.game.text_box_list.append(self)

	def draw(self, win):
		print_text = copy(self.text)
		if self.variable is not None:
			print_text += str(self.other.__dict__[self.variable])

		font = pygame.font.SysFont('Arial', self.size)
		
		text_render = font.render(print_text, True, self.color)
		win.blit(text_render, (self.x, self.y))



#########################################################################################
# main test code                                                                        #
#########################################################################################


def main():
	# TESTING CODE
	hello = game(800, 800)
	scratchSprite(hello, costume="fish4.png")
	scratchSprite(hello, costume="test.png")

	hello.run()

if __name__ == '__main__':
    main()