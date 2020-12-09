import pygame
from settings import *
import random

class Bullet(pygame.sprite.Sprite):
	
	def __init__(self, pos_x, pos_y, gravity_value):
		super().__init__()
		self.x = pos_x
		self.y = pos_y
		self.image = BULLET_IMG
		self.original_surface = BULLET_IMG
		self.rect = self.image.get_rect(center = (self.x, self.y))
		self.gravity = -10
		self.max_up = 100
		self.gravity_value = gravity_value
		self.is_smashed = False
		self.angle = 0

	def rotate(self, surface, angle):
		rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
		#rotated_rect = rotated_surface.get_rect(center = (self.x, self.y))
		rotated_rect = rotated_surface.get_rect(center = (self.x, self.y))
		rotated_rect.x = self.rect.x
		rotated_rect.y = self.rect.y
		return rotated_surface, rotated_rect


	def update(self):
		self.angle += 3
		self.image, self.rect = self.rotate(self.original_surface, self.angle)
		self.rect.y += self.gravity
		self.rect.x -= 3
		self.gravity += self.gravity_value

		if self.rect.y >= BOTTOM_LINE_FOR_ORANGES - 10:
			self.is_smashed = True
	
		#print(HEIGHT - 70)
		if self.rect.y >= BOTTOM_LINE_FOR_ORANGES:
			self.kill()