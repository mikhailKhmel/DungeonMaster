import pygame 
import random
import config
import renderGameTest
import logSystem
from music import *


udar = pygame.mixer.Sound('music/udar.ogg')
smert = pygame.mixer.Sound('music/smert.ogg')

def playerForDamage(tmp,x,y):							#функция проверки игрока рядом с мобом
	if tmp[x+1][y]=='2' or tmp[x][y+1]=='2' or tmp[x-1][y]=='2' or tmp[x][y-1]=='2':
		return True
	else:
		return False
		

def mobMovement(tmp,sc):		#логика передвижения моба
	print('count of mobs =',len(config.mobs))
	for c in range(0,len(config.mobs)): 
		playerNearby=False 		#флаг нахождения игрока в поле видимости
		x = config.mobs[c]['i']
		y = config.mobs[c]['j']
		for i in range(x-3,x+3):
			for j in range(y-3,y+3):
				if tmp[i][j]=='2':
					playerNearby=True 		#игрок в поле видимости
		print('playerNearby=',playerNearby)

		if playerNearby==False: 		#если игрока рядом нет, то передвижение хаотичное в зависимости от окружения
			dx=random.randint(-1,1)
			dy=random.randint(-1,1)
			if dx==0:
				dy=random.choice([-1,1])
			else:
				dy=0
			if tmp[x+dx][y+dy]=='1' or tmp[x+dx][y+dy]=='4' or tmp[x+dx][y+dy]=='a' or tmp[x+dx][y+dy]=='3' or tmp[x+dx][y+dy]=='2': 
				pass
			else:
				tmp[x+dx][y+dy]='5'
				tmp[x][y]='0'
				config.mobs[c]['i']=x + dx
				config.mobs[c]['j']=y + dy
		else:
			logSystem.blitLog('game',[7],sc)
			#алгоритм приближения моба к игроку
			if playerForDamage(tmp,x,y) == True: #если игрок находится вплотную к мобу, то произвести удар
				print('игрок рядом')
				renderGameTest.redPlayer(sc)
				config.player['hp']=config.player['hp']+config.player['arm']-config.mobs[c]['power']
			else: 
				print('приближаемся с игроку')
				renderGameTest.redPlayer(sc)
				diffX = config.player['i'] - x #просчитываем разницу координат игрока и моба
				diffY = config.player['j'] - y #это дает нам понять в какую сторону надо двигаться мобу
				dx=[]
				dy=[]
				if diffX<0 and diffY<0: #в зависимости от разницы составляются "векторы" направления моба
					dx=[-2,-1]
					dy=[-2,-1]
				elif diffX>0 and diffY<0:
					dx=[2,1]
					dy=[-2,-1]
				elif diffX<0 and diffY>0:
					dx=[-2,-1]
					dy=[2,1]
				elif diffX==0 and diffY<0:
					dx=[0,0]
					dy=[-2,-1]
				elif diffX==0 and diffY>0:
					dx=[0,0]
					dy=[2,1]
				elif diffX<0 and diffY==0:
					dx=[-2,-1]
					dy=[0,0]
				elif diffX>0 and diffY==0:
					dx=[2,1]
					dy=[0,0]
				else:
					pass
				print('вектор\t',dx,'\t',dy)
				flag=False
				newX=0
				newY=0
				for i in dx:
					for j in dy:
						if tmp[x+i][y+j]=='0': #в соответствии с вектором 
							flag=True
							newX=i
							newY=j
							break
					if flag==True:
						break

				if flag==True:
					config.mobs[c]['i']=x+newX #происходит перемещение моба
					config.mobs[c]['j']=y+newY
					tmp[x][y]='0'
					tmp[x+newX][y+newY]='5'

				x = config.mobs[c]['i']
				y = config.mobs[c]['j']
				if playerForDamage(tmp,x,y) == True: #если после передвижения моб оказался рядом с игроков, то производится удар моба
					print('игрок снова рядом')
					renderGameTest.redPlayer(sc)
					config.player['hp']=config.player['hp']+config.player['arm']-config.mobs[c]['power']
					
	#renderGameTest.redPlayer(sc)
	print(config.mobs)
	return tmp		


def mobKiller(sc): #функция удара игрока
	volume = config.PROCENT / 100
	udar.set_volume(volume)
	smert.set_volume(volume)

	x=config.player['i'] #координаты игрока
	y=config.player['j']
	print('в функции')
	if config.maps[x+1][y]=='5': #поиск моба рядом с игроком
		print('удар моба снизу')
		for c in config.mobs:
			if x+1==c['i'] and y==c['j']: #если координаты найденного моба рядом с игроком и координаты моба из ЛИСТА совпадают
				print('моб найден, id=',c['id'])
				c['hp']=c['hp']-config.player['power'] #то производится удар игрока
				config.player['hp']=config.player['hp']+config.player['arm']-c['power'] #и удар моба
				renderGameTest.redPlayer(sc)
				if c['hp']<=0: #если моб умер
					config.mobs.remove(c) #удаление его из листа
					config.maps[x+1][y]='0'
					openSound(smert)
				else:
					openSound(udar)
				return True #возвращаем в main обновление карты и анимацию удара
	elif config.maps[x][y+1]=='5':
		print('удар моба справа')
		for c in config.mobs:
			if x==c['i'] and y+1==c['j']:
				print('моб найден, id=',c['id'])
				c['hp']=c['hp']-config.player['power']
				config.player['hp']=config.player['hp']+config.player['arm']-c['power']
				renderGameTest.redPlayer(sc)
				if c['hp']<=0:
					config.mobs.remove(c)
					config.maps[x][y+1]='0'
					openSound(smert)
				else:
					openSound(udar)
				return True
	elif config.maps[x-1][y]=='5':
		print('удар моба сверху')
		for c in config.mobs:
			if x-1==c['i'] and y==c['j']:
				print('моб найден, id=',c['id'])
				c['hp']=c['hp']-config.player['power']
				config.player['hp']=config.player['hp']+config.player['arm']-c['power']
				renderGameTest.redPlayer(sc)
				if c['hp']<=0:
					config.mobs.remove(c)
					config.maps[x-1][y]='0'
					openSound(smert)
				else:
					openSound(udar)
				return True
	elif config.maps[x][y-1]=='5':
		print('удар моба слева')
		for c in config.mobs:
			if x==c['i'] and y-1==c['j']:
				print('моб найден, id=',c['id'])
				c['hp']=c['hp']-config.player['power']
				config.player['hp']=config.player['hp']+config.player['arm']-c['power']
				renderGameTest.redPlayer(sc)
				if c['hp']<=0:
					config.mobs.remove(c)
					config.maps[x][y-1]='0'
					openSound(smert)
				else:
					openSound(udar)
				return True
	else:
		print('моба рядом нет')
		return False #если моба рядом нет, передаем ту же карту и отсутствие анимации удара


def scanMobs(): #функция сканирования карты для поиска мобов
	lowHp=config.player['level']*2
	highHp=config.player['level']*4
	lowPower=config.player['level']
	highPower=config.player['level']*3
	c=0
	tmp=[]
	for i in range(0,len(config.maps)):
		for j in range(0,len(config.maps[i])):
			if config.maps[i][j]=='5':
				hp = random.randint(lowHp,highHp) #хп от 4 до 6
				power = random.randint(lowPower,highPower) #удар от 1 до 4
				mob = {'id':c,'hp':hp,'power':power,'i':i,'j':j}
				tmp.append(mob) #добавления словаря нового моба в лист
				c+=1
	return tmp