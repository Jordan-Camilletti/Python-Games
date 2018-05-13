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

while(not finish):
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			finish=True
		if(event.type == pygame.KEYDOWN):#Space=pause/unpause
			if(event.key == pygame.K_SPACE):
				pause=not pause

	if(not pause):
		turn+=1
		t=findSize(turn)
		#print(9**(turn-1))
		#print(t)
		for n in range(9**(turn-1)):
			#print(t+(math.floor(n%3)*findSize(turn-1)),t+(math.floor(n/3)*findSize(turn-1)))
		#print("\n")
			pygame.draw.rect(screen,white,[t+(math.floor(n%3)*findSize(turn-1)),t+(math.floor(n/3)*findSize(turn-1)),t,t])
		"""pygame.draw.rect(screen,white,[300,300,300,300])
		pygame.draw.rect(screen,white,[100,100,100,100])
		pygame.draw.rect(screen,white,[400,100,100,100])
		pygame.draw.rect(screen,white,[700,100,100,100])
		pygame.draw.rect(screen,white,[100,100,100,100])
		pygame.draw.rect(screen,white,[700,700,100,100])
		pygame.draw.rect(screen,white,[33,33,33,33])
		pygame.draw.rect(screen,white,[133,33,33,33])
		pygame.draw.rect(screen,white,[33,133,33,33])"""

		"""pygame.draw.rect(screen,white,[900/(3**1),900/(3**1),900/(3**1),900/(3**1)])
		pygame.draw.rect(screen,white,[900/(3**2),900/(3**2),900/(3**2),900/(3**2)])
		pygame.draw.rect(screen,white,[900/(3**3),900/(3**3),900/(3**3),900/(3**3)])"""
		pygame.time.wait(1000)
	pygame.display.update()
	
pygame.quit()
quit()
