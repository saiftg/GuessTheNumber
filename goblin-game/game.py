# Include pygane
# Init pygame
# Creat screen with particular size
# Crate game loop
# Add quit event
# Fill screen with color
# Repeat 6 over and over


import pygame
# we have to init to use pygame
#from math module get the fabs method
from math import fabs

pygame.init()

screen_size = (512, 480)
#screensize cant change
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load("background.png")
hero_img = pygame.image.load("hero.png")
goblin_img = pygame.image.load("goblin.png")
monster_img = pygame.image.load("lohan.jpg")

#heo location
hero = {
	'x' : 100,
	'y' : 100,
	'speed' : 20,
	'wins': 0
}


goblin = {
	'x': 200,
	'y': 200,
	'speed': 15
}

monster = {
	'x': 150,
	'y': 150,
	'speed': 10
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	'up': False,
	'down': False,
	'left': False,
	'right': False
}

#Creat a boolean for whehter the game should be going or not
game_on = True
while game_on:
	#we ar inside game loop, it will keep running as long as true
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			game_on = False
		elif (event.type == pygame.KEYDOWN):
			#print"Pressed a key!"
			if event.key == keys['up']:
				keys_down['up'] = True
				#hero['y'] -= hero['speed']
			elif event.key == keys['down']:
				keys_down['down'] = True
					
				#hero['y'] += hero['speed']
			elif event.key == keys['left']:
				keys_down['left'] = True
				#hero['x'] -= hero['speed']
			elif event.key == keys['right']:
				keys_down['right'] = True
				#hero['x'] += hero['speed']
		elif (event.type == pygame.KEYUP):
			if event.key == keys['up']:
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
			if event.key == keys['right']:
				keys_down['right'] = False

	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']


	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if distance_between < 32:
		print "Collsion!"
	else:
		print "No touching"

	#blit takes 2 arguments. What do u want to draw
	#wherer do u want to draw
	pygame_screen.blit(background_image, [0,0])

	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(hero_img, [hero['x'], hero['y']])

	pygame_screen.blit(goblin_img, [goblin['x'], goblin['y']])
	pygame_screen.blit(monster_img, [monster['x'], monster['y']])
	pygame.display.flip()













