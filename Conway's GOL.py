import pygame

pygame.init()
screen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("Conway's Game of Life.")
#clock = pygame.time.Clock()

while(True):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit()

		pygame.display.update()
		#clock.tick(60)
quit()