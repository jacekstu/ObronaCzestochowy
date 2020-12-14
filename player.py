import pygame
from settings import *
from bullet import Bullet
import random

# health bar code taken from yt channel : CleanCode

class Player(pygame.sprite.Sprite):

	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.animating = False
		self.current_sprite = 0
		self.image = PLAYER_SPRTIES_LT[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x, pos_y]

		# Health Bar varibles
		self.target_health = 500
		self.heal_change_speed = 5
		self.current_health = 200
		self.maximum_health = 1000
		self.health_bar_length = 400
		self.health_ratio = self.maximum_health / self.health_bar_length 
		self.healthbar_image = HEALTHBAR_IMG
		self.healthbar_image_rect = self.healthbar_image.get_rect()


	def update(self):
		if self.animating == True:
			self.current_sprite += 0.5
			if self.current_sprite >= len(PLAYER_SPRTIES_LT):
				self.current_sprite = 0
				self.animating = False

			self.image = PLAYER_SPRTIES_LT[int(self.current_sprite)]
		self.rect = (pygame.mouse.get_pos()[0], HEIGHT - 160)

		# update health bar
		self.advanced_health()

	def get_damage(self, amount):
		if self.target_health > 0:
			self.target_health -= amount
		if self.target_health <= 0:
			self.target_health = 0

	def get_health(self):
		if self.target_health < self.maximum_health:
			self.target_health += amount
		if self.target_health >= self.maximum_health:
			self.target_health = self.maximum_health

	def advanced_health(self):
		tranistion_width = 0
		transition_color = (255,0,0)

		if self.current_health < self.target_health:
			self.current_health += self.heal_change_speed
			tranistion_width = int((self.target_health - self.current_health)/
				self.health_ratio)
			transition_color = (0,255,0)

		if self.current_health > self.target_health:
			self.current_health -= self.heal_change_speed
			tranistion_width = int((self.target_health - self.current_health)/
				self.health_ratio)
			transition_color = (255,255,0)

		health_bar_rect = pygame.Rect(WIDTH - 410,27, self.current_health/self.health_ratio, 25)
		transition_bar_rect = pygame.Rect(health_bar_rect.right, 27, tranistion_width, 25)
		pygame.draw.rect(screen, (255, 0,0), health_bar_rect)
		pygame.draw.rect(screen, transition_color, transition_bar_rect)
		pygame.draw.rect(screen, (255,255,255), (WIDTH - 410, 27,self.health_bar_length, 25), 4)
		screen.blit(self.healthbar_image, (WIDTH - 440, 10))

	def animate(self):
		PUNCH_SND.play()
		self.animating = True

	def shoot(self):
		gravity_value = GRAVITY_LT[random.randint(0,len(GRAVITY_LT)-1)]
		return Bullet(pygame.mouse.get_pos()[0] + 63,HEIGHT- 120, gravity_value)