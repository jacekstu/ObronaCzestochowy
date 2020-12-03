import pygame
from settings import *
import random
from animation import Animation

class Bullet(pygame.sprite.Sprite):
	
	def __init__(self, pos_x, pos_y, gravity_value):
		super().__init__()
		self.image = BULLET_IMG
		self.rect = self.image.get_rect(center = (pos_x, pos_y))
		self.gravity = -10
		self.max_up = 100
		self.gravity_value = gravity_value

	def update(self):
		self.rect.y += self.gravity
		self.rect.x -= 3
		self.gravity += self.gravity_value

		if self.rect.y >= HEIGHT - 70:
			# zrobi animacje i play the sound rozijanej mandarynki
			self.kill()