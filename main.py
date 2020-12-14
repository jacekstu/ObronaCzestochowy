import pygame, sys
import random
from settings import *
from bullet import Bullet
from player import Player
from villain import Villain
from animation import Animation
from rocket import Rocket

# Add night
# create a filter of the same size as the display
filter = pygame.surface.Surface((WIDTH, HEIGHT))


# All postion available for villains on the x axis	
position_x_lt = [100,250,380, 510, 630, 770, 870, 950, 1130]

# Initialize the library/
pygame.init()
pygame.mouse.set_visible(False)

# Create a clock object
clock = pygame.time.Clock()
# Initialize delta
timer = 5
dt = 0

# Create the main display window
pygame.display.set_caption(GAME_TITLE)


# Define the sprite groups
animated_sprties = pygame.sprite.Group()
player = Player(WIDTH/2, HEIGHT/2 - 180)
animated_sprties.add(player)

# Other groups
bullet_group = pygame.sprite.Group()
villain_group = pygame.sprite.Group()
smashing_oranges_group = pygame.sprite.Group()
rocket_group = pygame.sprite.Group()


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
			#print(bullet_group.sprites()[0].rect.x)

	# attack or not
	attack = random.choice([random.randrange(30)])
	if attack == 2:
		rocket_group.add(Rocket())

	# Creating villains everytime the timer is equal to 0
	timer -= dt
	if timer <= 0:
		if len(villain_group) <= 9:
			# select the position of the villan on the x - axis
			# we set the max random int to the length of the list, since we gonna be removing items from it
			if len(position_x_lt) > 0:
				pos_x = random.randint(0,len(position_x_lt)-1)
				# Here we randomnly select a picture for our villain sprite
				idx = random.randint(0,6)
				villain = Villain(idx, position_x_lt[pos_x])
				villain_group.add(villain)
				# Delete  that x_postion from the lsit, so it can't be used y another sprite
				position_x_lt.pop(pos_x)
		timer = 3

	for bullet in bullet_group:
		gets_hit = pygame.sprite.spritecollide(bullet, villain_group, True)
		if gets_hit:
			# Create a new splash animation, it will be added to the
			# animated sprite group and removed from there
			# Once the animation has been completed
			new_splash = Animation(SPLASHING_FRUIT_LT2,gets_hit[0].pos_x, gets_hit[0].pos_y)
			animated_sprties.add(new_splash)
			new_splash.animate()
			# change the value for this pos_x key to True so it can be selected again
			# Add the x position back to the list of available postions
			if gets_hit[0].sound == 6:
				FAKEN.play()
			position_x_lt.append(gets_hit[0].pos_x)
			bullet_group.remove(bullet)

	for bullet in bullet_group.sprites():
		if bullet.is_smashed:
			smashed = Animation(SPLASHING_FRUIT_LT,bullet.rect.x-1, BOTTOM_LINE_FOR_ORANGES, False)
			smashing_oranges_group.add(smashed)
			smashed.animate()

	screen.fill((0,0,0))
	# Draw elements from the groups#	
	smashing_oranges_group.draw(screen)
	animated_sprties.draw(screen)
	villain_group.draw(screen)
	bullet_group.draw(screen)
	rocket_group.draw(screen)

	# Update the elements from the groups
	animated_sprties.update()
	villain_group.update()
	bullet_group.update()
	rocket_group.update()

	smashing_oranges_group.update()
	# Update the main display
	if len(smashing_oranges_group) > 5:
		smashing_oranges_group.remove(smashing_oranges_group.sprites()[0:2])

	filter.fill(pygame.color.Color('Grey'))
	# EFEKT PREDKOSCI - nie mozna robic screen.fill((0,0,0)
	#screen.blit(filter, (0,0), special_flags=pygame.BLEND_MULT) ##--> DAJE SUPER EFEKT ROZMYCIA
	pygame.display.flip()

	# get delat time
	dt = clock.tick(60) / 1000