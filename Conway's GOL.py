import pygame

pygame.init()
white=(255,255,255)
black=(0,0,0)
screen=pygame.display.set_mode((400, 300))
finish=False
pygame.display.set_caption("Conway's Game of Life.")
grid=[[0,0,0],[0,0,0]]
#clock = pygame.time.Clock()

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True

	#pygame.draw.rect(screen,white,[200,200,10,10])
	pygame.display.update()
	#clock.tick(60)
pygame.quit()
quit()
