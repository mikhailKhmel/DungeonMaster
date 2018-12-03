import pygame
import random
import config
import mob
import os

STEP = 64

WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

level = 1

surfGameDark = pygame.Surface((GAME_HEIGHT,GAME_WEIGHT))
surfGame = pygame.Surface((GAME_HEIGHT,GAME_WEIGHT))

surfGameLight = pygame.Surface((GAME_HEIGHT-4*STEP,GAME_HEIGHT-4*STEP))

surfHp = pygame.Surface((STEP,GAME_WEIGHT))
surfMob = pygame.Surface((STEP,STEP))
surfPlayer = pygame.Surface((STEP,STEP))


def blitImg(tpe,dark,dx,dy):
	if dark==True:
		if tpe=='1':
			img=pygame.image.load(config.dictEnv[1]+'/dark/tipo_stena.bmp')
			img_rect=img.get_rect(topleft=(dx,dy))
			surfGameLight.blit(img,img_rect)
		else:
			img=pygame.image.load(config.dictEnv[0]+'/dark/plitka1.bmp')
			img_rect=img.get_rect(topleft=(dx,dy))
			surfGameLight.blit(img,img_rect)
	else:
		if tpe=='0':
			img=pygame.image.load(config.dictEnv[0]+'/light/plitka1.bmp')
			img_rect=img.get_rect(topleft=(dx,dy))
			surfGameLight.blit(img,img_rect)
		elif tpe=='1':
			img=pygame.image.load(config.dictEnv[1]+'/light/tipo_stena.bmp')
			img_rect=img.get_rect(topleft=(dx,dy))
			surfGameLight.blit(img,img_rect)
		elif tpe=='2':
			img=pygame.image.load(config.dictEnv[2])
			img_rect=img.get_rect(topleft=(dx,dy))
			surfGameLight.blit(img,img_rect)
		elif tpe=='3':
			img=pygame.image.load(config.dictEnv[3])
			img_rect=img.get_rect(topleft=(dx,dy))
			surfGameLight.blit(img,img_rect)
		elif tpe=='4':
			img=pygame.image.load(config.dictEnv[4])
			img_rect=img.get_rect(topleft=(dx,dy))
			surfGameLight.blit(img,img_rect)
		elif tpe=='5':
			img=pygame.image.load(config.dictEnv[5])
			img_rect=img.get_rect(topleft=(dx,dy))
			surfGameLight.blit(img,img_rect)
		elif tpe=='a':
			img=pygame.image.load(config.dictEnv[10])
			img_rect=img.get_rect(topleft=(dx,dy))
			surfGameLight.blit(img,img_rect)

def loadMap():
	config.mobs.clear()
	print('level=',config.player['level'])
	path = 'maps/' + str(random.randint(1,len(os.listdir('maps/')))) + '.txt'
	f = open(path, 'r')
	s = f.read()
	m = []
	tmp = []
	for x in range(0,len(s)):
		if s[x]=='\n':
			m.append(tmp)
			tmp = []
		else:
			tmp.append(s[x])
	return m


