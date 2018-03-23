#"EXTREME GARDENING".py

"""
"""
import pygame

pygame.init()
white=(255,255,255)
black=(0,0,0)
finish=False
dosh=0
years=0
name=""
font=pygame.font.SysFont('Arial', 30)
text=font.render(name,False,black)
screen=pygame.display.set_mode((400,300))
screen.fill(white)
pygame.display.set_caption("EXTREME GARDENING!")

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True

	pygame.display.update()
	
pygame.quit()
quit()
