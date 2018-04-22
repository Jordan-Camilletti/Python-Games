#
"""
"""

import pygame

pygame.init()
white=(255,255,255)
black=(0,0,0)
finish=False
pause=False
screen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("Sierpinski's Carpet")

while(not finish):
  for event in pygame.event.get():
    
  pygame.display.update()
  
pygame.quit()
quit()
