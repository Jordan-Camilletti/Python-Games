#Sierpinski Carpet
"""
"""

import pygame
import math

def findSize(t):
	return(math.floor(900/(3**t)))
	
pygame.init()
white=(255,255,255)
black=(0,0,0)
turn=0
currSize=300
finish=False
pause=False
screen=pygame.display.set_mode((900, 900))
pygame.display.set_caption("Sierpinski's Carpet")

while(turn<3):
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
				print(t+(n1*findSize(turn-1)), t+(n2*findSize(turn-1)))
				pygame.draw.rect(screen,white,[t+(n1*findSize(turn-1)), t+(n2*findSize(turn-1)),t,t])
			print("X")
		print("\n")
		"""pygame.draw.rect(screen,white,[300,300,300,300])
		pygame.draw.rect(screen,white,[100,100,100,100])
		pygame.draw.rect(screen,white,[400,100,100,100])
		pygame.draw.rect(screen,white,[700,100,100,100])
		pygame.draw.rect(screen,white,[100,100,100,100])
		pygame.draw.rect(screen,white,[700,700,100,100])
		pygame.draw.rect(screen,white,[33,33,33,33])
		pygame.draw.rect(screen,white,[133,33,33,33])
		pygame.draw.rect(screen,white,[33,133,33,33])"""

		pygame.time.wait(1000)
	pygame.display.update()
	
pygame.quit()
quit()
