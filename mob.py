import pygame 
import random
from renderGameTest import *
from config import *

def mobMovement(tmp, enemy):
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
		playerHp = player['hp'] - 1
		player['hp'] = playerHp
	elif tmp[x+dx][y+dy] == '2':
		pass
	else:
		tmp[x][y]='0'
		tmp[x+dx][y+dy]='5'
		enemy['i'] = x+dx
		enemy['j'] = y+dy

	return tmp		


def mobKiller(tmp, enemy):
	xPl = 0
	yPl = 0
	for i in range(0, len(tmp)):
		for j in range(0, len(tmp[i])):
			if tmp[i][j] == '2':
				xPl = i
				yPl = j
			elif tmp[i][j] == '5':
				xMob = i
				yMob = j
	if tmp[xPl][yPl] == '2' and (tmp[xPl][yPl+1] == '5' or tmp[xPl+1][yPl] == '5' or tmp[xPl][yPl-1] == '5' or tmp[xPl-1][yPl] == '5'):
		enemyHp = enemy['hp'] - 1
		enemy['hp'] = enemyHp
		if (enemy['hp'] == 0 and amount == 0):
			if tmp[xPl][yPl+1] == '5':
				tmp[xPl][yPl+1] = '0'
			elif tmp[xPl+1][yPl] == '5':
				tmp[xPl+1][yPl] = '0'
			elif tmp[xPl][yPl-1] == '5':
				tmp[xPl][yPl-1] = '0'
			elif tmp[xPl-1][yPl] == '5':
				tmp[xPl-1][yPl] = '0' 
			amount = 1
		elif (amount > 0):
			enemy['hp'] = 2
			amount = 0

	print(enemy['hp'])

	return tmp	
