#!/usr/bin/python
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
match=True

screenXLen=800
screenYLen=600
paddleLength=(screenYLen*0.20)
paddle1=(screenYLen/2)-(paddleLength/2)
paddle2=(screenYLen/2)-(paddleLength/2)
movementX=6-(12*random.randint(0,1))
movementY=6-(12*random.randint(0,1))
score=[0,0]
screen=pygame.display.set_mode((screenXLen,screenYLen))
screen.fill(black)
pygame.display.set_caption("Population 1")

ballXPos=(screenXLen/2)-(screenXLen*0.01)
ballYPos=(screenYLen/2)-(screenYLen*0.01)

while(not finish):
	
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True
	keys=pygame.key.get_pressed()
	if(keys[pygame.K_w] and paddle1>0):
		paddle1-=6
	if(keys[pygame.K_s]):
		paddle1+=6
	
	ballXPos+=movementX
	ballYPos+=movementY
	if(ballXPos<0):
		ballXPos=0
		movementX=0
		score[0]+=1
		match=False
	elif(ballXPos>=screenXLen*0.98):
		ballXPos=screenXLen*0.98
		movementX=0
		score[1]+=1
		match=False
	if(ballYPos<0):
		ballYPos=0
		movementY*=-1
	elif(ballYPos>=screenYLen*0.98):
		ballYPos=screenYLen*0.98
		movementY*=-1
	
	screen.fill(black)
	pygame.draw.rect(screen,white,[100,paddle1,20,paddleLength])
	pygame.draw.rect(screen,white,[ballXPos,ballYPos,(screenXLen*0.02),(screenXLen*0.02)])
	pygame.display.update()
	
	clock.tick(45)
	
pygame.quit()
quit()
