"""This is a timer similar to the one used for GDQ/AGDQ
But this one actually counts with binary correctly
I couldn't stop focusing on how the GDQ counter was off with the binary counting
So I built my own"""

import pygame
import time
from random import randint

pygame.init()

white=(255,255,255)
black=(0,0,0)
finish=False
pause=False
count=0
yLen=int(input("Enter window height\n"))
ySqr=int(yLen/5)
xLen=int(yLen*8.86)
xSqr=int(xLen/5)

timer=time.time()
timeStr=""
timeS=""
font=pygame.font.SysFont('gillsans', 30)
screen=pygame.display.set_mode((xLen,yLen))
screen.fill(white)

while(not finish):
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			finish=True
		if(event.type == pygame.KEYDOWN):#Space=pause/unpause
			if(event.key == pygame.K_SPACE):
				pause=not pause

	if(not pause):
		count+=1
		bCount=("{0:b}".format(count))[::-1]
		for n in range(len(bCount)):
			if(bCount[n]=="0"):
				pygame.draw.rect(screen, white, [int(n/5)*xSqr,(n%5)*ySqr,xSqr,ySqr])
			elif(bCount[n]=="1" and screen.get_at((int(n/5)*xSqr,(n%5)*ySqr)) == (255,255,255,255)):#This last part makes colors less 'ravey'
				pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), [int(n/5)*xSqr,(n%5)*ySqr,xSqr,ySqr])
		
		timeS=str(time.time()-timer).split(".")
		timeStr=timeS[0]+"."+timeS[1][:2]#This makes sure that the time is cut off to 2 decimal places

		pygame.draw.rect(screen, screen.get_at((2*xSqr+1,2*ySqr+1)), [2*xSqr,2*ySqr,xSqr,ySqr])
		screen.blit(font.render(timeStr,False,black), ((int(xLen/2))-3-int(len(timeS[0])*10) , int(yLen/2)-int(font.get_height()/2)))

	pygame.time.wait(50)
	pygame.display.update()

pygame.quit()
quit()
