#Population 1
"""
"""

import pygame

print("")
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
finish=False

screen=pygame.display.set_mode((400,300))
screen.fill(white)
pygame.display.set_caption("Population 1")

while(not finish):
	for event in pygame.event.get():
		#if(event.type == pygame.QUIT):
			#finish=True
		if(event.type == pygame.MOUSEBUTTONDOWN):
			finish=True
	screen.fill(white)
	pygame.display.update()
pygame.quit()
quit()
