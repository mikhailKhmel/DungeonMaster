# здесь подключаются модули
import pygame
import logSystem
import random
from renderGameTest import *
from renderInv import *
from mob import *
import config
import menu
import emenu
from music import *

# здесь определяются константы, классы и функции
FPS = 10
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
mainMusic = 'music/main.ogg'
volume = config.PROCENT / 100
pygame.mixer.music.set_volume(volume)
openMusic(mainMusic)

def searchChests():
	x = config.player['i']
	y = config.player['j']
	if config.maps[x-1][y]=='4' or config.maps[x][y-1]=='4' or config.maps[x][y+1]=='4' or config.maps[x+1][y] == '4':
		logSystem.blitLog('game',[0],sc)
	else:
		logSystem.blitLog('game',[],sc)

def keyMove(dx,dy,sc):
	tmp = config.maps
	config.maps = renderList(dx,dy,level,tmp)
	tmp = config.maps
	config.maps = mobMovement(tmp,sc)
	searchChests()

def resetGame(sc):
	print('RESTART GAME\t',config.player)
	config.player = {'level': 1, 'type': 0, 'i':0, 'j':0, 'hp':6, 'arm':0, 'power':0.5}
	print('RESTART GAME\t',config.player)
	config.maps.clear()
	config.mobs.clear()
	config.inv.clear()
	config.maps = loadMap()				#config.dead - это флаг, по которому в menu.py выбирается задний фон
	config.inv = loadInv()
	config.mobs=scanMobs()
	
	surfSelect.set_alpha(0)
	renderInv(surfSelect,0,0,sc)
	refreshPlayer(config.player)
	renderHP(sc)					#отдельно вывел функцию в renderGameTest.py для отрисовки сердечек
	renderMap(config.maps,sc)
	searchChests()
	sc.fill((0,0,0))

	logSystem.blitLog('game',[],sc)

# если надо до цикла отобразить объекты на экране
menu.openMenu(punkt = 0)
sc.fill((0,0,0))

config.maps = loadMap()
config.mobs=scanMobs() #функция сканирования карты для поисков мобов и установки их первоначальных параметров
renderMap(config.maps,sc)

config.inv = loadInv()
surfSelect.set_alpha(0)
renderInv(surfSelect,0,0,sc)

logSystem.blitLog('game',[],sc)

pygame.display.update()
 
# главный цикл
while True:
	
    # задержка
	clock.tick(FPS)
	redM=False
	config.dead=False
    # цикл обработки событий
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
		elif i.type == pygame.KEYDOWN:
			print('player\t',config.player)
			if i.key == pygame.K_UP:
				keyMove(-1,0,sc)
			elif i.key == pygame.K_RIGHT:
				keyMove(0,1,sc)
			elif i.key == pygame.K_DOWN:
				keyMove(1,0,sc)
			elif i.key == pygame.K_LEFT:
				keyMove(0,-1,sc)
			elif i.key == pygame.K_SPACE:
				print('SPACE')
				redM=mobKiller(sc)
			elif i.key == pygame.K_i:
				openInv(config.maps,config.player, sc)
				searchChests()
			elif i.key == pygame.K_m:
				if config.music == True:
					pygame.mixer.music.pause()
					config.music = False
				elif config.music == False:
					pygame.mixer.music.unpause()
					config.music = True
			elif i.key == pygame.K_ESCAPE:
				emenu.openEmenu(punkt = 0)
				if config.dead==True:
					resetGame(sc)
				else:
					sc.fill((0,0,0))
					renderMap(config.maps,sc)
					surfSelect.set_alpha(0)
					renderInv(surfSelect,0,0,sc)
					logSystem.blitLog('game',[],sc)
			elif i.key == pygame.K_e:
				openChest(config.maps,sc)
			else:
				print('ERROR KEY')

			if config.player['hp'] <= 0:
				config.dead=True
				resetGame(sc)
				menu.openMenu(punkt = 0)
	
	if redM==False:
		renderMap(config.maps,sc)
	else:
		tmp = config.maps
		redMob(tmp,sc)
		
	renderInv(surfSelect,0,0,sc)
	renderHP(sc)
	# обновление экрана
	pygame.display.update()