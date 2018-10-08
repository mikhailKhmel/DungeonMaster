import pygame

STEP = 64

WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

INV_HEIGHT = WINDOW_HEIGHT - GAME_HEIGHT
INV_WEIGHT = GAME_WEIGHT

surfInv = pygame.Surface((INV_HEIGHT,INV_WEIGHT))

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