#EXTREME GARDENING
"""IT'S GARDENING
IT'S EXTREME
IT'S PLAYED BY CLICKING
IT'S EXTREME GARDENING"""

import pygame
from math import floor, ceil

def buy(costs,choice,dosh):
	incs=[0.0,0.0,0.0]#returns cost, dosh inc, tes inc
	if(int(costs[choice].split(" ")[0])<=dosh):
		incs[0]=int(costs[choice].split(" ")[0])
		incs[1]=int(costs[choice].split(" ")[1])
		incs[2]=int(costs[choice].split(" ")[2])
	#print(costs[choice])
	return(incs)

def shopPrint(x,y,d,cos,con):
	desc=d[(floor(x/80)-1)+(4*floor(y/100))]
	if(con!=(floor(x/80)-1)+(4*floor(y/100))):
		print(desc)
	return(floor(x/80)-1)+(4*floor(y/100))

def findSize(size, tes):#Gets the size of the flower based on clicks
	tPercent=(tes/1000.0)
	nSize=floor(size*tPercent)
	return(nSize)

def gridDisplay(name, b):#Used to display names from arrays onto a grid
	if(b):
		return(((1+(name%3))*66)+((name%3)*66))
	return(floor(name/3)*100)

print("")
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
finish=False
confirm1=-1
confirm2=-1
mInc=1#Money increase
tInc=1#Testosterone increase
dosh=0#Money
tes=0#Testosterone leves
flowerNum=0
stage=0#-2=credits,-1=help,0=menu,1=seed,2=grow,3=upgrade

sFont=pygame.font.SysFont('Impact',45)#starting font
cFont=pygame.font.SysFont('Arial', 15)#credits font
font1=pygame.font.SysFont('Arial', 10)
font2=pygame.font.SysFont('Arial', 20)

screen=pygame.display.set_mode((400,300))
screen.fill(white)
pygame.display.set_caption("EXTREME GARDENING!")

descriptions=open('Assets/Texts/Descriptions.txt','r').readlines()#Loading the info from Texts
names=open('Assets/Texts/Names.txt','r').readlines()
photos=open('Assets/Texts/Photos.txt','r').readlines()
shops=open('Assets/Texts/Shops.txt','r').readlines()

