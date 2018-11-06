import pygame 
import random
import config
from music import *


udar = pygame.mixer.Sound('music/udar.ogg')
smert = pygame.mixer.Sound('music/smert.ogg')

def mobMovement(tmp):
	print('count of mobs =',len(config.mobs))


	for c in range(0,len(config.mobs)):
		playerNearby=False
		x = config.mobs[c]['i']
		y = config.mobs[c]['j']
		for i in range(x-2,x+2):
			for j in range(y-2,y+2):
				if tmp[i][j]=='2':
					playerNearby=True

		if playerNearby==False:
			dx=random.randint(-1,1)
			dy=random.randint(-1,1)
			if dx==0:
				dy=random.choice([-1,1])
			else:
				dy=0
			if tmp[x+dx][y+dy]=='1' or tmp[x+dx][y+dy]=='4' or tmp[x+dx][y+dy]=='a' or tmp[x+dx][y+dy]=='3': 
				pass
			elif tmp[x+dx][y+dy]=='2':
				#алгоритм нанесения урона игроку
			else:
				tmp[x+dx][y+dy]='5'
				tmp[x][y]='0'
				config.mobs[c]['i']=x + dx
				config.mobs[c]['j']=y + dy
		else:
			#алгоритм приближения моба к игроку



	print(config.mobs)
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
		enemyHp = config.enemy['hp'] - config.player['power']
		config.enemy['hp'] = enemyHp
		openSound(udar)
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

def scanMobs(maps):
	c=0
	for i in range(0,len(maps)):
		for j in range(0,len(maps[i])):
			if maps[i][j]=='5':
				hp = random.randint(2,4)
				power = random.choice([0.0,0.5,1.0,1.5,2.0])
				mob = {'id':c,'hp':hp,'power':power,'i':i,'j':j}
				config.mobs.append(mob)
				c+=1

	print(config.mobs)