"""Conway's GOL".py

For a space that is 'populated':
Each cell with one or no neighbors dies, as if by solitude.
Each cell with four or more neighbors dies, as if by overpopulation.
Each cell with two or three neighbors survives.

For a space that is 'empty' or 'unpopulated':
Each cell with three neighbors becomes populated."""
import pygame
from math import floor

print("Click on a square to populate/depopulate it.\nUse space to pasue/unpause.")
pygame.init()
white=(255,255,255)
black=(0,0,0)
finish=False
pause=True
gridOld=[[False]*80 for n in range(60)]#60 arrays that are size 80
gridNew=[[False]*80 for n in range(60)]#gridOld is what's displayed and is what's checked by populated(), gridNew is what gridOld becomes after populated()
xPos,yPos=0,0
screen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("Conway's Game of Life.")

def populate(grid,x,y):#Determines if a square should be alive or dead based on the 4 rules
	score=0
	for ny in range(y-1,y+2):
		for nx in range(x-1,x+2):
			if(ny>=0 and nx>=0 and ny<60 and nx<80 and (ny!=y or nx!=x)):
				if(grid[ny][nx]):
					score+=1
	if(grid[y][x]):
		return(score==2 or score==3)
	return(score==3)

while(not finish):
	for event in pygame.event.get():
		#print(event)
		if(event.type == pygame.QUIT):
			finish=True
		if(event.type == pygame.KEYDOWN):#Space=pause/unpause
			if(event.key == pygame.K_SPACE):
				pause=not pause
		if(event.type == pygame.MOUSEBUTTONDOWN):#clicking on a square 'flips' it
			mouseX,mouseY=pygame.mouse.get_pos()
			gridNew[floor(mouseY/5)][floor(mouseX/5)]=not gridOld[floor(mouseY/5)][floor(mouseX/5)]
			gridOld[floor(mouseY/5)][floor(mouseX/5)]=not gridOld[floor(mouseY/5)][floor(mouseX/5)]
			if(gridOld[floor(mouseY/5)][floor(mouseX/5)]):
				pygame.draw.rect(screen,white,[floor(mouseX/5)*5,floor(mouseY/5)*5,5,5])
			else:
				pygame.draw.rect(screen,black,[floor(mouseX/5)*5,floor(mouseY/5)*5,5,5])

	if(not pause):
		yPos=-1#Putting the new squares in girdNew based off of gridOld
		for y in gridOld:
			yPos+=1
			xPos=-1
			for x in y:
				xPos+=1
				gridNew[yPos][xPos]=populate(gridOld,xPos,yPos)
		yPos=-1#Drawling gridNew into the window and setting gridOld to gridNew
		for y in gridNew:
			yPos+=1
			xPos=-1
			for x in y:
				xPos+=1
				gridOld[yPos][xPos]=gridNew[yPos][xPos]
				if(x):
					pygame.draw.rect(screen,white,[xPos*5,yPos*5,5,5])
				else:
					pygame.draw.rect(screen,black,[xPos*5,yPos*5,5,5])
		pygame.time.wait(250)
	pygame.display.update()
pygame.quit()
quit()
