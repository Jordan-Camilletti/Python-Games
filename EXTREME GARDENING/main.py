#"EXTREME GARDENING".py

"""
"""
import pygame
from math import floor, ceil

print("")
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
finish=False
dosh=0
inc=1
flowerNum=0
stage=0#-2=credits,-1=help,0=menu,1==seed,2=grow,3=upgrade

sFont=pygame.font.SysFont('Impact',45)#starting font
cFont=pygame.font.SysFont('Arial', 15)#credits font
font1=pygame.font.SysFont('Arial', 10)
font2=pygame.font.SysFont('Arial', 20)
names=["Bro's Rose",
		"Protien Petunia",
		"No Homo Hibiscus",
		"Tulip of Testosterone",
		"Beast Mode Blue Bonnet",
		"Dude's Daffodil",
		"Whey Waterlily",
		"Lifting Lavender",
		"'Sup Buttercup"]
seedPhotos=['Seeds/rose1.jpg',
		'Seeds/petunia1.jpg',
		'Seeds/hib1.png',
		'Seeds/tulip1.jpg',
		'Seeds/bonnet1.jpg',
		'Seeds/daffodil1.jpg',
		'Seeds/waterlily1.png',
		'Seeds/lavender1.jpg',
		'Seeds/buttercup1.jpg']
plantPhotos=['Plants/rose2.jpg',
			'Plants/petunia2.jpg',
			'Plants/hib2.jpg',
			'Plants/tulip2.jpg',
			'Plants/bonnet2.jpg',
			'Plants/daffodil2.jpg',
			'Plants/waterlily2.jpg',
			'Plants/lavender2.jpg',
			'Plants/buttercup2.jpg']
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
			if(stage<0):
				if(mouseX>=18 and mouseX<=78 and mouseY>=18 and mouseY<=41):
					stage=0

			elif(stage==0):
				if(mouseX>=160 and mouseX<=240 and mouseY>=150 and mouseY<=175):
					stage=1
				elif(mouseX>=160 and mouseX<=240 and mouseY>=195 and mouseY<=220):
					stage=-1
				elif(mouseX>=160 and mouseX<=240 and mouseY>=240 and mouseY<=265):
					stage=-2

			elif(stage==1):
				#print(ceil(mouseX/(400/3)), ceil(mouseY/(300/3)), )
				flowerNum=ceil(mouseX/(400/3))-4+(ceil(mouseY/(300/3))*3)
				stage=2

			elif(stage==2):
				if(mouseX>=15 and mouseX<=73 and mouseY>=14 and mouseY<=39):
					dosh=0
					inc=1
					stage=0
				elif(mouseX>=15 and mouseX<=73 and mouseY>=45 and mouseY<=70):
					stage=3
				else:
					dosh+=inc

			elif(stage==3):
				if(mouseX>=15 and mouseX<=73 and mouseY>=14 and mouseY<=39):
					stage=2

	screen.fill(white)
	if(stage==-2):#Credits
		pygame.draw.rect(screen,black,(18,18,60,23),3)
		screen.blit(font2.render("Back",False,black), (26,18))
		screen.blit(sFont.render("Credits",False,black), (133,0))
		screen.blit(font2.render("Programmed by:",False,black), (126.5,55))
		screen.blit(font2.render("Jordan Camilletti",False,black), (127,80))
		screen.blit(font2.render("Sponsored by:",False,black), (136,125))
		screen.blit(font2.render("The Democratic United Data Electors(DUDE)",False,black), (3,150))
		screen.blit(font2.render("Paid for by:",False,black), (149,195))
		screen.blit(font2.render("The Bureaucratic Recitative Offices(BRO)",False,black), (16.5,220))

	elif(stage==-1):#Help
		pygame.draw.rect(screen,black,(18,18,60,23),3)
		screen.blit(font2.render("Back",False,black), (26,18))
		screen.blit(sFont.render("Help:",False,black), (158.5,0))
		screen.blit(font2.render("",False,black), (0,20))

	elif(stage==0):#starting
		screen.blit(sFont.render("EXTREME!",False,red), (116,25))#\n isn't allowed, so I need to do this
		screen.blit(sFont.render("GARDENING!",False,red), (93.5, 65))
		screen.blit(font2.render("Start",False,black), (178.5, 150))
		screen.blit(font2.render("Help",False,black), (180.5,195))
		screen.blit(font2.render("Credits",False,black), (168.5,240))
		pygame.draw.rect(screen,black,(160,150,80,25),3)
		pygame.draw.rect(screen,black,(160,195,80,25),3)
		pygame.draw.rect(screen,black,(160,240,80,25),3)		
		#print(font2.render("",False,black).get_width()/2)

	elif(stage==1):#Flower Select
		pygame.draw.rect(screen,black,[0,0,2,300])
		for n in range(1,4):
			pygame.draw.rect(screen,black,[(n*133)-1,0,2,300])
		pygame.draw.rect(screen,black,[0,0,400,2])
		for n in range(1,4):
			pygame.draw.rect(screen,black,[0,(n*100)-2,400,2])
		for name in range(len(names)):#This extremely long line is for displaying the names on a 9x9 grid
			screen.blit(font1.render(names[name],False,black) , (((1+(name%3))*66)+((name%3)*66)-(font1.render(names[name],False,black).get_width()/2) , (floor(name/3)*100)+85))
			img=pygame.image.load(seedPhotos[name])
			screen.blit(img, (((1+(name%3))*66)+((name%3)*66)-40 , (floor(name/3)*100)+5))

	elif(stage==2):#Main
		pygame.draw.rect(screen,black,(15,14,58,25),3)
		screen.blit(font2.render("Back",False,black), (20,15))	
		pygame.draw.rect(screen,black,(15,45,58,25),3)
		screen.blit(font2.render("Shop",False,black), (20,46))	
		screen.blit(font2.render("¥{0}".format(dosh),False,black),(320,15))
		img=pygame.image.load(plantPhotos[flowerNum])
		screen.blit(img, (200-(img.get_width()/2),300-img.get_height()))	
		screen.blit(pygame.image.load('Plants/dirt.png'), (0,260))
		

	elif(stage==3):
		pygame.draw.rect(screen,black,(15,14,58,25),3)
		screen.blit(font2.render("Back",False,black), (20,15))	

	pygame.display.update()
	
pygame.quit()
quit()
