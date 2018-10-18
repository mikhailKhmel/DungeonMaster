# здесь подключаются модули
import pygame
import logSystem
import random
from renderGameTest import *
from renderInv import *

# здесь определяются константы, классы и функции
FPS = 15
STEP = 64

player = {'level': 1, 'type': random.randint(1,4), 'i':0, 'j':0, 'hp':5, 'arm':0}

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
renderMap(maps,player,sc)
logSystem.scanLog(maps,player,sc)

inv = loadInv(player)
surfSelect.set_alpha(0)
renderInv(inv,surfSelect,0,0,sc)

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
				openInv(inv,maps,player,sc)
			else:
				print('ERROR KEY')

	renderMap(maps,player,sc)
	logSystem.scanLog(maps,player,sc)

	# обновление экрана
	pygame.display.update()