while(not finish):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			finish=True
		if(event.type == pygame.MOUSEBUTTONDOWN):
			mouseX,mouseY=pygame.mouse.get_pos()
			if(stage<0):#Credits and help
				if(mouseX>=18 and mouseX<=78 and mouseY>=18 and mouseY<=41):
					stage=0

			elif(stage==0):#Start
				if(mouseX>=160 and mouseX<=240 and mouseY>=150 and mouseY<=175):
					stage=1
				elif(mouseX>=160 and mouseX<=240 and mouseY>=195 and mouseY<=220):
					stage=-1
				elif(mouseX>=160 and mouseX<=240 and mouseY>=240 and mouseY<=265):
					stage=-2

			elif(stage==1):#Seed select
				#print(ceil(mouseX/(400/3)), ceil(mouseY/(300/3)), )
				flowerNum=ceil(mouseX/(400/3))-4+(ceil(mouseY/(300/3))*3)
				stage=2

			elif(stage==2):#Main game
				if(mouseX>=15 and mouseX<=73 and mouseY>=14 and mouseY<=39):
					dosh=0
					mInc=1
					tInc=1
					tes=0
					stage=0
				elif(mouseX>=15 and mouseX<=73 and mouseY>=45 and mouseY<=70):
					stage=3
				else:
					dosh+=mInc
					tes+=tInc

			elif(stage==3):#Shop screen
				if(mouseX>=15 and mouseX<=73 and mouseY>=14 and mouseY<=39):
					stage=2
					confirm1=-1
					confirm2=-2
				if(mouseX>=82):
					confirm1=shopPrint(mouseX,mouseY,descriptions,shops,confirm2)
					if(confirm1==confirm2):
						changes=buy(shops,confirm1,dosh)
						dosh-=changes[0]
						mInc+=changes[1]
						tInc+=changes[2]
					else:
						print("Costs ¥{0}".format(shops[confirm1].split(" ")[0]))
						print("Click again to buy\n")
						confirm2=confirm1
					"""print(floor(mouseX/80)-1)
					print(floor(mouseY/100))
					print((floor(mouseX/80)-1)+(4*floor(mouseY/100)))"""

	screen.fill(white)
	if(stage==-2):#Credits
		pygame.draw.rect(screen,black,(18,18,60,23),3)
		screen.blit(font2.render("Back",False,black), (26,18))
		screen.blit(sFont.render("Credits",False,black), (133,0))
		screen.blit(font2.render("Programmed by:",False,black), (int(126.5),55))
		screen.blit(font2.render("Jordan Camilletti",False,black), (127,80))
		screen.blit(font2.render("Sponsored by:",False,black), (136,125))
		screen.blit(font2.render("The Democratic United Data Electors(DUDE)",False,black), (3,150))
		screen.blit(font2.render("Paid for by:",False,black), (149,195))
		screen.blit(font2.render("The Bureaucratic Recitative Offices(BRO)",False,black), (int(16.5),220))

	elif(stage==-1):#Help
		pygame.draw.rect(screen,black,(18,18,60,23),3)
		screen.blit(font2.render("Back",False,black), (26,18))
		screen.blit(sFont.render("Help:",False,black), (int(158.5),0))
		screen.blit(font2.render("CLICK ON THE SCREEN",False,black), (int(88.5),80))
		screen.blit(font2.render("GET TESTOSTERONE",False,black), (int(96.5),110))
		screen.blit(font2.render("GET THOSE GAINS",False,black), (int(109.5),140))
		screen.blit(font2.render("RESPECT YOUR ELDERS",False,black), (int(80.5),170))
		screen.blit(font2.render("ALWAYS USE YOUR TURN SIGNALS",False,black), (int(37.5),200))
		screen.blit(font2.render("DONATE TO CHARITY",False,black), (97,230))

	elif(stage==0):#Starting
		screen.blit(sFont.render("EXTREME!",False,red), (116,25))#\n isn't allowed, so I need to do this
		screen.blit(sFont.render("GARDENING!",False,red), (int(93.5), 65))
		screen.blit(font2.render("Start",False,black), (int(178.5), 150))
		screen.blit(font2.render("Help",False,black), (int(180.5),195))
		screen.blit(font2.render("Credits",False,black), (int(168.5),240))
		for n in range(3):
			pygame.draw.rect(screen,black,(160,150+(n*45),80,25),3)
		#print(font2.render("",False,black).get_width()/2)

	elif(stage==1):#Flower Select
		pygame.draw.rect(screen,black,[0,0,2,300])
		for n in range(1,4):
			pygame.draw.rect(screen,black,[(n*133)-1,0,2,300])
		pygame.draw.rect(screen,black,[0,0,400,2])
		for n in range(1,4):
			pygame.draw.rect(screen,black,[0,(n*100)-2,400,2])

		for name in range(len(names)):#This extremely long line is for displaying the names on a 9x9 grid
			screen.blit(font1.render(names[name][:-1],False,black) , (gridDisplay(name,1)-int(font1.render(names[name],False,black).get_width()/2) , gridDisplay(name,0)+85))
			img=pygame.image.load(photos[name][:-1])
			screen.blit(img, (gridDisplay(name,1)-40 , gridDisplay(name,0)+5))
			#((1+(name%3))*66)+((name%3)*66)
			#(floor(name/3)*100)

	elif(stage==2):#Main game
		pygame.draw.rect(screen,black,(15,14,58,25),3)
		screen.blit(font2.render("Exit",False,black), (20,15))	
		pygame.draw.rect(screen,black,(15,45,58,25),3)
		screen.blit(font2.render("Shop",False,black), (20,46))	

		screen.blit(font1.render("Dosh:",False,black),(320,15))
		screen.blit(font1.render("¥{0}".format(dosh),False,black),(320,25))
		screen.blit(font1.render("Testosterone:",False,black),(320,45))
		screen.blit(font1.render("{0} ng/dl".format(tes),False,black),(320,55))

		img=pygame.image.load(photos[flowerNum+9][:-1])
		currImg=pygame.transform.scale(img, (findSize(img.get_width(),tes), findSize(img.get_height(),tes)))
		screen.blit(currImg, (200-int(currImg.get_width()/2),300-currImg.get_height()))	
		screen.blit(pygame.image.load('Assets/Plants/dirt.png'), (0,260))
		

	elif(stage==3):#Shop 
		pygame.draw.rect(screen,black,(15,14,58,25),3)
		screen.blit(font2.render("Back",False,black), (20,15))	
		screen.blit(font1.render("Dosh:",False,black), (15,50))
		screen.blit(font1.render("¥{0}".format(dosh),False,black), (15,65))
		screen.blit(font1.render("Dosh",False,black), (15,95))
		screen.blit(font1.render("Increase:",False,black), (15,105))
		screen.blit(font1.render("x{0}".format(mInc),False,black), (15,120))
		screen.blit(font1.render("Testosterone",False,black), (15,150))
		screen.blit(font1.render("Increase:",False,black), (15,160))
		screen.blit(font1.render("x{0}".format(tInc),False,black), (15,175))

		screen.blit(font1.render("Supa' Soil",False,black), (120-int(24.5),85))
		screen.blit(font1.render("Words of",False,black), (200-int(20.5),75))
		screen.blit(font1.render("Encouragement",False,black), (200-38,85))
		screen.blit(font1.render("Capitalism",False,black), (280-25,85))
		screen.blit(font1.render("Flower Power",False,black), (360-int(31.5),85))

		screen.blit(font1.render("Protien Powder",False,black), (120-36,185))
		screen.blit(font1.render("Get a Real Job",False,black), (200-int(35.5),185))
		screen.blit(font1.render("Really Cool",False,black), (280-int(27.5),175))
		screen.blit(font1.render("Gloves",False,black), (280-16,185))
		screen.blit(font1.render("Gym",False,black), (360-11,175))
		screen.blit(font1.render("Membership",False,black), (360-29,185))

		screen.blit(font1.render("UV Lights",False,black), (120-int(22.5),285))
		screen.blit(font1.render("Extra",False,black), (200-12,275))
		screen.blit(font1.render("Mitochondria",False,black), (200-int(31.5),285))
		screen.blit(font1.render("Wrestling",False,black), (280-int(21.5),275))
		screen.blit(font1.render("Movies",False,black), (280-int(16.5),285))
		screen.blit(font1.render("SLIM JIMS™",False,black), (360-31,285))

		for n in range(1,5):#Drawling shop grid
			pygame.draw.rect(screen,black,(n*80,0,1,300),2)
		pygame.draw.rect(screen,black,(398,0,1,300),2)
		for n in range(3):
			pygame.draw.rect(screen,black,(80,n*100,400,1),2)
		pygame.draw.rect(screen,black,(80,298,400,1),2)

		for name in range(12):
			img=pygame.image.load(photos[name+18][:-1])
			screen.blit(img, (2+(80*(1+(name%4))) , 2+(100*floor(name/4))))

	pygame.display.update()
pygame.quit()
quit()