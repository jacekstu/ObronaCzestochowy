import pygame
from settings import *

class Animation(pygame.sprite.Sprite):
	def __init__(self, imgs_lt, x, y, kill=True):
		super().__init__()
		self.lt = imgs_lt
		self.kill_em = kill
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
				if self.kill_em == True:
					self.kill()

			self.image = self.lt[int(self.current_sprite)]

	def animate(self):
		self.animating = True