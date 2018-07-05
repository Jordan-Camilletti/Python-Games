import pygame

pygame.init()
finish=False
white=(255,255,255)
black=(0,0,0)

#8.86p x 1p
#6c x 4c
count=0
screen=pygame.display.set_mode((int(100*8.86),100))
screen.fill(white)

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True

	count+=1
	bCount="{0:b}".format(count)
	#print(bCount)
	for n in range(len(bCount)):
		if(bCount[n]=="0"):
			pygame.draw.rect(screen,white,[int(n/4)*50,(n%4)*25,50,25])
		else:
			pygame.draw.rect(screen,black,[int(n/4)*50,(n%4)*25,50,25])

	pygame.time.wait(100)
	pygame.display.update()

pygame.quit()
quit()
