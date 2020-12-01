import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
	
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.image = BULLET_IMG
		self.rect = self.image.get_rect(center = (pos_x, pos_y))

	def update(self):
		self.rect.y -= 8
		self.rect.x -= 3
		if self.rect.y <= 30:
			self.kill()
