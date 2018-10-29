import random

#здесь хранятся глобальные переменные

amount = 0
player = {'level': 1, 'type': 0, 'i':0, 'j':0, 'hp':6, 'arm':0, 'power':0} #конфигурация игрока
enemy = {'lvl':1,'i':0, 'j':0, 'hp':2} #конфигурация мобов

#словарь текстур
dictEnv = {	0: 'srcBMP/env',
				1: 'srcBMP/env',
				2: 'srcBMP/player/player0'+str(player['type'])+'.bmp',
				3: 'srcBMP/env/light/ladder.bmp',
				4: 'srcBMP/env/light/chest.bmp',
				5: 'srcBMP/env/light/mob'+str(random.randint(1,4))+'.bmp'
			}

