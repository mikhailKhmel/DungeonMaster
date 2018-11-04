import pygame, logSystem
from renderGameTest import *
from config import *
from music import *
import config

STEP = 64

WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

INV_HEIGHT = WINDOW_HEIGHT - GAME_HEIGHT
INV_WEIGHT = GAME_WEIGHT

surfInv = pygame.Surface((INV_HEIGHT,INV_WEIGHT))
surfSelect = pygame.Surface((STEP,STEP))

glotok = pygame.mixer.Sound('music/glotok.ogg')
brosok = pygame.mixer.Sound('music/brosok.ogg')

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
	if player['type'] == 1:
		m[1][1] = 'd'
	elif player['type'] == 2:
		m[1][1] = 'e'
#	print(m)
	return m

def renderInv(inv,surfSelect,a,b,sc):
	x = 0
	y = 0
	for i in range(0,len(inv)):
		for j in range(0,len(inv[i])):
			if inv[i][j]=='0':
				img = pygame.image.load('srcBMP/inv/invbg.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInv.blit(img,img_rect)
				x+=STEP
			elif inv[i][j]=='1':
				img = pygame.image.load('srcBMP/inv/invempty.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInv.blit(img,img_rect)
				x+=STEP
			elif inv[i][j]=='2':
				img = pygame.image.load('srcBMP/inv/statbg.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInv.blit(img,img_rect)
				x+=STEP
			elif inv[i][j]=='a':
				img = pygame.image.load('srcBMP/inv/invpotion.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInv.blit(img,img_rect)
				x+=STEP
			elif inv[i][j]=='d':
				img = pygame.image.load('srcBMP/inv/invsword.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInv.blit(img,img_rect)
				x+=STEP
			elif inv[i][j]=='e':
				img = pygame.image.load('srcBMP/inv/invspear.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInv.blit(img,img_rect)
				x+=STEP
			elif inv[i][j]=='h':
				img = pygame.image.load('srcBMP/inv/invarmour0.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInv.blit(img,img_rect)
				x+=STEP
			elif inv[i][j]=='i':
				img = pygame.image.load('srcBMP/inv/invarmour1.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInv.blit(img,img_rect)
				x+=STEP
			elif inv[i][j]=='j':
				img = pygame.image.load('srcBMP/inv/invarmour2.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInv.blit(img,img_rect)
				x+=STEP
		x = 0
		y += STEP
	img = pygame.image.load('srcBMP/inv/invsel.bmp')
	img_rect = img.get_rect(topleft=(a*STEP,b*STEP))
	surfSelect.blit(img,img_rect)
	surfInv.blit(surfSelect,(b*STEP,a*STEP))
	sc.blit(surfInv,(GAME_HEIGHT,0))

def openInv(inv,maps,player,sc):
	logSystem.blitLog('inv',[],sc)
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
					print(player['arm'],'-',player['type'])
					renderInv(inv,surfSelect,a,b,sc)
					return
				elif i.key == pygame.K_e:
					#Использование зелья
					if inv[a][b] == 'a':
						volume = config.PROCENT / 100
						glotok.set_volume(volume)
						openSound(glotok)
						player['hp'] +=2
						if player['hp'] > 6:
							player['hp'] = 6
						inv[a][b] = '1'
					#Замена экипировки
					elif inv[a][b] == 'd':
						inv[a][b] = inv[1][1]
						inv[1][1] = 'd'
						player['type'] = 1
						player['power'] = 1
						refreshPlayer(player)
					elif inv[a][b] == 'e':
						inv[a][b] = inv[1][1]
						inv[1][1] = 'e'
						player['type'] = 2
						player['power'] = 2
						refreshPlayer(player)
					#Замена брони
					elif inv[a][b] == 'i':
						if player['arm'] < 1:
							inv[a][b] = inv[3][1]
							inv[3][1] = 'i'
							player['arm'] = 1
							refreshPlayer(player)
						else:
							logSystem.blitLog('inv',[0],sc)
					elif inv[a][b] == 'j':
						if player['arm'] < 2:
							inv[a][b] = inv[3][1]
							inv[3][1] = 'j'
							player['arm'] = 2
							refreshPlayer(player)
				#Деекипировка
				elif i.key == pygame.K_r:
					if inv[a][b] == '1':
						inv[a][b] = inv[1][1]
						inv[1][1] = '1'
						player['type'] = 0
						player['power'] = 0
						refreshPlayer(player)
				#Уничтожение вещи
				elif i.key == pygame.K_q:
					if inv[a][b] != '1':
						volume = config.PROCENT / 100
						brosok.set_volume(volume)
						openSound(brosok)
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
		renderMap(maps,sc)
		pygame.display.update()
		
def refreshPlayer(player):
	dictEnv[2] = 'srcBMP/player/player'+str(player['arm'])+str(player['type'])+'.bmp'

def openChest(inv,maps,sc):
	x = player['i']
	y = player['j']
	if maps[x-1][y-1]=='4' or maps[x-1][y]=='4' or maps[x][y-1]=='4' or maps[x+1][y+1]=='4' or maps[x][y+1]=='4' or maps[x+1][y] == '4' or maps[x+1][y-1] == '4' or maps[x-1][y+1]=='4':
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if maps[i][j]=='4':
					for a in range(5, len(inv)):
						for b in range(0, len(inv[a])):
							if inv[a][b]=='1':
								addItem(inv,a,b,sc)
								maps[i][j]='a'
								return
					print('You are overencumbered')
					logSystem.blitLog('game',[1],sc)
					return
	else:
		print('No chest nearby')
	
def addItem(inv,x,y,sc):
	c=random.randint(1,10)
	if c<7:
		inv[x][y]='a'
		print('Potion added')
		logSystem.blitLog('game',[2],sc)
	elif c==7:
		inv[x][y]='d'
		print('Sword added')
		logSystem.blitLog('game',[3],sc)
	elif c==8:
		inv[x][y]='e'
		print('Spear & shield added')
		logSystem.blitLog('game',[4],sc)
	elif c==9:
		inv[x][y]='i'
		print('Leather armour added')
		logSystem.blitLog('game',[5],sc)
	elif c==10:
		inv[x][y]='j'
		print('Steel armour added')
		logSystem.blitLog('game',[6],sc)