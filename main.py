# здесь подключаются модули
import pygame
import os
from renderGame import *
# здесь определяются константы, классы и функции
FPS = 60
STEP = 64
player = dict()
WINDOW_HEIGHT = 1024
WINDOW_WEIGHT = 800

GAME_HEIGHT = 576
GAME_WEIGHT = 576

INV_HEIGHT = WINDOW_HEIGHT - GAME_HEIGHT
INV_WEIGHT = GAME_WEIGHT


# здесь происходит инициация, создание объектов и др.
pygame.init()
sc = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WEIGHT))
sc.fill((0,0,0))

surfGameDark = pygame.Surface((GAME_HEIGHT,GAME_WEIGHT))

# sc.blit(surfGameDark,(0,0))

surfGameLight = pygame.Surface((GAME_HEIGHT-4*STEP,GAME_HEIGHT-4*STEP))

surfInv = pygame.Surface((INV_HEIGHT,INV_WEIGHT))
# sc.blit(surfInv,(GAME_HEIGHT,0))

clock = pygame.time.Clock()

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
	


def renderInv(inv):
	
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
				img2 = pygame.image.load('srcBMP/inv/candle.bmp')
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
		
def openInv():
	
	invcell = inv[1][1]
	inv[1][1] = '4'
	a = 1
	b = 1
	renderInv(inv)
	while True:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			elif i.type == pygame.KEYDOWN:
				if i.key == pygame.K_i:
					#surfGameDark.set_alpha(0)
					inv[a][b] = invcell
					renderInv(inv)
					invcell = '0'
					return
				elif i.key == pygame.K_e:
					invcell = '1'
				elif i.key == pygame.K_1:
					exit()
				if i.key == pygame.K_UP:
					invcell = moveInv(-1,0,inv,invcell)
					a -= 1
				elif i.key == pygame.K_RIGHT:
					invcell = moveInv(0,1,inv,invcell)
					b += 1
				elif i.key == pygame.K_DOWN:
					invcell = moveInv(1,0,inv,invcell)
					a += 1
				elif i.key == pygame.K_LEFT:
					invcell = moveInv(0,-1,inv,invcell)
					b -= 1
				else:
					print('ERROR KEY')
		renderInv(inv)
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

# если надо до цикла отобразить объекты на экране
level = 1
maps = loadMap(level)

inv = loadInv()
renderMap(maps,player,surfGameDark,surfGameLight,sc,STEP)
renderInv(inv)
pygame.display.update()
 
# главный цикл
while True:
	
    # задержка
	clock.tick(FPS)
	
    # цикл обработки событий
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
		elif i.type == pygame.KEYDOWN:
			if i.key == pygame.K_UP:
				tmp = maps
				maps = renderList(-1,0,level,tmp,player)
				renderMap(maps,player,surfGameDark,surfGameLight,sc,STEP)
			elif i.key == pygame.K_RIGHT:
				tmp = maps
				maps = renderList(0,1,level,tmp,player)
				renderMap(maps,player,surfGameDark,surfGameLight,sc,STEP)
			elif i.key == pygame.K_DOWN:
				tmp = maps
				maps = renderList(1,0,level,tmp,player)
				renderMap(maps,player,surfGameDark,surfGameLight,sc,STEP)
			elif i.key == pygame.K_LEFT:
				tmp = maps
				maps = renderList(0,-1,level,tmp,player)
				renderMap(maps,player,surfGameDark,surfGameLight,sc,STEP)
			elif i.key == pygame.K_i:
				openInv()
			else:
				print('ERROR KEY')

	# обновление экрана
	pygame.display.update()