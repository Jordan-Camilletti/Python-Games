import pygame
from random import randint

pygame.init()
finish=False
white=(255,255,255)

#8.86pix x 1pix
#6squares x 4squares
count=0
yLen=100
ySqr=int(yLen/4)
xLen=int(yLen*8.86)
xSqr=int(xLen/6)
screen=pygame.display.set_mode((xLen,yLen))
screen.fill(white)

while(not finish):
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			finish=True

	count+=1
	bCount=("{0:b}".format(count))[::-1]
	#print(bCount)
	for n in range(len(bCount)):
		if(bCount[n]=="0"):
			pygame.draw.rect(screen,white, [int(n/4)*xSqr,(n%4)*ySqr,xSqr,ySqr])
		elif(bCount[n]=="1" and screen.get_at((int(n/4)*xSqr,(n%4)*ySqr)) == (255,255,255,255)):#This last part makes colors less 'ravey'
			pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), [int(n/4)*xSqr,(n%4)*ySqr,xSqr,ySqr])

	pygame.time.wait(100)
	pygame.display.update()

pygame.quit()
quit()
