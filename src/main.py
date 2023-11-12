#import pygame, sys, random, time from time and import all the stuff that is in pygame in the project 

import pygame
import sys
import random
from time import time
from time import sleep
from pygame.locals import *
from pygame import mixer

# initialize pygame
pygame.init()
# initialize mixer
mixer.init()

# create the display
screen  = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("Pillow Dodge")

# load the sounds
lostlife = pygame.mixer.Sound('sounds/lostlife.wav')
pickupcoin = pygame.mixer.Sound('sounds/pickupcoin.wav')

# make the main menu def

def main_menu():
    # load and play the background music for the main menu
	pygame.mixer.music.load("sounds/mainmenu.ogg") 
	pygame.mixer.music.play(-1,0.0)
    	
	clock = pygame.time.Clock()

	bgm_img = pygame.image.load('images/background.png').convert_alpha()
	playerm_img = pygame.image.load('images/dodger.png').convert_alpha()
	playerm_img = pygame.transform.scale(playerm_img, (96, 96))
	pillowm_img = pygame.image.load('images/pillow.png').convert_alpha()
	pillowm_img = pygame.transform.scale(pillowm_img, (106, 96))

	three_lines_img = pygame.image.load('images/threeLines.png').convert_alpha()
	three_lines_img = pygame.transform.scale(three_lines_img, (118, 118))

	screen  = pygame.display.set_mode((800, 600), 0, 32)
	pygame.display.set_caption('Pillow Dodge')

	while True:
		main_text_font = pygame.font.Font('fonts/Toon Around df.otf', 104)
		main_text = main_text_font.render('Pillow Dodge!', True, (0,0,0))
		small_text_font = pygame.font.Font('fonts/Toon Around df.otf', 64)
		press_to_start = small_text_font.render('Press Space to start!', True, (0, 0, 0))
		press_to_quit = small_text_font.render('Or press Q to quit', True, (0, 0, 0))
		version_font = pygame.font.Font('fonts/Toon Around df.otf', 36)
  
		version = version_font.render('Version 1.0.0', True, (0, 0, 0))


		screen.blit(bgm_img, (0, 0))
		screen.blit(pillowm_img, (450, 240))
		screen.blit(playerm_img,(170, 240))
		screen.blit(main_text,(155, 50))
		screen.blit(three_lines_img, (550, 230))
		screen.blit(press_to_start, (150, 410))
		screen.blit(press_to_quit, (200, 480))
		screen.blit(version, (630, 5))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.key == pygame.K_q:
					pygame.quit()
					sys.exit()
				if event.key == pygame.K_SPACE:
					pygame.mixer.music.stop()
					main()
				
		pygame.display.update()
		clock.tick(61)

# the main method where the game mechanism is implemented

