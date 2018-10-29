import pygame
<<<<<<< Updated upstream
import random
from config import *
=======
import config
>>>>>>> Stashed changes

STEP = 64

WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

logmsgGame = ['УРОВЕНЬ: ' + str(config.player['level']) + ' Up - вверх, Right - вправо, Down - вниз, Left - влево',
				'I - открыть инвентарь',
				'E - открыть сундук']

logmsgInv = ['E - Экипировать или использовать',
				'R - снять оружие',
				'Q - уничтожить предмет',
				'На вас надета более прочная броня']

surfLog = pygame.Surface((WINDOW_HEIGHT,WINDOW_WEIGHT-GAME_HEIGHT))

def blitLog(t,addition,sc):
	surfLog.fill((0,0,0))
	font = pygame.font.SysFont('arial',20)
	# text = font.render(config.logmsgGame[s], True, (255,255,255))
	# surfLog.blit(text,(0,x))

	if t == 'game':
		x = 0
		for s in range(0,len(logmsgGame)-2):
			font = pygame.font.SysFont('arial',20)
			text = font.render(logmsgGame[s], 1, (255,255,255))
			surfLog.blit(text,(0,x))
			x+=20
		if addition==True:
			font = pygame.font.SysFont('arial',20)
			text = font.render(logmsgGame[len(logmsgGame)-1],True,(255,255,255))
			surfLog.blit(text,(0,x))
		sc.blit(surfLog,(0,GAME_HEIGHT+STEP))
		return
	else:
		x = 0
		print('inv')
		for s in range(0,len(logmsgInv)-2):
			font = pygame.font.SysFont('arial',20)
			text = font.render(logmsgInv[s], 1, (255,255,255))
			surfLog.blit(text,(0,x))
			x+=20
		if addition==True:
			font = pygame.font.SysFont('arial',20)
			text = font.render(logmsgInv[len(logmsgInv)-1],True,(255,255,255))
			surfLog.blit(text,(0,x))
		sc.blit(surfLog,(0,GAME_HEIGHT+STEP))
		return
	
