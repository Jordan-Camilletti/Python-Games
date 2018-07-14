import pygame
import time
from random import randint

pygame.init()

#8.86pix x 1pix
#6squares x 4squares
white=(255,255,255)
black=(0,0,0)
finish=False
count=0
yLen=int(input("Enter window height\n"))
ySqr=int(yLen/4)
xLen=int(yLen*8.86)
xSqr=int(xLen/6)

timer=time.time()
font=pygame.font.SysFont('Arial', 10)
screen=pygame.display.set_mode((xLen,yLen))
screen.fill(white)

while(not finish):
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			finish=True

	#print(timer)
	count+=1
	bCount=("{0:b}".format(count))[::-1]
	for n in range(len(bCount)):
		if(bCount[n]=="0"):
			pygame.draw.rect(screen, white, [int(n/4)*xSqr,(n%4)*ySqr,xSqr,ySqr])
		elif(bCount[n]=="1" and screen.get_at((int(n/4)*xSqr,(n%4)*ySqr)) == (255,255,255,255)):#This last part makes colors less 'ravey'
			pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), [int(n/4)*xSqr,(n%4)*ySqr,xSqr,ySqr])
	screen.blit(font.render(str(time.time()-timer)[:5],False,black), (0,0))

	pygame.time.wait(100)
	pygame.display.update()

pygame.quit()
quit()