def renderMap(maps,sc):

	for i in range(0,len(maps)):
		for j in range(0,len(maps[i])):
			if maps[i][j] == '2':
				config.player['i'] = i
				config.player['j'] = j


	startIdark = config.player['i'] - 4
	startJdark = config.player['j'] - 4
	endIdark = startIdark + 10
	endJdark = startJdark + 10

	x=0
	y=0
	for i in range(startIdark,endIdark):
		for j in range(startJdark,endJdark):
			if maps[i][j]=='0':
				img=pygame.image.load(config.dictEnv[0]+'/dark/plitka1.bmp')
				img_rect=img.get_rect(topleft=(x,y))
				surfGameDark.blit(img,img_rect)
			elif maps[i][j]=='1':
				img=pygame.image.load(config.dictEnv[1]+'/dark/tipo_stena.bmp')
				img_rect=img.get_rect(topleft=(x,y))
				surfGameDark.blit(img,img_rect)
			x+=STEP
		x=0
		y+=STEP
	sc.blit(surfGameDark,(0,0))

	startIlight = config.player['i'] - 2
	startJlight = config.player['j'] - 2
	endIlight = startIlight + 5
	endJlight = startJlight + 5

	x=0
	y=0
	c=0
	sector1=[1,2,3]
	sector2=[5,10,15]
	sector3=[9,14,19]
	sector4=[21,22,23]
	sector5=[0,4,20,24]
	for i in range(startIlight,endIlight):
		for j in range(startJlight,endJlight):
			if c in sector1 or c in sector2 or c in sector3 or c in sector4 or c in sector5:
				if c in sector1:
					if maps[i+1][j]=='1':
						blitImg(maps[i][j],True,x,y)
					else:
						blitImg(maps[i][j],False,x,y)

				if c in sector2:
					if maps[i][j+1]=='1':
						blitImg(maps[i][j],True,x,y)
					else:
						blitImg(maps[i][j],False,x,y)

				if c in sector3:
					if maps[i][j-1]=='1':
						blitImg(maps[i][j],True,x,y)
					else:
						blitImg(maps[i][j],False,x,y)

				if c in sector4:
					if maps[i-1][j]=='1':
						blitImg(maps[i][j],True,x,y)
					else:
						blitImg(maps[i][j],False,x,y)

				if c in sector5:
					if c==0:
						if maps[i+1][j+1]=='1':
							blitImg(maps[i][j],True,x,y)
						else:
							blitImg(maps[i][j],False,x,y)

					if c==4:
						if maps[i+1][j-1]=='1':
							blitImg(maps[i][j],True,x,y)
						else:
							blitImg(maps[i][j],False,x,y)

					if c==20:
						if maps[i-1][j+1]=='1':
							blitImg(maps[i][j],True,x,y)
						else:
							blitImg(maps[i][j],False,x,y)

					if c==24:
						if maps[i-1][j-1]=='1':
							blitImg(maps[i][j],True,x,y)
						else:
							blitImg(maps[i][j],False,x,y)	
			else:
				blitImg(maps[i][j],False,x,y)	
			c+=1
			x+=STEP
		x=0
		y+=STEP

	sc.blit(surfGameLight,(STEP*2,STEP*2))

def renderHP(sc):
	hp=[]
	if config.player['hp'] == 6: 
		hp=[2,2,2]
	elif config.player['hp'] == 5: 
		hp=[2,2,1]
	elif config.player['hp'] == 4: 
		hp=[2,2,0]
	elif config.player['hp'] == 3: 
		hp=[2,1,0]
	elif config.player['hp'] == 2:
		hp=[2,0,0]
	elif config.player['hp'] == 1: 
		hp=[1,0,0]
	elif config.player['hp'] == 0: 
		hp=[0,0,0]
	#print('hp=',hp)
	x=0
	y=GAME_HEIGHT
	for i in hp:
		img = pygame.image.load('srcBMP/hp/hp'+str(i)+'.bmp')
		img_rect = img.get_rect(topleft=(x,y))
		sc.blit(img,img_rect)
		x+=STEP
	#sc.blit(surfHp,(0,GAME_WEIGHT))


def renderList(dx,dy,level,tmp):
	x=0
	y=0
	for i in range(0,len(tmp)):
		for j in range(0,len(tmp[i])):
			if (tmp[i][j]=='2'):
				x=i
				y=j
				break

	if tmp[x+dx][y+dy] == '1' or tmp[x+dx][y+dy] == '4' or tmp[x+dx][y+dy] == 'a' or tmp[x+dx][y+dy] == '5':
		pass
	elif tmp[x+dx][y+dy] == '3':
		config.player['level']+=1
		tmp=loadMap()
	else:
		tmp[x][y]='0'
		tmp[x+dx][y+dy]='2'
		config.player['i'] = x+dx
		config.player['j'] = y+dy

	return tmp

def redMob(maps,sc):
	x=config.player['i']
	y=config.player['j']
	surfMob.set_alpha(0)
	surfMob.fill((0,0,0))
	dx=0
	dy=0
	if maps[x-1][y]=='5':
		dx=STEP*4
		dy=STEP*3
	elif maps[x][y-1]=='5':
		dx=STEP*3
		dy=STEP*4
	elif maps[x+1][y]=='5': 
		dx=STEP*4
		dy=STEP*5
	elif maps[x][y+1]=='5':
		dx=STEP*5
		dy=STEP*4
	print('dx=',dx,'\tdy=',dy)
	if dx==0 and dy==0:
		return
	else:
		img=pygame.image.load('srcBMP/env/light/redMob.bmp')
		img_rect=img.get_rect(topleft=(dx,dy))
		sc.blit(img,img_rect)

def redPlayer(sc):
	surfPlayer.set_alpha(0)
	surfPlayer.fill((0,0,0))
	img=pygame.image.load('srcBMP/env/light/redMob.bmp')
	img_rect=img.get_rect(topleft=(STEP*4,STEP*4))
	sc.blit(img,img_rect)