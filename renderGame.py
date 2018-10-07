import pygame
import random

STEP = 64

WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

INV_HEIGHT = WINDOW_HEIGHT - GAME_HEIGHT
INV_WEIGHT = GAME_WEIGHT

level = 1

surfGameDark = pygame.Surface((GAME_HEIGHT,GAME_WEIGHT))
surfGame = pygame.Surface((GAME_HEIGHT,GAME_WEIGHT))

surfGameLight = pygame.Surface((GAME_HEIGHT-4*STEP,GAME_HEIGHT-4*STEP))

surfInv = pygame.Surface((INV_HEIGHT,INV_WEIGHT))

surfHp = pygame.Surface((STEP,GAME_WEIGHT))

def loadMap(level):
	#print('level=',level)
	path = 'maps/map' + str(level) + '.txt'
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

def loadInv():
	f = open('inv.txt', 'r')
	s = f.read()
	m = []
	tmp = []
	for x in range(0,len(s)):
		if s[x]=='\n':
			m.append(tmp)
			tmp = []
		else:
			tmp.append(s[x])
	print(m)
	return m

def renderMap(maps,player,randPlitka,sc):
	dictEnv = {	0: 'srcBMP/env',
				1: 'srcBMP/env',
				2: 'srcBMP/player/'+str(player['type'])+'.bmp',
				3: 'srcBMP/env/light/ladder.bmp',
				4: 'srcBMP/env/light/chest.bmp'
			}
			
	for i in range(0,len(maps)):
		for j in range(0,len(maps[i])):
			if maps[i][j] == '2':
				player['i'] = i
				player['j'] = j

	startI = player['i'] - 4
	startJ = player['j'] - 4
	x=0
	y=0
	r=0	
	for i in range(startI,startI+10):
		for j in range(startJ,startJ+10):
			if maps[i][j]=='0':
				if randPlitka[r] == 1:
					img0=pygame.image.load(dictEnv[0]+'/dark/plitka.bmp')
				elif randPlitka[r] == 2:
					img0=pygame.image.load(dictEnv[0]+'/dark/grass_plitka.bmp')
				elif randPlitka[r] == 3:
					img0=pygame.image.load(dictEnv[0]+'/dark/pobitaya_plitka.bmp')
				img0_rect=img0.get_rect(topleft=(x,y))
				surfGameDark.blit(img0,img0_rect)
				r+=1
				x+=STEP
			elif maps[i][j]=='1':
				img1=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
				img1_rect=img1.get_rect(topleft=(x,y))
				surfGameDark.blit(img1,img1_rect)
				x+=STEP
		x=0
		y+=STEP

	sc.blit(surfGameDark,(0,0))

	startI = player['i'] - 2
	startJ = player['j'] - 2
	x=0
	y=0
	r=0
	for i in range(startI,startI+5):
		for j in range(startJ,startJ+5):
			if (i!=0 and j!=0) or (i!=0 and j!=startJ+4) or (i!=startI+4 and j!=0) or (i!=startI+4 and j!=startJ+4):
				if maps[i][j]=='0':
					if randPlitka[r] == 1:
						img0=pygame.image.load(dictEnv[0]+'/light/plitka.bmp')
					elif randPlitka[r] == 2:
						img0=pygame.image.load(dictEnv[0]+'/light/grass_plitka.bmp')
					elif randPlitka[r] == 3:
						img0=pygame.image.load(dictEnv[0]+'/light/pobitaya_plitka.bmp')
					img0_rect=img0.get_rect(topleft=(x,y))
					surfGameLight.blit(img0,img0_rect)
					r+=1
					x+=STEP
				elif maps[i][j]=='1':
					img1=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
					img1_rect=img1.get_rect(topleft=(x,y))
					surfGameLight.blit(img1,img1_rect)
					x+=STEP
				elif maps[i][j]=='2':
					img2 = pygame.image.load(dictEnv[2])
					img2_rect = img2.get_rect(topleft = (x,y))
					surfGameLight.blit(img2,img2_rect)
					x+=STEP
				elif maps[i][j]=='3':
					img2 = pygame.image.load(dictEnv[3])
					img2_rect = img2.get_rect(topleft = (x,y))
					surfGameLight.blit(img2,img2_rect)
					x+=STEP
				elif maps[i][j]=='4':
					img2 = pygame.image.load(dictEnv[4])
					img2_rect = img2.get_rect(topleft = (x,y))
					surfGameLight.blit(img2,img2_rect)
					x+=STEP
		x=0
		y+=STEP
	sc.blit(surfGameLight,(STEP*2,STEP*2))
	
	
	hp=[]
	if player['hp'] == 6: 
		hp=[2,2,2]
	elif player['hp'] == 5: 
		hp=[2,2,1]
	elif player['hp'] == 4: 
		hp=[2,2,0]
	elif player['hp'] == 3: 
		hp=[2,1,0]
	elif player['hp'] == 2:
		hp=[2,0,0]
	elif player['hp'] == 1: 
		hp=[1,0,0]
	elif player['hp'] == 0: 
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

def renderInv(inv,sc):
	x = 0
	y = 0
	for i in range(0,len(inv)):
		for j in range(0,len(inv[i])):
			if inv[i][j]=='0':
				img0 = pygame.image.load('srcBMP/inv/border.bmp')
				img0_rect = img0.get_rect(topleft=(x,y))
				surfInv.blit(img0,img0_rect)
				x+=STEP
			elif inv[i][j]=='1':
				img1 = pygame.image.load('srcBMP/inv/empty.bmp')
				img1_rect = img1.get_rect(topleft=(x,y))
				surfInv.blit(img1,img1_rect)
				x+=STEP
			elif inv[i][j]=='2':
				img2 = pygame.image.load('srcBMP/inv/torch.bmp')
				img2_rect = img2.get_rect(topleft=(x,y))
				surfInv.blit(img2,img2_rect)
				x+=STEP
			elif inv[i][j]=='3':
				img3 = pygame.image.load('srcBMP/inv/potion.bmp')
				img3_rect = img3.get_rect(topleft=(x,y))
				surfInv.blit(img3,img3_rect)
				x+=STEP
			elif inv[i][j]=='4':
				img4 = pygame.image.load('srcBMP/inv/selector.bmp')
				img4_rect = img4.get_rect(topleft=(x,y))
				surfInv.blit(img4,img4_rect)
				x+=STEP
		x = 0
		y += STEP
	sc.blit(surfInv,(GAME_HEIGHT,0))

def renderList(dx,dy,level,tmp,player):
	x=0
	y=0
	for i in range(0,len(tmp)):
		for j in range(0,len(tmp[i])):
			if (tmp[i][j]=='2'):
				x=i
				y=j
				break

	if tmp[x+dx][y+dy] == '1' or tmp[x+dx][y+dy] == '4' :
		pass
	elif tmp[x+dx][y+dy] == '3':
		player['level']+=1
		tmp=loadMap(player['level'])
	else:
		tmp[x][y]='0'
		tmp[x+dx][y+dy]='2'
		player['i'] = x+dx
		player['j'] = y+dy

	return tmp
