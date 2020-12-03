import pygame
from settings import *

class Animation(pygame.sprite.Sprite):
	def __init__(self, imgs_lt, x, y):
		super().__init__()
		self.lt = imgs_lt
		self.animating = False
		self.current_sprite = 0
		self.image = self.lt[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		if self.animating == True:
			self.current_sprite += 0.5
			if self.current_sprite >= len(self.lt):
				self.current_sprite = 0
				self.animating = False
				self.kill()

			self.image = self.lt[int(self.current_sprite)]

	def animate(self):
		self.animating = True