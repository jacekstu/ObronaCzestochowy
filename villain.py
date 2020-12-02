import pygame, random
from settings import *

pos_lt_y = [0,150,250,350,450]

class Villain(pygame.sprite.Sprite):
	def __init__(self, idx, x_pos):
		super().__init__()
		self.image = VILLAIN_LT[idx]
		self.pos_x = x_pos
		self.pos_y = pos_lt_y[random.randint(0,3)]
		self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))
		self.speed = -1
		self.max_up = self.rect.y + 50
		self.max_down = self.rect.y - 50
		self.sound = idx

	def update(self):
		self.rect.y += self.speed
		if self.rect.y >= self.max_up:
			self.speed = -self.speed
		if self.rect.y <= self.max_down:
			self.speed = -self.speed
