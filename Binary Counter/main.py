import pygame
from random import randint

pygame.init()
finish=False
white=(255,255,255)
black=(0,0,0)

#8.86pix x 1pix
#6squares x 4squares
count=0
yLen=100
xLen=int(yLen*8.86)
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
			pygame.draw.rect(screen,white, [int(n/4)*50,(n%4)*25,50,25])
		else:
			pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), [int(n/4)*50,(n%4)*25,50,25])

	pygame.time.wait(100)
	pygame.display.update()

pygame.quit()
quit()
