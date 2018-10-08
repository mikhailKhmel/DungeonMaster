import pygame
from renderGameTest import *

STEP = 64

WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

INV_HEIGHT = WINDOW_HEIGHT - GAME_HEIGHT
INV_WEIGHT = GAME_WEIGHT

surfInv = pygame.Surface((INV_HEIGHT,INV_WEIGHT))
surfSelect = pygame.Surface((STEP,STEP))

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

def renderInv(inv,surfSelect,a,b,sc):
	x = 0
	y = 0
	for i in range(0,len(inv)):
		for j in range(0,len(inv[i])):
			if inv[i][j]=='0':
				img0 = pygame.image.load('srcBMP/inv/invbg.bmp')
				img0_rect = img0.get_rect(topleft=(x,y))
				surfInv.blit(img0,img0_rect)
				x+=STEP
			elif inv[i][j]=='1':
				img1 = pygame.image.load('srcBMP/inv/invempty.bmp')
				img1_rect = img1.get_rect(topleft=(x,y))
				surfInv.blit(img1,img1_rect)
				x+=STEP
			elif inv[i][j]=='2':
				img2 = pygame.image.load('srcBMP/inv/statbg.bmp')
				img2_rect = img2.get_rect(topleft=(x,y))
				surfInv.blit(img2,img2_rect)
				x+=STEP
			elif inv[i][j]=='3':
				img3 = pygame.image.load('srcBMP/inv/invsword.bmp')
				img3_rect = img3.get_rect(topleft=(x,y))
				surfInv.blit(img3,img3_rect)
				x+=STEP
			elif inv[i][j]=='4':
				img4 = pygame.image.load('srcBMP/inv/invtorch.bmp')
				img4_rect = img4.get_rect(topleft=(x,y))
				surfInv.blit(img4,img4_rect)
				x+=STEP
			elif inv[i][j]=='5':
				img5 = pygame.image.load('srcBMP/inv/invpotion.bmp')
				img5_rect = img5.get_rect(topleft=(x,y))
				surfInv.blit(img5,img5_rect)
				x+=STEP
		x = 0
		y += STEP
	imgS = pygame.image.load('srcBMP/inv/invsel.bmp')
	imgS_rect = imgS.get_rect(topleft=(a*STEP,b*STEP))
	surfSelect.blit(imgS,imgS_rect)
	surfInv.blit(surfSelect,(b*STEP,a*STEP))
	sc.blit(surfInv,(GAME_HEIGHT,0))

def openInv(inv,maps,player,randPlitka,sc):
	a = 5
	b = 1
	surfSelect.set_alpha(127)
	renderInv(inv,surfSelect,a,b,sc)
	while True:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			elif i.type == pygame.KEYDOWN:
				if i.key == pygame.K_i:
					surfSelect.set_alpha(0)
					renderInv(inv,surfSelect,a,b,sc)
					return
				elif i.key == pygame.K_e:
					if inv[a][b] == '5':
						player['hp'] +=2
						if player['hp'] > 6:
							player['hp'] = 6
						inv[a][b] = '1'
				elif i.key == pygame.K_q:
					inv[a][b] = '1'
				elif i.key == pygame.K_UP:
					a -= 1
					if a < 5:
						a = 5
				elif i.key == pygame.K_RIGHT:
					b += 1
					if b > 5:
						b = 5
				elif i.key == pygame.K_DOWN:
					a += 1
					if a > 7:
						a = 7
				elif i.key == pygame.K_LEFT:
					b -= 1
					if b < 1:
						b = 1
				else:
					print('ERROR KEY')
		renderInv(inv,surfSelect,a,b,sc)
		renderMap(maps,player,randPlitka,sc)
		pygame.display.update()