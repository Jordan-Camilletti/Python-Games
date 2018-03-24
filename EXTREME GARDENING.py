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
stage=0#0=seed,1=grow,2=upgrade
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

	print(stage)
	if(stage==0):
		pygame.draw.rect(screen,black,[50,10,5,5])
	elif(screen==1):
		pygame.draw.rect(screen,white,[0,0,1,1])
	else:
		pygame.draw.rect(screen,white,[0,0,1,1])
	pygame.display.update()
	
pygame.quit()
quit()
