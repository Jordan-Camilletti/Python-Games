#!/usr/bin/python
#Ping
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

screenXLen=800#All paddle/ball speeds/sizes are based off of these two
screenYLen=600
paddleLength=(screenYLen*0.20)
paddleSpeed=screenYLen*0.01
ballSpeed=paddleSpeed-1
score=[0,0]
screen=pygame.display.set_mode((screenXLen,screenYLen))
screen.fill(black)
pygame.display.set_caption("Ping")

def AIMove(ballY, ballSpeed, paddleY, paddleSpeed, paddleLen, screenY):
	center=paddleY+(paddleLen/2)#Center of paddle
	if(center!=ballY and paddleY>=0 and paddleY+paddleLen<=screenY):
		if(center>ballY):#Paddle needs to move up
			if(paddleY-paddleSpeed<=0):
				return(0)
			return(paddleY-paddleSpeed)
		else:#Paddle needs to move downs
			if(paddleY+paddleLen+paddleSpeed>screenY):
				return(screenY-paddleLen)
			return(paddleY+paddleSpeed)
	return(paddleY)#Paddle doesn't need to move/can't move

while(not finish):
	match=True#Match is used for each game to reset it
	paddle1=(screenYLen/2)-(paddleLength/2)#Paddle starting positions
	paddle2=(screenYLen/2)-(paddleLength/2)
	movementX=ballSpeed-(2*ballSpeed*random.randint(0,1))#Starting ball speeds
	movementY=0
	ballXPos=(screenXLen/2)-(screenXLen*0.01)#Starting ball positions
	ballYPos=(screenYLen/2)-(screenYLen*0.01)
	while(match):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				finish=True
		keys=pygame.key.get_pressed()
		
		if(keys[pygame.K_w] and paddle1>0):#Moving up and down
			paddle1-=paddleSpeed
		if(keys[pygame.K_s] and paddle1+paddleLength<screenYLen):
			paddle1+=paddleSpeed
		paddle2=AIMove(ballYPos,ballSpeed,paddle2,paddleSpeed,paddleLength,screenYLen)
		
		if(movementX<0 and abs(ballXPos-(screenXLen*0.1))<20 and ballYPos-paddle1<paddleLength and ballYPos-paddle1>=0):
			movementX=(-1*movementX)+1#Ball hitting left paddle
			movementY=0.2*(ballYPos-paddle1-(paddleLength/2))
		if(movementX>0 and abs(ballXPos-(screenXLen-(screenXLen*0.125)))<20 and ballYPos-paddle2<paddleLength and ballYPos-paddle2>=0):
			movementX=(-1*movementX)-1#Ball hitting right paddle
			movementY=0.2*(ballYPos-paddle2-(paddleLength/2))
		ballXPos+=movementX
		ballYPos+=movementY
		
		if(ballXPos<0):#Ball hitting left goal
			ballXPos=0
			movementX=0
			score[1]+=1
			match=False
		elif(ballXPos>=screenXLen*0.98):#Ball hitting right goal
			ballXPos=screenXLen*0.98
			movementX=0
			score[0]+=1
			match=False
		if(ballYPos<0):#Hitting the top and bottom of the screen
			ballYPos=0
			movementY*=-1
		elif(ballYPos>=screenYLen*0.98):
			ballYPos=screenYLen*0.98
			movementY*=-1
	
		screen.fill(black)
		screen.blit(font.render(str(score[0]),False,white), ((screenXLen/2)-(screenXLen*0.2), 10))
		screen.blit(font.render(str(score[1]),False,white), ((screenXLen/2)+(screenXLen*0.2), 10))
		pygame.draw.rect(screen,white,[screenXLen*0.1,paddle1,20,paddleLength])
		pygame.draw.rect(screen,white,[screenXLen-(screenXLen*0.125),paddle2,20,paddleLength])
		pygame.draw.rect(screen,white,[ballXPos,ballYPos,(screenXLen*0.02),(screenXLen*0.02)])
		pygame.display.update()
		
		clock.tick(45)
	
pygame.quit()
quit()
