#"Conway's GOL".py
"""For a space that is 'populated':
Each cell with one or no neighbors dies, as if by solitude.
Each cell with four or more neighbors dies, as if by overpopulation.
Each cell with two or three neighbors survives.
For a space that is 'empty' or 'unpopulated'
Each cell with three neighbors becomes populated."""
import pygame
from math import floor

pygame.init()
white=(255,255,255)
black=(0,0,0)
finish=False
pause=True
grid=[[False]*80 for n in range(60)]#60 arrays that are size 80
xPos,yPos=0,0
screen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("Conway's Game of Life.")
#clock = pygame.time.Clock()

def populate(grid,x,y):
	score=9
	for ny in range(y-1,y+1):
		for nx in range(x-1,x+1):
			if(ny<0 or nx<0):
				score-=1
			elif(ny>=60 or nx>=80):
				score-=1
			elif(grid[ny][nx]):
				score-=1
	return((grid and score>=2 and score<=3) or (score==3 and not grid[y][x]))


while(not finish):
	for event in pygame.event.get():
		#print(event)
		if(event.type == pygame.QUIT):
			finish=True
		if(event.type == pygame.KEYDOWN):#Space=pause
			if(event.key == pygame.K_SPACE):
				pause=not pause
		if(event.type == pygame.MOUSEBUTTONDOWN):#clicking on square flips it
			mouseX,mouseY=pygame.mouse.get_pos()
			grid[floor(mouseY/5)][floor(mouseX/5)]=not grid[floor(mouseY/5)][floor(mouseX/5)]
			if(grid[floor(mouseY/5)][floor(mouseX/5)]):
				pygame.draw.rect(screen,white,[floor(mouseX/5)*5,floor(mouseY/5)*5,5,5])
			else:
				pygame.draw.rect(screen,black,[floor(mouseX/5)*5,floor(mouseY/5)*5,5,5])

	if(not pause):
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
