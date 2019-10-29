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
font=pygame.font.SysFont('Impact', 40)

finish=False

screenXLen=800
screenYLen=600
paddleLength=(screenYLen*0.20)
paddleSpeed=6
ballSpeed=5
score=[0,0]
screen=pygame.display.set_mode((screenXLen,screenYLen))
screen.fill(black)
pygame.display.set_caption("Population 1")

def AIMove(ballY, paddleY, paddleLen, screenY, speed):
	if(paddleY<ballY and abs(paddleY-ballY)<paddleLen/2):
		return(paddleY)
	if(paddleY>ballY):
		return(paddleY-speed)
	if(paddleY+paddleLen<screenY):
		return(paddleY+speed)
	return(paddleY)

while(not finish):
	print(score)
	match=True
	paddle1=(screenYLen/2)-(paddleLength/2)
	paddle2=(screenYLen/2)-(paddleLength/2)
	movementX=ballSpeed-(2*ballSpeed*random.randint(0,1))
	movementY=0
	ballXPos=(screenXLen/2)-(screenXLen*0.01)
	ballYPos=(screenYLen/2)-(screenYLen*0.01)
	while(match):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				finish=True
		keys=pygame.key.get_pressed()
		
		if(keys[pygame.K_w] and paddle1>0):
			paddle1-=paddleSpeed
		if(keys[pygame.K_s] and paddle1+paddleLength<screenYLen):
			paddle1+=paddleSpeed
		paddle2=AIMove(ballYPos,paddle2,paddleLength,screenYLen,paddleSpeed+1)

		if(abs(ballXPos-(screenXLen*0.1))<20 and ballYPos-paddle1<paddleLength and ballYPos-paddle1>=0):
			movementX=(-1*movementX)+1
			movementY=0.2*(ballYPos-paddle1-(paddleLength/2))
		if(abs(ballXPos-(screenXLen-(screenXLen*0.125)))<20 and ballYPos-paddle2<paddleLength and ballYPos-paddle2>=0):
			movementX=(-1*movementX)-1
			movementY=0.2*(ballYPos-paddle2-(paddleLength/2))
		ballXPos+=movementX
		ballYPos+=movementY
		if(ballXPos<0):
			ballXPos=0
			movementX=0
			score[1]+=1
			match=False
		elif(ballXPos>=screenXLen*0.98):
			ballXPos=screenXLen*0.98
			movementX=0
			score[0]+=1
			match=False
		if(ballYPos<0):
			ballYPos=0
			movementY*=-1
		elif(ballYPos>=screenYLen*0.98):
			ballYPos=screenYLen*0.98
			movementY*=-1
	
		screen.fill(black)
		screen.blit(font.render(str(score[0]),False,white), (300, 10))
		screen.blit(font.render(str(score[1]),False,white), (500, 10))
		pygame.draw.rect(screen,white,[screenXLen*0.1,paddle1,20,paddleLength])
		pygame.draw.rect(screen,white,[screenXLen-(screenXLen*0.125),paddle2,20,paddleLength])
		pygame.draw.rect(screen,white,[ballXPos,ballYPos,(screenXLen*0.02),(screenXLen*0.02)])
		pygame.display.update()
		
		clock.tick(45)
	
pygame.quit()
quit()
