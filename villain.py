import pygame, random
from settings import *

pos_lt_x = [0,150,350,450,750]
pos_lt_y = [0,150,250,350,450]

class Villain(pygame.sprite.Sprite):
	def __init__(self, idx):
		super().__init__()
		self.image = VILLAIN_LT[idx]
		self.image = pygame.transform.scale(self.image, (100,100))
		self.pos_x = pos_lt_x[random.randint(0, len(pos_lt_x) - 1)]
		pos_y = pos_lt_y[random.randint(0,3)]
		self.rect = self.image.get_rect(center = (self.pos_x, pos_y))
		self.speed = -1
		self.max_up = self.rect.y + 50
		self.max_down = self.rect.y - 50

	def update(self):
		self.rect.y += self.speed
		if self.rect.y >= self.max_up:
			self.speed = -self.speed
		if self.rect.y <= self.max_down:
			self.speed = -self.speed