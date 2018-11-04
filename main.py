# здесь подключаются модули
import pygame
import logSystem
import random
from renderGameTest import *
from renderInv import *
from mob import *
from config import *
from menu import *
from music import *

# здесь определяются константы, классы и функции
FPS = 20
STEP = 64
PROC = 100

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

# Настройка звука
mainMusic = 'music/main.mp3'
openMusic(mainMusic)

def searchChests():
	x = player['i']
	y = player['j']
	if maps[x-1][y-1]=='4' or maps[x-1][y]=='4' or maps[x][y-1]=='4' or maps[x+1][y+1]=='4' or maps[x][y+1]=='4' or maps[x+1][y] == '4' or maps[x+1][y-1] == '4' or maps[x-1][y+1]=='4':
		logSystem.blitLog('game',[0],sc)
	else:
		logSystem.blitLog('game',[],sc)
	

# если надо до цикла отобразить объекты на экране
menu = openMenu(punkt = 0)
sc.fill((0,0,0))

maps = loadMap()
renderMap(maps,sc)

inv = loadInv()
surfSelect.set_alpha(0)
renderInv(inv,surfSelect,0,0,sc)

logSystem.blitLog('game',[],sc)

pygame.display.update()
 
# главный цикл
while True:
	
    # задержка
	clock.tick(FPS)
	redM=False
    # цикл обработки событий
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
		elif i.type == pygame.KEYDOWN:
			if i.key == pygame.K_UP:
				tmp = maps
				maps = renderList(-1,0,level,tmp)
				tmp = maps
				maps = mobMovement(tmp)
				print(player['hp'])
				searchChests()
			elif i.key == pygame.K_RIGHT:
				tmp = maps
				maps = renderList(0,1,level,tmp)
				tmp = maps
				maps = mobMovement(tmp)
				print(player['hp'])
				searchChests()
			elif i.key == pygame.K_DOWN:
				tmp = maps
				maps = renderList(1,0,level,tmp)
				tmp = maps
				maps = mobMovement(tmp)
				print(player['hp'])
				searchChests()
			elif i.key == pygame.K_LEFT:
				tmp = maps
				maps = renderList(0,-1,level,tmp)
				tmp = maps
				maps = mobMovement(tmp)
				print(player['hp'])
				searchChests()
			elif i.key == pygame.K_SPACE:
				redM=True
				tmp = maps
				maps = mobKiller(tmp)
			elif i.key == pygame.K_i:
				openInv(inv,maps,player, sc)
				searchChests()
			elif i.key == pygame.K_ESCAPE:
				openMenu(punkt = 0)
				sc.fill((0,0,0))
				renderMap(maps,sc)
				surfSelect.set_alpha(0)
				renderInv(inv,surfSelect,0,0,sc)

			elif i.key == pygame.K_e:
				openChest(inv,maps,sc)
			else:
				print('ERROR KEY')
			#searchChests()
	if redM==False:
		renderMap(maps,sc)
	else:
		tmp = maps
		redMob(redM,tmp,sc)

	renderInv(inv,surfSelect,0,0,sc)
	
	# обновление экрана
	pygame.display.update()