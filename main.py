import pygame, sys
import random
from settings import *
from bullet import Bullet
from player import Player
from villain import Villain


# All postion available for villains on the x axis
position_x_lt = [0,150,350, 450, 750]

# Initialize the library
pygame.init()
pygame.mouse.set_visible(False)

# Create a clock object
clock = pygame.time.Clock()
# Initialize delta
timer = 5
dt = 0

# Create the main display window
screen = pygame.display.set_mode(WINDOW)
pygame.display.set_caption(GAME_TITLE)


# Define the sprite groups
animated_sprties = pygame.sprite.Group()
player = Player(WIDTH/2, HEIGHT/2 - 180)
animated_sprties.add(player)



# Other groups
bullet_group = pygame.sprite.Group()
villain_group = pygame.sprite.Group()

# The main loop of the game
while True:

	# Getting the game's events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				terminate_game()
		if event.type == pygame.MOUSEBUTTONDOWN:
			player.animate()
			bullet_group.add(player.shoot())

	# Creating villains everytime the timer is equal to 0
	timer -= dt
	if timer <= 0:
		if len(villain_group) <= 5:
			# select the position of the villan on the x - axis
			# we set the max random int to the length of the list, since we gonna be removing items from it
			if len(position_x_lt) > 0:
				pos_x = random.randint(0,len(position_x_lt)-1)
				# Here we randomnly select a picture for our villain sprite
				idx = random.randint(0,6)
				villain = Villain(idx, position_x_lt[pos_x])
				# Delete  that x_postion from the lsit, so it can't be used y another sprite
				position_x_lt.pop(pos_x)
		timer = 3

	for bullet in bullet_group:
		gets_hit = pygame.sprite.spritecollide(bullet, villain_group, True)
		if gets_hit:
			# change the value for this pos_x key to True so it can be selected again
			# Add the x position back to the list of available postions
			position_x_lt.append(gets_hit[0].pos_x)
			bullet_group.remove(bullet)


	screen.fill(BLACK)

	# Draw elements from the groups
	animated_sprties.draw(screen)
	villain_group.draw(screen)
	bullet_group.draw(screen)
	# Update the elements from the groups
	animated_sprties.update()
	villain_group.update()
	bullet_group.update()
	# Update the main display
	pygame.display.flip()

	# get delat time
	dt = clock.tick(60) / 1000


