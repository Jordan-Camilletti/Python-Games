#Sierpinski Carpet
"""
"""

import pygame

def findSize(int curr, int turn, int width, int height):
	#

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
    
	if(not pause):
		turn+=1
		pygame.time.wait(250)
	pygame.display.update()
  
pygame.quit()
quit()


