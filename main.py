import pygame, sys
import random
from settings import *
from bullet import Bullet
from player import Player
from villain import Villain

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
			print(len(villain_group))
			idx = random.randint(0,6)
			villain = Villain(idx)
			villain_group.add(villain)
		timer = 3

	for bullet in bullet_group:
		gets_hit = pygame.sprite.spritecollide(bullet, villain_group, True)
		if gets_hit:
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


