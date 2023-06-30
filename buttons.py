# Importing modules
import pygame

#button class
class Button():
	def __init__(self, x, y, image, offset):
		width = image.get_width()
		height = image.get_height()
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.offset = offset
		self.always_up = False

	def draw(self, surface):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mousehover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.rect.bottom -= self.offset
				action = True

		elif self.offset != 0:
			#to reset the position of button
			if pygame.mouse.get_pressed()[0] == 1 and (self.clicked == True and not self.always_up):
				self.clicked = False
				self.rect.bottom += self.offset
				action = False

		if self.offset == 0:
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action