import pygame

pygame.init()
finish=False
white=(255,255,255)
black=(0,0,0)

#9p x 1p
#8.86 x 1
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
	for n in range(len(bCount)):
		pygame.draw.rect(screen,black,[0,int(n/4)*25,50,25*int(bCount[n])])

	pygame.time.wait(1000)
	pygame.display.update()

pygame.quit()
quit()