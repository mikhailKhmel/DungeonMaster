import pygame
from renderGame import *

STEP = 64

surfSelect = pygame.Surface((STEP,STEP))

def openInv(inv,maps,player,randPlitka,sc):
	a = 5
	b = 1
	surfSelect.set_alpha(127)
	renderInv(inv,surfSelect,a,b,sc)
	while True:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			elif i.type == pygame.KEYDOWN:
				if i.key == pygame.K_i:
					surfSelect.set_alpha(0)
					renderInv(inv,surfSelect,a,b,sc)
					return
				elif i.key == pygame.K_e:
					if inv[a][b] == '5':
						player['hp'] +=2
					inv[a][b] = '1'
				elif i.key == pygame.K_q:
					inv[a][b] = '1'
				elif i.key == pygame.K_UP:
					a -= 1
					if a < 5:
						a = 5
				elif i.key == pygame.K_RIGHT:
					b += 1
					if b > 5:
						b = 5
				elif i.key == pygame.K_DOWN:
					a += 1
					if a > 7:
						a = 7
				elif i.key == pygame.K_LEFT:
					b -= 1
					if b < 1:
						b = 1
				else:
					print('ERROR KEY')
		renderInv(inv,surfSelect,a,b,sc)
		renderMap(maps,player,randPlitka,sc)
		pygame.display.update()