import pygame
from config import *

STEP = 64

WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

surfLog = pygame.Surface((WINDOW_HEIGHT,STEP))

def scanLog(maps,sc):
	surfLog.fill((0,0,0))

	s = 'УРОВЕНЬ: ' + str(player['level']) + ' Up - вверх, Right - вправо, Down - вниз, Left - влево'
	f = pygame.font.SysFont('arial',20)
	text = f.render(s,1,(255,255,255))
	surfLog.blit(text,(0,0))

	s=''
	x = player['i']
	y = player['j']
	flag4 = False
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			if maps[i][j] == '4':
				if flag4==False:
					s+='E - открыть сундук'
					flag4 = True

				
	f = pygame.font.SysFont('arial',20)
	text = f.render(s,1,(255,255,255))
	surfLog.blit(text,(0,20))

	sc.blit(surfLog,(0,GAME_HEIGHT+STEP))
