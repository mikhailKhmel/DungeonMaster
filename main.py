# здесь подключаются модули
import pygame
import logSystem
import random
from renderGameTest import *
from renderInv import *

# здесь определяются константы, классы и функции
FPS = 60
STEP = 64

player = {'level': 1, 'type': random.randint(1,4), 'i':0, 'j':0, 'hp':5}

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

# если надо до цикла отобразить объекты на экране

maps = loadMap(player['level'])
randPlitka = []
for i in range(0,len(maps)):
	for j in range(0,len(maps[i])):
		if maps[i][j] == '0':
			typeOfPlitka = random.randint(1,3)
			randPlitka.append(typeOfPlitka)

print('plitka=',randPlitka)
renderMap(maps,player,randPlitka,sc)
logSystem.scanLog(maps,player,sc)

inv = loadInv()
renderInv(inv,sc)

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
			elif i.key == pygame.K_RIGHT:
				tmp = maps
				maps = renderList(0,1,level,tmp,player)
			elif i.key == pygame.K_DOWN:
				tmp = maps
				maps = renderList(1,0,level,tmp,player)
			elif i.key == pygame.K_LEFT:
				tmp = maps
				maps = renderList(0,-1,level,tmp,player)
			elif i.key == pygame.K_i:
				openInv(inv,sc)
			else:
				print('ERROR KEY')

	renderMap(maps,player,randPlitka,sc)
	logSystem.scanLog(maps,player,sc)

	# обновление экрана
	pygame.display.update()