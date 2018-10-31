import pygame
import sys
from music import *
import config

window = pygame.display.set_mode((1024, 800))
pygame.display.set_caption('DungeonMaster')
screen = pygame.Surface((1024, 800))



def openMenu(punkt):
	punkts = [(500, 400, u'Play', (11, 0, 77), (250,250,30), 0),
			  (500, 440, u'Sound ' + str(config.PROCENT) +'%', (11, 0, 77), (250, 250, 30), 1),
			  (500, 480, u'Exit', (11, 0, 77), (250,250,30), 2)]
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
		pygame.mouse.set_visible(True)
		while done:
			screen.fill((0, 100, 200))
			mp = pygame.mouse.get_pos()
			for i in self.punkts:
				if mp[0]>i[0] and mp[0]<i[0] and mp[1]>i[1] and mp[1]<i[1]+50:
					punkt =i[5]
			self.render(screen, font_menu, punkt)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					sys.exit()
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_ESCAPE:
					 sys.exit()
					if e.key == pygame.K_UP:
						if punkt > 0:
							punkt -= 1
					if e.key == pygame.K_DOWN:
						if punkt < len(self.punkts)-1:
							punkt += 1
					if e.key == pygame.K_SPACE:
						if punkt == 0:
							done = False
						elif punkt == 2:
								exit()
					if e.key == pygame.K_LEFT:
						if punkt == 1:
							if config.PROCENT > 10:
								config.PROCENT -=10
								volume = config.PROCENT / 100
								pygame.mixer.music.set_volume(volume)
								openMenu(punkt)
								done = False
					if e.key == pygame.K_RIGHT:
						if punkt == 1:
							if config.PROCENT < 100:
								config.PROCENT +=10
								volume = config.PROCENT / 100
								pygame.mixer.music.set_volume(volume)
								openMenu(punkt)
								done = False
				if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
					if punkt == 0:
						done = False
					elif punkt == 2:
						exit()
			window.blit(screen, (0, 0))
			pygame.display.update()
