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
surfInvlog = pygame.Surface((3*STEP, 3*STEP))
surfInvitm = pygame.Surface((5*STEP, 3*STEP))

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
#	print(m)
	return m

def renderInv(surfSelect,a,b,sc):
	x = 0
	y = 0
	for i in range(0,len(config.inv)):
		for j in range(0,len(config.inv[i])):
			if config.inv[i][j]=='0':
				img = pygame.image.load('srcBMP/inv/invempty.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInvitm.blit(img,img_rect)
				x+=STEP
			elif config.inv[i][j]=='a':
				img = pygame.image.load('srcBMP/inv/invpotion.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInvitm.blit(img,img_rect)
				x+=STEP
			elif config.inv[i][j]=='d':
				img = pygame.image.load('srcBMP/inv/invsword.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInvitm.blit(img,img_rect)
				x+=STEP
			elif config.inv[i][j]=='e':
				img = pygame.image.load('srcBMP/inv/invspear.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInvitm.blit(img,img_rect)
				x+=STEP
			elif config.inv[i][j]=='i':
				img = pygame.image.load('srcBMP/inv/invarmour1.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInvitm.blit(img,img_rect)
				x+=STEP
			elif config.inv[i][j]=='j':
				img = pygame.image.load('srcBMP/inv/invarmour2.bmp')
				img_rect = img.get_rect(topleft=(x,y))
				surfInvitm.blit(img,img_rect)
				x+=STEP
		x = 0
		y += STEP
	surfSelect.fill((255, 0, 0))
	surfInvitm.blit(surfSelect,(b*STEP,a*STEP))
	surfInvlog.fill((78, 78, 78))
	x = 5
	invlogmsg = ['Уровень брони: '+str(config.player['arm']), 'Сила: '+str(config.player['power'])]
	for s in invlogmsg:
		font = pygame.font.SysFont('verdana',20)
		text = font.render(s, 1, (255,255,255))
		surfInvlog.blit(text,(5,x))
		x+=20
	img = pygame.image.load('srcBMP/inv/invbg.bmp')
	img_rect = img.get_rect(topleft=(0,0))
	surfInv.blit(img,img_rect)
	surfInv.blit(surfInvlog, (3*STEP, STEP))
	surfInv.blit(surfInvitm, (1*STEP, 5*STEP))
	if config.player['type'] == 0:
		img = pygame.image.load('srcBMP/inv/invempty.bmp')
		surfInv.blit(img, (STEP, STEP))
	elif config.player['type'] == 1:
		img = pygame.image.load('srcBMP/inv/invsword.bmp')
		surfInv.blit(img, (STEP, STEP))
	elif config.player['type'] == 2:
		img = pygame.image.load('srcBMP/inv/invspear.bmp')
		surfInv.blit(img, (STEP, STEP))
	if config.player['arm'] == 0:
		img = pygame.image.load('srcBMP/inv/invempty.bmp')
		surfInv.blit(img, (STEP, 3*STEP))
	elif config.player['arm'] == 1:
		img = pygame.image.load('srcBMP/inv/invarmour1.bmp')
		surfInv.blit(img, (STEP, 3*STEP))
	elif config.player['arm'] == 2:
		img = pygame.image.load('srcBMP/inv/invarmour2.bmp')
		surfInv.blit(img, (STEP, 3*STEP))
	sc.blit(surfInv,(GAME_HEIGHT,0))

def openInv(maps,player,sc):
	logSystem.blitLog('inv',[],sc)
	a = 0
	b = 0
	surfSelect.set_alpha(127)
	renderInv(surfSelect,a,b,sc)
	while True:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			elif i.type == pygame.KEYDOWN:
				if i.key == pygame.K_i:
					surfSelect.set_alpha(0)
					renderInv(surfSelect,a,b,sc)
					return
				elif i.key == pygame.K_e:
					#Использование зелья
					if config.inv[a][b] == 'a':
						volume = config.PROCENT / 100
						glotok.set_volume(volume)
						openSound(glotok)
						player['hp'] +=2
						if player['hp'] > 6:
							player['hp'] = 6
						config.inv[a][b] = '0'
						renderHP(sc)
					#Замена экипировки
					elif config.inv[a][b] == 'd':
						if player['type'] == 0:
							config.inv[a][b] = '0'
						elif player['type'] == 1:
							config.inv[a][b] = 'd'
						elif player['type'] == 2:
							config.inv[a][b] = 'e'
						player['type'] = 1
						player['power'] = 2
						refreshPlayer(player)
					elif config.inv[a][b] == 'e':
						if player['type'] == 0:
							config.inv[a][b] = '0'
						elif player['type'] == 1:
							config.inv[a][b] = 'd'
						elif player['type'] == 2:
							config.inv[a][b] = 'e'
						player['type'] = 2
						player['power'] = 1
						refreshPlayer(player)
					#Замена брони
					elif config.inv[a][b] == 'i':
						if player['arm'] < 1:
							if player['arm'] == 0:
								config.inv[a][b] = '0'
							elif player['arm'] == 1:
								config.inv[a][b] = 'i'
							elif player['arm'] == 2:
								config.inv[a][b] = 'j'
							player['arm'] = 1
							refreshPlayer(player)
						else:
							logSystem.blitLog('inv',[0],sc)
					elif config.inv[a][b] == 'j':
						if player['arm'] < 2:
							if player['arm'] == 0:
								config.inv[a][b] = '0'
							elif player['arm'] == 1:
								config.inv[a][b] = 'i'
							elif player['arm'] == 2:
								config.inv[a][b] = 'j'
							player['arm'] = 2
							refreshPlayer(player)
				#Деекипировка
				elif i.key == pygame.K_r:
					if config.inv[a][b] == '0':
						if player['type'] == 0:
							config.inv[a][b] = '0'
						elif player['type'] == 1:
							config.inv[a][b] = 'd'
						elif player['type'] == 2:
							config.inv[a][b] = 'e'
						player['type'] = 0
						player['power'] = 0.5
						refreshPlayer(player)
				#Уничтожение вещи
				elif i.key == pygame.K_q:
					if config.inv[a][b] != '0':
						volume = config.PROCENT / 100
						brosok.set_volume(volume)
						openSound(brosok)
						config.inv[a][b] = '0'
				elif i.key == pygame.K_UP:
					a -= 1
					if a < 0:
						a = 0
				elif i.key == pygame.K_RIGHT:	
					b += 1
					if b > 4:
						b = 4
				elif i.key == pygame.K_DOWN:
					a += 1
					if a > 2:
						a = 2
				elif i.key == pygame.K_LEFT:
					b -= 1
					if b < 0:
						b = 0
				else:
					print('ERROR KEY')
		renderInv(surfSelect,a,b,sc)
		renderMap(maps,sc)
		pygame.display.update()
		
def refreshPlayer(player):
	dictEnv[2] = 'srcBMP/player/player'+str(player['arm'])+str(player['type'])+'.bmp'
	
def openChest(maps,sc):
	x = config.player['i']
	y = config.player['j']
	if maps[x-1][y]=='4' or maps[x][y-1]=='4' or maps[x][y+1]=='4' or maps[x+1][y] == '4':
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if maps[i][j]=='4':
					for a in range(0, len(config.inv)):
						for b in range(0, len(config.inv[a])):
							if config.inv[a][b] == '0':
								addItem(config.inv,a,b,sc)
								maps[i][j] = 'a'
								return
					print('You are overencumbered')
					logSystem.blitLog('game',[1],sc)
					return
	else:
		print('No chest nearby')
	
def addItem(inv,x,y,sc):
	c=random.randint(1,10)
	if c<7:
		config.inv[x][y]='a'
		print('Potion added')
		logSystem.blitLog('game',[2],sc)
	elif c==7:
		config.inv[x][y]='d'
		print('Sword added')
		logSystem.blitLog('game',[3],sc)
	elif c==8:
		config.inv[x][y]='e'
		print('Spear & shield added')
		logSystem.blitLog('game',[4],sc)
	elif c==9:
		config.inv[x][y]='i'
		print('Leather armour added')
		logSystem.blitLog('game',[5],sc)
	elif c==10:
		config.inv[x][y]='j'
		print('Steel armour added')
		logSystem.blitLog('game',[6],sc)