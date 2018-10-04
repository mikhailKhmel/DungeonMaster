import pygame

def loadMap(level):
	print('level=',level)
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

def renderMap(maps,player,surfGameDark,surfGameLight,sc,STEP):
	for i in range(0,len(maps)):
		for j in range(0,len(maps[i])):
			if maps[i][j] == '2':
				player['i'] = i
				player['j'] = j
	startI = player['i'] - 4
	startJ = player['j'] - 4
	x=0
	y=0
	for i in range(startI,startI+10):
		for j in range(startJ,startJ+10):
			if maps[i][j]=='0':
				img0=pygame.image.load('srcBMP/dark/ground.bmp')
				img0_rect=img0.get_rect(topleft=(x,y))
				surfGameDark.blit(img0,img0_rect)
				x+=STEP
			elif maps[i][j]=='1':
				img1=pygame.image.load('srcBMP/dark/wall.bmp')
				img1_rect=img1.get_rect(topleft=(x,y))
				surfGameDark.blit(img1,img1_rect)
				x+=STEP
			elif maps[i][j]=='2':
				img2 = pygame.image.load('srcBMP/dark/player.bmp')
				img2_rect = img2.get_rect(topleft = (x,y))
				surfGameDark.blit(img2,img2_rect)
				x+=STEP
			elif maps[i][j]=='3':
				img2 = pygame.image.load('srcBMP/dark/stairs.bmp')
				img2_rect = img2.get_rect(topleft = (x,y))
				surfGameDark.blit(img2,img2_rect)
				x+=STEP
		x=0
		y+=STEP
	# surfGameDark.set_alpha(25)
	# surfGameDark.convert_alpha()
	sc.blit(surfGameDark,(0,0))

	startI = player['i'] - 2
	startJ = player['j'] - 2
	x=0
	y=0
	for i in range(startI,startI+5):
		for j in range(startJ,startJ+5):
			if (i!=0 and j!=0) or (i!=0 and j!=startJ+4) or (i!=startI+4 and j!=0) or (i!=startI+4 and j!=startJ+4):
				if maps[i][j]=='0':
					img0=pygame.image.load('srcBMP/light/ground.bmp')
					img0_rect=img0.get_rect(topleft=(x,y))
					surfGameLight.blit(img0,img0_rect)
					x+=STEP
				elif maps[i][j]=='1':
					img1=pygame.image.load('srcBMP/light/wall.bmp')
					img1_rect=img1.get_rect(topleft=(x,y))
					surfGameLight.blit(img1,img1_rect)
					x+=STEP
				elif maps[i][j]=='2':
					img2 = pygame.image.load('srcBMP/light/player.bmp')
					img2_rect = img2.get_rect(topleft = (x,y))
					surfGameLight.blit(img2,img2_rect)
					x+=STEP
				elif maps[i][j]=='3':
					img2 = pygame.image.load('srcBMP/light/stairs.bmp')
					img2_rect = img2.get_rect(topleft = (x,y))
					surfGameLight.blit(img2,img2_rect)
					x+=STEP
		x=0
		y+=STEP
	sc.blit(surfGameLight,(STEP*2,STEP*2))


def renderList(dx,dy,level,tmp,player):
	x=0
	y=0
	for i in range(0,len(tmp)):
		for j in range(0,len(tmp[i])):
			if (tmp[i][j]=='2'):
				x=i
				y=j
				break

	if tmp[x+dx][y+dy] == '1':
		pass
	elif tmp[x+dx][y+dy] == '3':
		level = level + 1
		tmp=loadMap(level)
	else:
		tmp[x][y]='0'
		tmp[x+dx][y+dy]='2'
		player['i'] = x+dx
		player['j'] = y+dy

	return tmp