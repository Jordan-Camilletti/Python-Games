#Population 1
"""
"""

import pygame
import random

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
movementX=6-(12*random.randint(0,1))
movementY=6-(12*random.randint(0,1))
score=[0,0]
screen=pygame.display.set_mode((screenXLen,screenYLen))
screen.fill(black)
pygame.display.set_caption("Population 1")

playerXPos=(screenXLen/2)-(screenXLen*0.01)
playerYPos=(screenYLen/2)-(screenYLen*0.01)

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True
	playerXPos+=movementX
	if(playerXPos<0):
		playerXPos=0
		movementX=0
		score[0]+=1
	elif(playerXPos>=screenXLen*0.98):
		playerXPos=screenXLen*0.98
		movementX=0
		score[1]+=1
	playerYPos+=movementY
	if(playerYPos<0):
		playerYPos=0
		movementY*=-1
	elif(playerYPos>=screenYLen*0.98):
		playerYPos=screenYLen*0.98
		movementY*=-1
	
	screen.fill(black)
	pygame.draw.rect(screen,white,[playerXPos,playerYPos,(screenXLen*0.02),(screenXLen*0.02)])
	pygame.display.update()
	
	clock.tick(45)
	
pygame.quit()
quit()