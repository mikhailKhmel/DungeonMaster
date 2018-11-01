import pygame

pygame.mixer.init()
clock = pygame.time.Clock()

def openMusic(file):
	pygame.mixer.music.load(file)
	pygame.mixer.music.play(-1, 0.0)

def openSound(audio):
	audio.play()
