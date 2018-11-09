import pygame 
import random
import config
from music import *


udar = pygame.mixer.Sound('music/udar.ogg')
smert = pygame.mixer.Sound('music/smert.ogg')

def mobForDamage(tmp,x,y):
	if tmp[x+1][y]=='5' or tmp[x][y+1]=='5' or tmp[x-1][y]=='5' or tmp[x][y-1]=='5':
		return True
	else:
		return False


def playerForDamage(tmp,x,y):	#функция проверки игрока рядом с мобом
	if tmp[x+1][y]=='2' or tmp[x][y+1]=='2' or tmp[x-1][y]=='2' or tmp[x][y-1]=='2':
		return True
	else:
		return False
		

def mobMovement(tmp):
	print('count of mobs =',len(config.mobs))
	for c in range(0,len(config.mobs)):
		playerNearby=False
		x = config.mobs[c]['i']
		y = config.mobs[c]['j']
		for i in range(x-3,x+3):
			for j in range(y-3,y+3):
				if tmp[i][j]=='2':
					playerNearby=True
					#config.player['hp']=config.player['hp']-config.mobs[c]['power']
		print('playerNearby=',playerNearby)

		if playerNearby==False:
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
			#алгоритм приближения моба к игроку
			if playerForDamage(tmp,x,y) == True:
				config.player['hp']=config.player['hp']+config.player['arm']-config.mobs[c]['power']
			else:
				diffX = config.player['i'] - x
				diffY = config.player['j'] - y
				dx=[]
				dy=[]
				if diffX<0 and diffY<0:
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

				flag=False
				newX=0
				newY=0
				for i in dx:
					for j in dy:
						if tmp[x+i][y+j]=='0':
							flag=True
							newX=i
							newY=j
							break
					if flag==True:
						break

				if flag==True:
					config.mobs[c]['i']=x+newX
					config.mobs[c]['j']=y+newY
					tmp[x][y]='0'
					tmp[x+newX][y+newY]='5'

				x = config.mobs[c]['i']
				y = config.mobs[c]['j']
				if playerForDamage(tmp,x,y) == True:
					config.player['hp']=config.player['hp']+config.player['arm']-config.mobs[c]['power']

	print(config.mobs)
	return tmp		


def mobKiller(tmp):
	volume = config.PROCENT / 100
	udar.set_volume(volume)
	smert.set_volume(volume)

	x=config.player['i']
	y=config.player['j']

	if tmp[x+1][y]=='5':
		for c in config.mobs:
			if x+1==c['i'] and y==c['j']:
				c['hp']=c['hp']-config.player['power']
				config.player['hp']=config.player['hp']+config.player['arm']-c['power']
				if c['hp']<=0:
					config.mobs.remove(c)
					tmp[x+1][y]='0'
					openSound(smert)
				else:
					openSound(udar)
				return tmp,True
	elif tmp[x][y+1]=='5':
		for c in config.mobs:
			if x==c['i'] and y+1==c['j']:
				c['hp']=c['hp']-config.player['power']
				config.player['hp']=config.player['hp']+config.player['arm']-c['power']
				if c['hp']<=0:
					config.mobs.remove(c)
					tmp[x][y+1]='0'
					openSound(smert)
				else:
					openSound(udar)
				return tmp,True
	elif tmp[x-1][y]=='5':
		for c in config.mobs:
			if x-1==c['i'] and y==c['j']:
				c['hp']=c['hp']-config.player['power']
				config.player['hp']=config.player['hp']+config.player['arm']-c['power']
				if c['hp']<=0:
					config.mobs.remove(c)
					tmp[x-1][y]='0'
					openSound(smert)
				else:
					openSound(udar)
				return tmp,True
	elif tmp[x][y-1]=='5':
		for c in config.mobs:
			if x==c['i'] and y-1==c['j']:
				c['hp']=c['hp']-config.player['power']
				config.player['hp']=config.player['hp']+config.player['arm']-c['power']
				if c['hp']<=0:
					config.mobs.remove(c)
					tmp[x][y-1]='0'
					openSound(smert)
				else:
					openSound(udar)
				return tmp,True
	else:
		return tmp,False


def scanMobs(maps):
	c=0
	for i in range(0,len(maps)):
		for j in range(0,len(maps[i])):
			if maps[i][j]=='5':
				hp = random.randint(4,6)
				power = random.choice([1,2,3,4])
				mob = {'id':c,'hp':hp,'power':power,'i':i,'j':j}
				config.mobs.append(mob)
				c+=1

	print(config.mobs)