def main():
	# load and play the background music for the main game
	pygame.mixer.music.load("sounds/maingame.wav") 
	pygame.mixer.music.play(-1)
 
	#varibles and stuff
	clock = pygame.time.Clock()
	playerX = 70
	playerY = 250
	pillowX = 850
	pillowY = 250
 
	coinX = 850
	coinY = 250
 
	pillow2X = 850
	pillow2Y = 250
 
	move = 2
	move_pillow = 2
	move_pillow2 = 3
	move_coin = random.randint(1, 3)
	pillow_move_speed = 15
	pillow2_move_speed = 10
	coin_move_speed = random.randint(9, 13)
	scoreX = 580
	hearts = 3

	# the varible of the score counter

	score = 0

	#colors
	r = (255, 0, 0)
	g = (0, 255, 0)
	b = (0, 0, 255)
	bl = (0, 0, 0)
	w = (255, 255, 255)

	# load images
	bg_img = pygame.image.load('images/background.png').convert_alpha()
	player_img = pygame.image.load('images/dodger.png').convert_alpha()
	player_img = pygame.transform.scale(player_img, (96, 96))
	pillow_img = pygame.image.load('images/pillow.png').convert_alpha()
	pillow_img = pygame.transform.scale(pillow_img, (106, 96))
	pillow2_img = pygame.image.load('images/pillow.png').convert_alpha()
	pillow2_img = pygame.transform.scale(pillow_img, (106, 96))
 
	threehearts_img = pygame.image.load('images/threehearts.png').convert_alpha()
	threehearts_img = pygame.transform.scale(threehearts_img, (230, 60))
 
	twohearts_img = pygame.image.load('images/twohearts.png').convert_alpha()
	twohearts_img = pygame.transform.scale(twohearts_img, (230, 60))

	oneheart_img = pygame.image.load('images/oneheart.png').convert_alpha()
	oneheart_img = pygame.transform.scale(oneheart_img, (230, 60))

	zerohearts_img = pygame.image.load('images/zerohearts.png').convert_alpha()
	zerohearts_img = pygame.transform.scale(zerohearts_img, (230, 60))
 
	coinimg = pygame.image.load('images/coin1.png').convert_alpha()
	coinimg = pygame.transform.scale(coinimg, (82, 82))

	# make the two pillows and the player a rect so that they can have collision detection
	player_rect = player_img.get_rect()
	pillow_rect = pillow_img.get_rect()
	pillow2_rect = pillow2_img.get_rect()
	coin_rect = coinimg.get_rect()

	# initialize the screen size and title
	screen  = pygame.display.set_mode((800, 600), 0, 32)
	pygame.display.set_caption('Pillow Dodge')

	def game_over():
			pygame.mixer.music.stop()
			pygame.mixer.music.load("sounds/gameovermusic.mp3") 
			pygame.mixer.music.play(-1,0.0)
			while True:
				clock = pygame.time.Clock()
				gameover_font = pygame.font.Font('fonts/Toon Around df.otf', 96)
				gameover_small_font = pygame.font.Font('fonts/Toon Around df.otf', 64)
				press_text_font = pygame.font.Font('fonts/Toon Around df.otf', 52)

				gameover_text = gameover_font.render('Game Over! :(', True, bl)

				gameover_small_text = gameover_small_font.render('Better Luck Next Time!', True, bl)
				press_text = press_text_font.render('Press R to restart', True, bl)
				presss_text2 = press_text_font.render('And press M to go to the main menu', True, bl) 
				screen.blit(gameover_text, (180, 80))
				screen.blit(gameover_small_text, (140, 180))
				screen.blit(press_text, (230, 350))
				screen.blit(presss_text2, (70, 400))
    
				# keyboard input

				keys = pygame.key.get_pressed()
				if keys[K_r]:
					pygame.mixer.music.stop()
					main()
				if keys[K_m]:
					main_menu()

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							pygame.quit()
							sys.exit()
				pygame.display.update()
				clock.tick(61)
    
	latest_hit_time = 0
	latest_hit_time2 = 0
 
	coin_delay = 0
 
	while True:
		player_rect.x = playerX
		player_rect.y = playerY

		pillow_rect.x = pillowX
		pillow_rect.y = pillowY
  
		pillow2_rect.x = pillow2X
		pillow2_rect.y = pillow2Y
  
		coin_rect.x = coinX
		coin_rect.y = coinY

		pillowX -= pillow_move_speed
  
		coinX -= coin_move_speed
  
		pillow2X -= pillow2_move_speed

		score_text_font = pygame.font.Font('fonts/Toon Around df.otf', 64)
		score_text = score_text_font.render('Score: ' + str(score), True, bl)

		screen.blit(bg_img, (0, 0))
		screen.blit(player_img, player_rect)
		screen.blit(pillow_img, (pillowX, pillowY))
		screen.blit(pillow2_img, (pillow2X, pillow2Y))
		screen.blit(score_text, (scoreX, 10))
		screen.blit(coinimg, (coinX, coinY))
  
		if hearts == 3:
			screen.blit(threehearts_img, (560, 530))
		if hearts == 2:
			screen.blit(twohearts_img, (560, 530))
		if hearts == 1:
			screen.blit(oneheart_img, (560, 530))

		# check if the score equals 10, 100, 1000, 10000 or 100000 and then move it back to have space to display the score text

		if score == 10 or score > 10:
			scoreX = 560
		if score == 100 or score > 100:
			scoreX = 530
		if score == 1000 or score > 1000:
			scoreX = 510
		if score == 10000 or score > 10000:
			scoreX = 480
		if score == 100000 or score > 100000:
			scoreX = 460

		# check if the pillows and the coin is out of bounds

		if pillowX < -80:
			pillowX = 800
			score += 1
			move_pillow = random.randint(1, 3)
   
		if pillow2X < -80:
			pillow2X = 800
			score += 1
			move_pillow2 = random.randint(1, 3)
   
		if coinX < -55:
			coinX = random.randint(1000, 1500)
			move_coin = random.randint(1, 3)

		# checks for collision between the player and the pillow and also the player and the coin
		if player_rect.colliderect(coin_rect):
			if (time() - coin_delay) > 0.1:
				pygame.mixer.Sound.play(pickupcoin)
				score += 10
				coinX = random.randint(2000, 5000)
    
				move_coin = random.randint(1, 3)
			coin_delay = time()
   
		if player_rect.colliderect(pillow_rect):
			if (time() - latest_hit_time) > 0.1:
				pygame.mixer.Sound.play(lostlife)
				hearts -= 1
			latest_hit_time = time()
   
		if player_rect.colliderect(pillow2_rect):
			if (time() - latest_hit_time2) > 0.1:
				pygame.mixer.Sound.play(lostlife)
				hearts -= 1
			latest_hit_time2 = time()
			
		if hearts == 0:
			screen.blit(zerohearts_img, (560, 530))
			pillow_move_speed = 0
			move = 0
			sleep(0.1)
			game_over()

		# move the character when move equals something

		if move == 2:
			playerY = 250
		if move == 3:
			playerY = 50
		if move == 1:
			playerY = 450

		# check if move_pillow equals something

		if move_pillow == 2:
			pillowY = 250
		if move_pillow == 3:
			pillowY = 50
		if move_pillow == 1:
			pillowY = 450
   
		if move_pillow2 == 2:
			pillow2Y = 250
		if move_pillow2 == 3:
			pillow2Y = 50
		if move_pillow2 == 1:
			pillow2Y = 450
   
		if move_coin == 2:
			coinY = 250
		if move_coin == 3:
			coinY = 50
		if move_coin == 1:
			coinY = 450

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

				# change the value of move for arrow keys

				if event.key == pygame.K_UP and move == 2:
					move = 3
				if event.key == pygame.K_DOWN and move == 2:
					move = 1
				if event.key == pygame.K_DOWN and move == 3:
					move = 2
				if event.key == pygame.K_UP and move == 1:
					move = 2
				if event.key == pygame.K_UP and move == 3:
					move = 3
				if event.key == pygame.K_DOWN and move == 1:
					move = 1

				# change the value of move for wasd

				if event.key == pygame.K_w and move == 2:
					move = 3
				if event.key == pygame.K_s and move == 2:
					move = 1
				if event.key == pygame.K_s and move == 3:
					move = 2
				if event.key == pygame.K_w and move == 1:
					move = 2
				if event.key == pygame.K_w and move == 3:
					move = 3
				if event.key == pygame.K_s and move == 1:
					move = 1

		pygame.display.update()
		clock.tick(61)
main_menu()