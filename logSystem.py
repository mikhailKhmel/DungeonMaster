import pygame

STEP = 64

WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

surfLog = pygame.Surface((WINDOW_HEIGHT,STEP))

def scanLog(maps,player,sc):
	surfLog.fill((0,0,0))
	s = 'УРОВЕНЬ: ' + str(player['level']) + ' Up - вверх, Right - вправо, Down - вниз, Left - влево'
	x = player['i']
	y = player['j']
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			if maps[i][j] == '4':
				s+=' E - открыть сундук'
				
	f = pygame.font.SysFont('arial',20)
	text = f.render(s+' E - открыть сундук',1,(255,255,255))
	surfLog.blit(text,(0,0))

	sc.blit(surfLog,(0,GAME_HEIGHT+STEP))
