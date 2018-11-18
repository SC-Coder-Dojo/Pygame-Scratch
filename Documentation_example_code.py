
# Empty example sprite
class example_empty_sprite(scratchSprite):
	def __init__(self, game, x=None, y=None):	
		super().__init__(game, x, y) # Keep This
		### This code runs when the sprite is created
		pass

	def update(self):	
		### This code runs every frame of the game
		pass

	def broadcast(self, message):	
		### This code runs when you broadcast a message
		if message == "Test":	
			# This code runs if the message "Test" is broadcast
			pass


# Example fish sprite
class example_fish_sprite(scratchSprite):
	def __init__(self, game, x=None, y=None):
		super().__init__(game, x, y) # Keep This

	def update(self):
		self.move(20)		# fish moves forward 20 pixels every frame
		self.turn_right(1)	# fish turns right 1 every frame
		self.edge_bounce()	# fish bounces of the edges

	def broadcast(self, message):
		# This code runs when you broadcast a message
		if message == "Test":
			# This code runs if the message "Test" is broadcast
			pass


fish_one = example_fish_sprite(game, 100, 200)		
	# Create an example fish sprite called fish_one at x:100 y:200
fish_one.costume = "fish2.png"
	# Give fish_one a costume (image in Costumes folder)
fish_one.size = 50
	# Set the size of the fish


fish_two = example_fish_sprite(game)
	# Create another example fish sprite called fish_two at a random position,
	# as we didnt give it and x and y position
fish_two.costume = "fish3.png"
	# Give fish_two a costume


## ScratchSprite Functions

# Control
wait(time)

# Looks
show()
hide()

# Motion
move(steps)
right(deg), turn_right(deg)
left(deg), turn_left(deg)

goto(x, y)
goto_random()

point_in_direc(deg)
point_towards(other)

edge_bounce()

distance_to(other)
touching(other)

direction_to(other)

# Pen
clear()
stamp()
pen_down()
pen_up()

# Control
wait(milliseconds) # 1000 milliseconds in 1 sec



# Debugging
game.show_hit_box = True