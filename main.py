# здесь подключаются модули
import pygame
from renderGame import *
# здесь определяются константы, классы и функции
FPS = 60
STEP = 64
player = {'i':0,'j':0,'hp':3}
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
		x=0
		y+=STEP
	sc.blit(surfInv,(GAME_HEIGHT,0))
		
def openInv():
	
	inv[len(inv)-2][len(inv)] = inv[1][1]
	inv[1][1] = '4'
	renderInv(inv)
	while True:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			
			elif i.type == pygame.KEYDOWN:
				if i.key == pygame.K_i:
					#surfGameDark.set_alpha(0)
					return
				elif i.key == pygame.K_e:
					inv[len(inv)-2][len(inv)] = '1'
				elif i.key == pygame.K_1:
					exit()
				if i.key == pygame.K_UP:
					moveInv(-1,0,inv)
				elif i.key == pygame.K_RIGHT:
					moveInv(0,1,inv)
				elif i.key == pygame.K_DOWN:
					moveInv(1,0,inv)
				elif i.key == pygame.K_LEFT:
					moveInv(0,-1,inv)
				else:
					print('ERROR KEY')

		renderInv(inv)
		pygame.display.update()


def moveInv(dx,dy,inv):
	x=0
	y=0
	for i in range(0,len(inv)):
		for j in range(0,len(inv[i])):
			if (inv[i][j]=='4'):
				x=i
				y=j
				break
	if inv[x+dx][y+dy] == '0':
		pass
	else:
		inv[x][y] = inv[len(inv)-2][len(inv)]
		inv[len(inv)-2][len(inv)] = inv[x+dx][y+dy]
		inv[x+dx][y+dy] = '4'

# если надо до цикла отобразить объекты на экране

maps = loadMap(level)

inv = loadInv()
renderMap(maps,player,sc)
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
				renderMap(maps,player,sc)
			elif i.key == pygame.K_RIGHT:
				tmp = maps
				maps = renderList(0,1,level,tmp,player)
				renderMap(maps,player,sc)
			elif i.key == pygame.K_DOWN:
				tmp = maps
				maps = renderList(1,0,level,tmp,player)
				renderMap(maps,player,sc)
			elif i.key == pygame.K_LEFT:
				tmp = maps
				maps = renderList(0,-1,level,tmp,player)
				renderMap(maps,player,sc)
			elif i.key == pygame.K_i:
				openInv()
				#
			else:
				print('ERROR KEY')

	# обновление экрана
	pygame.display.update()