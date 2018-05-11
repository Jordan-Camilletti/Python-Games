#Sierpinski Carpet
"""
"""

import pygame

def findSize(t):
	return(900/(3**t))
	
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

	if(not pause):
		turn+=1
		t=findSize(turn)
		for n in range(9**(turn-1)):
			pygame.draw.rect(screen,white,[t,t,t,t])
		"""pygame.draw.rect(screen,white,[900/(3**1),900/(3**1),900/(3**1),900/(3**1)])
		pygame.draw.rect(screen,white,[900/(3**2),900/(3**2),900/(3**2),900/(3**2)])
		pygame.draw.rect(screen,white,[900/(3**3),900/(3**3),900/(3**3),900/(3**3)])"""
		pygame.time.wait(1000)
	pygame.display.update()
	
pygame.quit()
quit()
