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

def loadInv(player):
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
	if player['type'] == 1:
		m[1][1] = 'd'
	elif player['type'] == 2:
		m[1][1] = 'f'
	elif player['type'] == 3:
		m[1][1] = 'e'
	elif player['type'] == 4:
		m[1][1] = 'g'
#	print(m)
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
			elif inv[i][j]=='a':
				imga = pygame.image.load('srcBMP/inv/invpotion.bmp')
				imga_rect = imga.get_rect(topleft=(x,y))
				surfInv.blit(imga,imga_rect)
				x+=STEP
			elif inv[i][j]=='d':
				imgd = pygame.image.load('srcBMP/inv/invsword.bmp')
				imgd_rect = imgd.get_rect(topleft=(x,y))
				surfInv.blit(imgd,imgd_rect)
				x+=STEP
			elif inv[i][j]=='e':
				imge = pygame.image.load('srcBMP/inv/invspear.bmp')
				imge_rect = imge.get_rect(topleft=(x,y))
				surfInv.blit(imge,imge_rect)
				x+=STEP
			elif inv[i][j]=='f':
				imgf = pygame.image.load('srcBMP/inv/invbow.bmp')
				imgf_rect = imgf.get_rect(topleft=(x,y))
				surfInv.blit(imgf,imgf_rect)
				x+=STEP
			elif inv[i][j]=='g':
				imgg = pygame.image.load('srcBMP/inv/invtorch.bmp')
				imgg_rect = imgg.get_rect(topleft=(x,y))
				surfInv.blit(imgg,imgg_rect)
				x+=STEP
			elif inv[i][j]=='h':
				imgh = pygame.image.load('srcBMP/inv/invarmour0.bmp')
				imgh_rect = imgh.get_rect(topleft=(x,y))
				surfInv.blit(imgh,imgh_rect)
				x+=STEP
			elif inv[i][j]=='i':
				imgi = pygame.image.load('srcBMP/inv/invarmour1.bmp')
				imgi_rect = imgi.get_rect(topleft=(x,y))
				surfInv.blit(imgi,imgi_rect)
				x+=STEP
			elif inv[i][j]=='j':
				imgj = pygame.image.load('srcBMP/inv/invarmour2.bmp')
				imgj_rect = imgj.get_rect(topleft=(x,y))
				surfInv.blit(imgj,imgj_rect)
				x+=STEP
			elif inv[i][j]=='k':
				imgk = pygame.image.load('srcBMP/inv/invarmour3.bmp')
				imgk_rect = imgk.get_rect(topleft=(x,y))
				surfInv.blit(imgk,imgk_rect)
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
				#	Использование зелья
					if inv[a][b] == 'a':
						player['hp'] +=2
						if player['hp'] > 6:
							player['hp'] = 6
						inv[a][b] = '1'
				#	Замена экипировки
					elif inv[a][b] == 'd':
						inv[a][b] = inv[1][1]
						inv[1][1] = 'd'
						player['type'] = 1
					elif inv[a][b] == 'e':
						inv[a][b] = inv[1][1]
						inv[1][1] = 'e'
						player['type'] = 3
					elif inv[a][b] == 'f':
						inv[a][b] = inv[1][1]
						inv[1][1] = 'f'
						player['type'] = 2
					elif inv[a][b] == 'g':
						inv[a][b] = inv[1][1]
						inv[1][1] = 'g'
						player['type'] = 4
				#	Замена брони
					elif inv[a][b] == 'i':
						if player['arm'] < 1:
							inv[a][b] = inv[3][1]
							inv[3][1] = 'i'
							player['arm'] = 1
					elif inv[a][b] == 'j':
						if player['arm'] < 2:
							inv[a][b] = inv[3][1]
							inv[3][1] = 'j'
							player['arm'] = 2
					elif inv[a][b] == 'k':
						if player['arm'] < 3:
							inv[a][b] = inv[3][1]
							inv[3][1] = 'k'
							player['arm'] = 3
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