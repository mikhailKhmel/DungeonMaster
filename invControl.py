import pygame
from renderGame import *
STEP = 64

def openInv(inv,sc):
	invcell = inv[1][1]
	inv[1][1] = '4'
	a = 1
	b = 1
	renderInv(inv,sc)
	while True:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			elif i.type == pygame.KEYDOWN:
				if i.key == pygame.K_i:
					inv[a][b] = invcell
					renderInv(inv,sc)
					invcell = '0'
					return
				elif i.key == pygame.K_e:
					invcell = '1'
				elif i.key == pygame.K_UP:
					invcell = moveInv(-1,0,inv,invcell)
					a -= 1
					if a < 1:
						a = 1
				elif i.key == pygame.K_RIGHT:
					invcell = moveInv(0,1,inv,invcell)
					b += 1
					if b > 5:
						b = 5
				elif i.key == pygame.K_DOWN:
					invcell = moveInv(1,0,inv,invcell)
					a += 1
					if a > 5:
						a = 5
				elif i.key == pygame.K_LEFT:
					invcell = moveInv(0,-1,inv,invcell)
					b -= 1
					if b < 1:
						b = 1
				else:
					print('ERROR KEY')
		renderInv(inv,sc)
		pygame.display.update()

def moveInv(dx,dy,inv,invcell):
	x = 0
	y = 0
	for i in range(0,len(inv)):
		for j in range(0,len(inv[i])):
			if (inv[i][j]=='4'):
				x=i
				y=j
				break
	if inv[x+dx][y+dy] == '0':
		pass
	else:
		inv[x][y] = invcell
		invcell = inv[x+dx][y+dy]
		inv[x+dx][y+dy] = '4'
	return invcell