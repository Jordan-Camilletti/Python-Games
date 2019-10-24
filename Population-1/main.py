#Population 1
"""
"""

import pygame

print("")
pygame.init()
clock=pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
star=(10,10,244)
finish=False

screenXLen=800
screenYLen=600
screen=pygame.display.set_mode((screenXLen,screenYLen))
screen.fill(black)
pygame.display.set_caption("Population 1")

playerXPos=(screenXLen/2)-(screenXLen*0.01)
playerYPos=(screenYLen/2)-(screenYLen*0.01)

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True
		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_w and playerYPos>0):
				playerYPos-=min(2,playerYPos)
			if(event.key == pygame.K_a and playerXPos>0):
				playerXPos-=min(2,playerXPos)
			if(event.key == pygame.K_s and playerYPos<screenYLen*0.99):
				playerYPos+=min(2,screenYLen-playerYPos)
			if(event.key == pygame.K_d and playerXPos<screenXLen*0.99):
				playerXPos+=min(2,screenXLen-playerXPos)
	screen.fill(black)
	pygame.draw.rect(screen,white,[playerXPos,playerYPos,(screenXLen*0.02),(screenXLen*0.02)])
	pygame.display.update()
	
	clock.tick(45)
	
pygame.quit()
quit()