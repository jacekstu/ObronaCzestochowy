import pygame
from settings import *
from bullet import Bullet
import random

class Player(pygame.sprite.Sprite):

	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.animating = False
		self.current_sprite = 0
		self.image = PLAYER_SPRTIES_LT[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x, pos_y]

	def update(self):
		if self.animating == True:
			self.current_sprite += 0.5
			if self.current_sprite >= len(PLAYER_SPRTIES_LT):
				self.current_sprite = 0
				self.animating = False

			self.image = PLAYER_SPRTIES_LT[int(self.current_sprite)]
		self.rect = (pygame.mouse.get_pos()[0], HEIGHT - 160)

	def animate(self):
		PUNCH_SND.play()
		self.animating = True

	def shoot(self):
		gravity_value = GRAVITY_LT[random.randint(0,len(GRAVITY_LT)-1)]
		return Bullet(pygame.mouse.get_pos()[0] + 63,HEIGHT- 120, gravity_value)