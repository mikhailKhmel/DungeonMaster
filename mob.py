import pygame 
import random
import config
from music import *


udar = pygame.mixer.Sound('music/udar.ogg')
smert = pygame.mixer.Sound('music/smert.ogg')


def mobMovement(tmp):
	x = 0
	y = 0
	dx = random.randint(-1,1)
	dy = random.randint(-1,1)
	if (dx == -1 or dx == 1):
		dy = 0
	else:
		dx = 0 
	for i in range(0, len(tmp)):
		for j in range(0, len(tmp[i])):
			if tmp[i][j] == '5':
				x = i
				y = j
				break
	if tmp[x+dx][y+dy] == '1' or tmp[x+dx][y+dy] == '4' :
		pass
	elif tmp[x+dx][y+dy] == '3':
		pass
	elif tmp[x][y] == '5' and (tmp[x][y+1] == '2' or tmp[x+1][y] == '2' or tmp[x][y-1] == '2' or tmp[x-1][y] == '2'):
		playerHp = config.player['hp'] - 1
		config.player['hp'] = playerHp
	elif tmp[x+dx][y+dy] == '2':
		pass
	else:
		tmp[x][y]='0'
		tmp[x+dx][y+dy]='5'
		config.enemy['i'] = x+dx
		config.enemy['j'] = y+dy

	return tmp		


def mobKiller(tmp):
	xPl = 0
	yPl = 0
	volume = config.PROCENT / 100
	udar.set_volume(volume)
	smert.set_volume(volume)
	for i in range(0, len(tmp)):
		for j in range(0, len(tmp[i])):
			if tmp[i][j] == '2':
				xPl = i
				yPl = j
			elif tmp[i][j] == '5':
				xMob = i
				yMob = j
	if tmp[xPl][yPl] == '2' and (tmp[xPl][yPl+1] == '5' or tmp[xPl+1][yPl] == '5' or tmp[xPl][yPl-1] == '5' or tmp[xPl-1][yPl] == '5'):
		enemyHp = config.enemy['hp'] - 1
		config.enemy['hp'] = enemyHp
		if config.enemy['hp'] == 0 and config.amount == 0:
			if tmp[xPl][yPl+1] == '5':
				tmp[xPl][yPl+1] = '0'
			elif tmp[xPl+1][yPl] == '5':
				tmp[xPl+1][yPl] = '0'
			elif tmp[xPl][yPl-1] == '5':
				tmp[xPl][yPl-1] = '0'
			elif tmp[xPl-1][yPl] == '5':
				tmp[xPl-1][yPl] = '0' 
			config.amount = 1
			openSound(smert)
		elif config.amount > 0:
			config.enemy['hp'] = 2
			config.amount = 0

	print(config.enemy['hp'])

	return tmp	
