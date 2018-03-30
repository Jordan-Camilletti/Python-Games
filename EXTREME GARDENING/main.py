#"EXTREME GARDENING".py

"""
"""
import pygame
from math import floor

print("")
pygame.init()
white=(255,255,255)
black=(0,0,0)
finish=False
dosh=0
years=0
stage=0#0=seed,1=grow,2=upgrade

font=pygame.font.SysFont('Arial', 10)
names=["Bro's Rose",
		"Protien Petunia",
		"No Homo Hibiscus",
		"Tulip of Testosterone",
		"Beast Mode Blue Bonnet",
		"Dude's Daffodil",
		"Whey Waterlily",
		"Lifting Lavender",
		"'Sup Buttercup"]
photos=[]
#text=font.render("ABC",False,black)
screen=pygame.display.set_mode((400,300))
screen.fill(white)
pygame.display.set_caption("EXTREME GARDENING!")

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True

	if(stage==0):
		pygame.draw.rect(screen,black,[0,0,2,300])
		for n in range(1,4):
			pygame.draw.rect(screen,black,[(n*133)-1,0,2,300])
		pygame.draw.rect(screen,black,[0,0,400,2])
		for n in range(1,4):
			pygame.draw.rect(screen,black,[0,(n*100)-2,400,2])
		for name in range(len(names)):#This extremely long line is for displaying the names on a 9x9 grid
			screen.blit(font.render(names[name],False,black) , (((1+(name%3))*66)+((name%3)*66)-(font.render(names[name],False,black).get_width()/2) , (floor(name/3)*100)+80))
			img=pygame.image.load(photos[name])
			screen.blit(img, (10,10))

	elif(screen==1):
		pygame.draw.rect(screen,white,[0,0,1,1])

	else:
		pygame.draw.rect(screen,white,[0,0,1,1])
	pygame.display.update()
	
pygame.quit()
quit()
