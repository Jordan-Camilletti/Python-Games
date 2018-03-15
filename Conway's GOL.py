#"Conway's GOL".py
import pygame

pygame.init()
white=(255,255,255)
black=(0,0,0)
finish=False
grid=[[1,0,1],[0,1,0]]
yPos,xPos=0,0
screen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("Conway's Game of Life.")
#clock = pygame.time.Clock()

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True

	yPos=-1
	for y in grid:
		yPos+=1
		xPos=-1
		for x in y:
			xPos+=1
			if(x):
				pygame.draw.rect(screen,white,[xPos*5,yPos*5,5,5])#x,y,width,height
			else:
				pygame.draw.rect(screen,black,[xPos*5,yPos*5,5,5])
	pygame.display.update()
	#clock.tick(60)
pygame.quit()
quit()
