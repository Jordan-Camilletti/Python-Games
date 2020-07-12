#Sierpinski Carpet
"""
"""

import pygame
import math

def findSize(t):
	return(math.floor(size/(3**t)))
	
size=int(input("Enter the width of the screen.\n"))
pygame.init()
white=(255,255,255)
black=(0,0,0)
turn=0
currSize=math.sqrt(size/3)
finish=False
pause=False
screen=pygame.display.set_mode((size, size))
pygame.display.set_caption("Sierpinski's Carpet")

while(not finish and turn<6):
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			finish=True
		if(event.type == pygame.KEYDOWN):#Space=pause/unpause
			if(event.key == pygame.K_SPACE):
				pause=not pause

	if(not pause):
		turn+=1
		t=findSize(turn)
		for n1 in range(int(9**((turn-1)/2))):
			for n2 in range(int(9**((turn-1)/2))):
				pygame.draw.rect(screen,white,[t+(n1*findSize(turn-1)), t+(n2*findSize(turn-1)),t,t])
		pygame.time.wait(1000)
	pygame.display.update()
	
pygame.quit()
quit()
