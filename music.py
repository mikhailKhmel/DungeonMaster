import pygame
import config

pygame.mixer.init()
clock = pygame.time.Clock()

def openMusic(file):
	pygame.mixer.music.load(file)
	pygame.mixer.music.play(-1, 0.0)

def openSound(audio):
	if config.music == True:
		audio.play()
