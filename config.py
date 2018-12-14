import random

#здесь хранятся глобальные переменные
MENU = random.randint(1,4)
music = True
PROCENT = 110
amount = 0
player = {'level': 1, 'type': 0, 'i':0, 'j':0, 'hp':6, 'arm':0, 'power':0.5} #конфигурация игрока
inv = []
maps = []
mobs = [] #конфигурации мобов
dead = False

#словарь текстур
dictEnv = {	0: 'srcBMP/env',
				1: 'srcBMP/env',
				2: 'srcBMP/player/player0'+str(player['type'])+'.bmp',
				3: 'srcBMP/env/light/ladder.bmp',
				4: 'srcBMP/env/light/chest.bmp',
				5: 'srcBMP/env/light/mob'+str(random.randint(1,4))+'.bmp',
				10: 'srcBMP/env/light/emptychest.bmp'
			}

