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
		"'Sup Butetrcup"]
seedPhotos=['Seeds/bonnet1.jpg',
		'Seeds/buttercup1.jpg',
		'Seeds/daffodil1.jpg',
		'Seeds/hib1.png',
		'Seeds/lavender1.jpg',
		'Seeds/petunia1.jpg',
		'Seeds/rose1.jpg',
		'Seeds/sunflower1.jpg',
		'Seeds/tulip1.jpg',
		'Seeds/waterlily1.png']
#text=font.render("ABC",False,black)
screen=pygame.display.set_mode((400,300))
screen.fill(white)
pygame.display.set_caption("EXTREME GARDENING!")

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True
		if(event.type == pygame.MOUSEBUTTONDOWN):
			mouseX,mouseY=pygame.mouse.get_pos()
			if(stage==0):
				print(mouseX/(400/3), mouseY/(300/3))
			elif(stage==1):
				print(mouseX)
			else:
				print(mouseX)

	if(stage==0):
		pygame.draw.rect(screen,black,[0,0,2,300])
		for n in range(1,4):
			pygame.draw.rect(screen,black,[(n*133)-1,0,2,300])
		pygame.draw.rect(screen,black,[0,0,400,2])
		for n in range(1,4):
			pygame.draw.rect(screen,black,[0,(n*100)-2,400,2])
		for name in range(len(names)):#This extremely long line is for displaying the names on a 9x9 grid
			screen.blit(font.render(names[name],False,black) , (((1+(name%3))*66)+((name%3)*66)-(font.render(names[name],False,black).get_width()/2) , (floor(name/3)*100)+85))
			img=pygame.image.load(seedPhotos[name])
			screen.blit(img, (((1+(name%3))*66)+((name%3)*66)-40 , (floor(name/3)*100)+5))

	elif(screen==1):
		pygame.draw.rect(screen,white,[0,0,1,1])

	else:
		pygame.draw.rect(screen,white,[0,0,1,1])
	pygame.display.update()
	
pygame.quit()
quit()
