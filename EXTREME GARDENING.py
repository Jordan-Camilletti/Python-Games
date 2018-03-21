#"EXTREME GARDENING".py

"""
"""
import pygame

pygame.init()
finish=False
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("EXTREME GARDENING")

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True
			
	pygame.display.update()
pygame.quit()
quit()