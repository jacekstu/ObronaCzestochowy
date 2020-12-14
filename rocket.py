import pygame 
from settings import *
import random

class Rocket(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = ROCKET_IMG
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0,WIDTH)
		self.speed_y = random.randint(3,10)

	def update(self):
		self.rect.y += self.speed_y
		if self.rect.y > HEIGHT:
			self.kill()


