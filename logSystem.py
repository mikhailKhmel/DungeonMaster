import pygame
import config


STEP = 64

WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

surfLog = pygame.Surface((WINDOW_HEIGHT,WINDOW_WEIGHT-GAME_HEIGHT))

def blitLog(t,addition,sc):
	logmsgGame = ['УРОВЕНЬ: ' + str(config.player['level']) + ' Up - вверх, Right - вправо, Down - вниз, Left - влево',
				'I - открыть инвентарь', 'SPACE - удар', 'M - включение/выключение звука']

	logmsgGameAdd = ['E - открыть сундук', 'Вы перегружены','Лечебное зелье добавлено в сумку',
	'Меч добавлен в сумку',
	'Копье и щит добавлены в сумку',
	'Кожаная броня добавлена в сумку','Стальная броня добавлена в сумку']

	logmsgInv = ['E - Экипировать или использовать',
					'R - снять оружие',
					'Q - уничтожить предмет']

	logmsgInvAdd = ['На вас надета более прочная броня']
	surfLog.fill((0,0,0))
	font = pygame.font.SysFont('arial',20)
	# text = font.render(config.logmsgGame[s], True, (255,255,255))
	# surfLog.blit(text,(0,x))

	if t == 'game':
		x = 0
		for s in logmsgGame:
			font = pygame.font.SysFont('arial',20)
			text = font.render(s, 1, (255,255,255))
			surfLog.blit(text,(0,x))
			x+=20
		
		for i in addition:
			print('i=',i)
			font = pygame.font.SysFont('arial',20)
			text = font.render(logmsgGameAdd[i],1,(255,255,255))
			surfLog.blit(text,(0,x))
			x+=20
		sc.blit(surfLog,(0,GAME_HEIGHT+STEP))
		return
	elif t == 'inv':
		x = 0
		for s in logmsgInv:
			font = pygame.font.SysFont('arial',20)
			text = font.render(s, 1, (255,255,255))
			surfLog.blit(text,(0,x))
			x+=20
		for i in addition:
			print('i=',i)
			font = pygame.font.SysFont('arial',20)
			text = font.render(logmsgInvAdd[i],1,(255,255,255))
			surfLog.blit(text,(0,x))
			x+=20
		sc.blit(surfLog,(0,GAME_HEIGHT+STEP))
		return
	
