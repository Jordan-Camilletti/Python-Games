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
file=open("Assets/data.txt", "r")

finish=False
currMatch=0

screenXLen=800#All paddle/ball speeds/sizes are based off of these two
screenYLen=600
paddleLength=(screenYLen*0.20)
paddleSpeed=screenYLen*0.01
enemySpeed=screenYLen*0.01
ballSpeed=paddleSpeed-1
movementX=ballSpeed*1
score=[0,0]
dataFile=open("Assets/data.txt","r")
data=[]

screen=pygame.display.set_mode((screenXLen,screenYLen))
screen.fill(black)
pygame.display.set_caption("Ping")

def AIMove(ballY, ballSpeed, paddleY, paddleSpeed, paddleLen, screenY):
	if(paddleY<0):
		return(0)
	if(paddleY+paddleLen>screenY):
		return(screenY-paddleLen)
	center=paddleY+(paddleLen/2)#Center of paddle
	if(center!=ballY):
		if(center>=ballY):#Paddle needs to move up
			if(paddleY-paddleSpeed<0):
				return(0)
			if(center-paddleSpeed<ballY):
				return(ballY-(paddleLen/2))
			return(paddleY-paddleSpeed)
		else:#Paddle needs to move downs
			if(paddleY+paddleLen+paddleSpeed>screenY):
				return(screenY-paddleLen)
			if(center+paddleSpeed>ballY):
				return(ballY-(paddleLen/2))
			return(paddleY+paddleSpeed)
	return(paddleY)#Paddle doesn't need to move/can't move

def loadNewGame(paddleSpeed,file,curr):#TODO: Create 'data list' for game to read off of
	print("A")
	paddleSpeed=600
	print(paddleSpeed)
	return(0)

while(not finish):
	for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				finish=True
	match=True#Match is used for each game to reset it
	paddle1=(screenYLen/2)-(paddleLength/2)#Paddle starting positions
	paddle2=(screenYLen/2)-(paddleLength/2)
	if(movementX>0):
		movementX=ballSpeed
	else:
		movementX=-1*ballSpeed
	movementY=ballSpeed*random.randint(-50,50)*0.01#Starting ball speeds
	ballXPos=(screenXLen/2)-(screenXLen*0.01)#Starting ball positions
	ballYPos=(screenYLen/2)-(screenYLen*0.01)
	if(score[0]+score[1]>=3 and abs(score[0]-score[1])>=2):#Player must win/lose by at least 2 points
		currMatch+=1
		if(score[1]>score[0]):
			currMatch=0
		score[0]=0
		score[1]=0
			
		data=[]
		for n in range(8):
			data.append(float(dataFile.readline().split(",")[currMatch]))
		print(data)
		screenXLen=data[0]
		screenYLen=data[1]
		paddleLength=data[2]
		paddleSpeed=data[3]
		enemySpeed=data[4]
		ballSpeed=data[5]
		movementX=data[6]
		ballSize=data[7]
	
	while(match and not finish):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				finish=True
		keys=pygame.key.get_pressed()
		
		if((keys[pygame.K_w] or keys[pygame.K_UP]) and paddle1>0):#Moving up and down
			paddle1-=paddleSpeed
		if((keys[pygame.K_s] or keys[pygame.K_DOWN]) and paddle1+paddleLength<screenYLen):
			paddle1+=paddleSpeed
		#paddle2=AIMove(ballYPos,ballSpeed,paddle2,enemySpeed,paddleLength,screenYLen)
		
		if(movementX<0 and abs(ballXPos-(screenXLen*0.1))<20 and ballYPos-paddle1<paddleLength and ballYPos-paddle1>=0):
			movementX=(-1*movementX)+1#Ball hitting left paddle
			movementY=0.2*(ballYPos-paddle1-(paddleLength/2))
		if(movementX>0 and abs(ballXPos-(screenXLen-(screenXLen*0.125)))<20 and ballYPos-paddle2<paddleLength and ballYPos-paddle2>=0):
			movementX=(-1*movementX)-1#Ball hitting right paddle
			movementY=0.2*(ballYPos-paddle2-(paddleLength/2))
		ballXPos+=movementX
		ballYPos+=movementY
		
		if(ballXPos<0):#Ball hitting left goal
			score[1]+=1
			match=False
		elif(ballXPos>=screenXLen):#Ball hitting right goal
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
	
dataFile.close()
pygame.quit()
quit()