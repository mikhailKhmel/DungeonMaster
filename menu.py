import pygame
import sys
import random
import config
from music import *


window = pygame.display.set_mode((1024, 800))
pygame.display.set_caption('DungeonMaster')
screen = pygame.Surface((1024, 800))
image_menu = ''


def openMenu(punkt):
	punkts = [(10, 630, u'Play', (255, 255, 255), (250,250,30), 0),
			  (10, 680, u'Sound ' + str(config.PROCENT) +'%', (255, 255, 255), (250, 250, 30), 1),
			  (10, 730, u'Exit', (255, 255, 255), (250,250,30), 2)]
	game = Menu(punkts)
	game.menu(punkt)

class Menu:
	def __init__(self, punkts = [400, 350, u'Punkt', (250,250,30), (250,30,250)]):
		self.punkts = punkts
	def render(self, poverhnost, font, num_punkt):
		for i in self.punkts:
			if num_punkt == i[5]:
				poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
			else:
				poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
	def menu(self, punkt):
		done = True
		font_menu = pygame.font.SysFont("arial", 50)
		pygame.key.set_repeat(0,0)
		#pygame.mouse.set_visible(True)
		if config.dead == False:
			image_menu = pygame.image.load('srcBMP/menu/'+str(config.MENU)+'.bmp')
		else:
			image_menu = pygame.image.load('srcBMP/menu/gameover.jpg')


		while done:
			screen.blit(image_menu,(0,0))
			mp = pygame.mouse.get_pos()
			for i in self.punkts:
				if mp[0]>i[0] and mp[0]<i[0] and mp[1]>i[1] and mp[1]<i[1]+50:
					punkt =i[5]
			self.render(screen, font_menu, punkt)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					sys.exit()
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_m:
						if config.music == True:
							pygame.mixer.music.pause()
							config.music = False
						elif config.music == False:
							pygame.mixer.music.unpause()
							config.music = True
					if e.key == pygame.K_ESCAPE:
					 sys.exit()
					if e.key == pygame.K_UP:
						if punkt > 0:
							punkt -= 1
					if e.key == pygame.K_DOWN:
						if punkt < len(self.punkts)-1:
							punkt += 1
					if e.key == pygame.K_RETURN:
						if punkt == 0:
							done = False
						elif punkt == 2:
								exit()
					if e.key == pygame.K_LEFT:
						if punkt == 1:
							if config.PROCENT > 0:
								config.PROCENT -=5
								volume = config.PROCENT / 100
								pygame.mixer.music.set_volume(volume)
								openMenu(punkt)
								done = False
					if e.key == pygame.K_RIGHT:
						if punkt == 1:
							if config.PROCENT < 100:
								config.PROCENT +=5
								volume = config.PROCENT / 100
								pygame.mixer.music.set_volume(volume)
								openMenu(punkt)
								done = False
			window.blit(screen, (0, 0))
			pygame.display.update()
