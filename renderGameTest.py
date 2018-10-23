import pygame
import random

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


def renderMap(maps,player,sc):
	dictEnv = {	0: 'srcBMP/env',
				1: 'srcBMP/env',
				2: 'srcBMP/player/'+str(player['type'])+'.bmp',
				3: 'srcBMP/env/light/ladder.bmp',
				4: 'srcBMP/env/light/chest.bmp',
				5: 'srcBMP/env/light/mob.png'
			}
			
	for i in range(0,len(maps)):
		for j in range(0,len(maps[i])):
			if maps[i][j] == '2':
				player['i'] = i
				player['j'] = j


	startIdark = player['i'] - 4
	startJdark = player['j'] - 4
	endIdark = startIdark + 10
	endJdark = startJdark + 10

	x=0
	y=0
	for i in range(startIdark,endIdark):
		for j in range(startJdark,endJdark):
			if maps[i][j]=='0':
				img=pygame.image.load(dictEnv[0]+'/dark/plitka1.bmp')
				img_rect=img.get_rect(topleft=(x,y))
				surfGameDark.blit(img,img_rect)
			elif maps[i][j]=='1':
				img=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
				img_rect=img.get_rect(topleft=(x,y))
				surfGameDark.blit(img,img_rect)
			x+=STEP
		x=0
		y+=STEP
	sc.blit(surfGameDark,(0,0))

	startIlight = player['i'] - 2
	startJlight = player['j'] - 2
	endIlight = startIlight + 5
	endJlight = startJlight + 5
	# lightZone = []
	# tmp=[]
	# for i in range(startIlight,endIlight):
	# 	for j in range(startJlight,endJlight):
	# 		tmp.append(maps[i][j])
	# 	lightZone.append(tmp)
	# 	tmp=[]
	# print(lightZone)
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
						if maps[i][j]=='1':
							img=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						else:
							img=pygame.image.load(dictEnv[0]+'/dark/plitka1.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
					else:
						if maps[i][j]=='0':
							img=pygame.image.load(dictEnv[0]+'/light/plitka1.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='1':
							img=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='2':
							img=pygame.image.load(dictEnv[2])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='3':
							img=pygame.image.load(dictEnv[3])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='4':
							img=pygame.image.load(dictEnv[4])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='5':
							img=pygame.image.load(dictEnv[4])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='5':
							img=pygame.image.load(dictEnv[5])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)	
				if c in sector2:
					if maps[i][j+1]=='1':
						if maps[i][j]=='1':
							img=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						else:
							img=pygame.image.load(dictEnv[0]+'/dark/plitka1.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
					else:
						if maps[i][j]=='0':
							img=pygame.image.load(dictEnv[0]+'/light/plitka1.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='1':
							img=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='2':
							img=pygame.image.load(dictEnv[2])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='3':
							img=pygame.image.load(dictEnv[3])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='4':
							img=pygame.image.load(dictEnv[4])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='5':
							img=pygame.image.load(dictEnv[4])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='5':
							img=pygame.image.load(dictEnv[5])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)		
				if c in sector3:
					if maps[i][j-1]=='1':
							if maps[i][j]=='1':
								img=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							else:
								img=pygame.image.load(dictEnv[0]+'/dark/plitka1.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
					else:
						if maps[i][j]=='0':
							img=pygame.image.load(dictEnv[0]+'/light/plitka1.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='1':
							img=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='2':
							img=pygame.image.load(dictEnv[2])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='3':
							img=pygame.image.load(dictEnv[3])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='4':
							img=pygame.image.load(dictEnv[4])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='5':
							img=pygame.image.load(dictEnv[5])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)	
				if c in sector4:
					if maps[i-1][j]=='1':
						if maps[i][j]=='1':
							img=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						else:
							img=pygame.image.load(dictEnv[0]+'/dark/plitka1.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
					else:
						if maps[i][j]=='0':
							img=pygame.image.load(dictEnv[0]+'/light/plitka1.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='1':
							img=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='2':
							img=pygame.image.load(dictEnv[2])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='3':
							img=pygame.image.load(dictEnv[3])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='4':
							img=pygame.image.load(dictEnv[4])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
						elif maps[i][j]=='5':
							img=pygame.image.load(dictEnv[5])
							img_rect=img.get_rect(topleft=(x,y))
							surfGameLight.blit(img,img_rect)
				if c in sector5:
					if c==0:
						if maps[i+1][j+1]=='1':
							if maps[i][j]=='1':
								img=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							else:
								img=pygame.image.load(dictEnv[0]+'/dark/plitka1.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
						else:
							if maps[i][j]=='0':
								img=pygame.image.load(dictEnv[0]+'/light/plitka1.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='1':
								img=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='2':
								img=pygame.image.load(dictEnv[2])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='3':
								img=pygame.image.load(dictEnv[3])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='4':
								img=pygame.image.load(dictEnv[4])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='5':
								img=pygame.image.load(dictEnv[5])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
					if c==4:
						if maps[i+1][j-1]=='1':
							if maps[i][j]=='1':
								img=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							else:
								img=pygame.image.load(dictEnv[0]+'/dark/plitka1.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
						else:
							if maps[i][j]=='0':
								img=pygame.image.load(dictEnv[0]+'/light/plitka1.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='1':
								img=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='2':
								img=pygame.image.load(dictEnv[2])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='3':
								img=pygame.image.load(dictEnv[3])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='4':
								img=pygame.image.load(dictEnv[4])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='5':
								img=pygame.image.load(dictEnv[5])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
					if c==20:
						if maps[i-1][j+1]=='1':
							if maps[i][j]=='1':
								img=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							else:
								img=pygame.image.load(dictEnv[0]+'/dark/plitka1.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
						else:
							if maps[i][j]=='0':
								img=pygame.image.load(dictEnv[0]+'/light/plitka1.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='1':
								img=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='2':
								img=pygame.image.load(dictEnv[2])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='3':
								img=pygame.image.load(dictEnv[3])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='4':
								img=pygame.image.load(dictEnv[4])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='5':
								img=pygame.image.load(dictEnv[5])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)	
					if c==24:
						if maps[i-1][j-1]=='1':
							if maps[i][j]=='1':
								img=pygame.image.load(dictEnv[1]+'/dark/tipo_stena.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							else:
								img=pygame.image.load(dictEnv[0]+'/dark/plitka1.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
						else:
							if maps[i][j]=='0':
								img=pygame.image.load(dictEnv[0]+'/light/plitka1.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='1':
								img=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='2':
								img=pygame.image.load(dictEnv[2])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='3':
								img=pygame.image.load(dictEnv[3])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='4':
								img=pygame.image.load(dictEnv[4])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)
							elif maps[i][j]=='5':
								img=pygame.image.load(dictEnv[5])
								img_rect=img.get_rect(topleft=(x,y))
								surfGameLight.blit(img,img_rect)	
			else:
				if maps[i][j]=='0':
					img=pygame.image.load(dictEnv[0]+'/light/plitka1.bmp')
					img_rect=img.get_rect(topleft=(x,y))
					surfGameLight.blit(img,img_rect)
				elif maps[i][j]=='1':
					img=pygame.image.load(dictEnv[1]+'/light/tipo_stena.bmp')
					img_rect=img.get_rect(topleft=(x,y))
					surfGameLight.blit(img,img_rect)
				elif maps[i][j]=='2':
					img=pygame.image.load(dictEnv[2])
					img_rect=img.get_rect(topleft=(x,y))
					surfGameLight.blit(img,img_rect)
				elif maps[i][j]=='3':
					img=pygame.image.load(dictEnv[3])
					img_rect=img.get_rect(topleft=(x,y))
					surfGameLight.blit(img,img_rect)
				elif maps[i][j]=='4':
					img=pygame.image.load(dictEnv[4])
					img_rect=img.get_rect(topleft=(x,y))
					surfGameLight.blit(img,img_rect)
				elif maps[i][j]=='5':
					img=pygame.image.load(dictEnv[5])
					img_rect=img.get_rect(topleft=(x,y))
					surfGameLight.blit(img,img_rect)	
				
				
			c+=1
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
	elif tmp[x+dx][y+dy] == '5':
		pass
	else:
		tmp[x][y]='0'
		tmp[x+dx][y+dy]='2'
		player['i'] = x+dx
		player['j'] = y+dy

	return tmp