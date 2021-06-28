################################################################################
# NAME:         Mike Feltham
# DATE:         7 December 2017
# COURSE:       LS 111-A
# ASSIGNMENT:   Tank Game
# PURPOSE:      Multiplayer tank game that allows two players to move left or
#               or right on opposite boundaries and fire bullets at each other.
#               The bullets subtract 1 health and the tanks both have 10 health.
#               The first tank to lower their opponent to 0 health wins.
#KNOWN ISSUES:  None
################################################################################
import pygame, sys

from pygame.locals import *

import random

#Returns the number of milliseconds since pygame.init() was called
pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

#Sets window size
DISPLAYSURF = pygame.display.set_mode((600, 400))

#Music
#chooses song randonly and loads/plays on loop
jukebox= random.randrange(1,8)
if jukebox== 1:
    pygame.mixer.music.load('Stayin Alive.mp3')
    pygame.mixer.music.play(-1,0.0)
    
if jukebox== 2:
    pygame.mixer.music.load('Sandstorm.mp3')
    pygame.mixer.music.play(-1,0.0)
    
if jukebox== 3:
    pygame.mixer.music.load('The Final Countdown.mp3')
    pygame.mixer.music.play(-1,0.0)
    
if jukebox== 4:
    pygame.mixer.music.load('Jump.mp3')
    pygame.mixer.music.play(-1,0.0)
    
if jukebox== 5:
    pygame.mixer.music.load('Through The Fire and Flames.mp3')
    pygame.mixer.music.play(-1,0.0)
    
if jukebox== 6:
    pygame.mixer.music.load('Shooting Stars.mp3')
    pygame.mixer.music.play(-1,0.0)

if jukebox== 7:
    pygame.mixer.music.load('Crazy Train.mp3')
    pygame.mixer.music.play(-1,0.0)

#Defined Colors
# Color = (Red, Green, Blue)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tank Data
# x and y coordinates of tanks
blue_x = 0
blue_y = 10

red_x = 600
red_y = 350

# defined tank heaight and width
tank_width = 190
tank_height = 40

# bullet coordinates
red_b_x = -10
red_b_y = -200

blue_b_x = -10
blue_b_y = -10

bull_speed = 15

# before key is pressed
# when statement becomes true different conditions take place
move_blue_left = False
move_blue_right = False

move_red_left = False
move_red_right = False

#fires bullets
fire_red = False
fire_blue = False

#Health            
blue_health = 10
red_health = 10

pygame.display.set_caption('Tank Game')

print ('You both have 10 health.')

while True: #Game loop

    #Sets Background
    DISPLAYSURF.fill(BLACK)

    #Draw Tanks
    pygame.draw.rect(DISPLAYSURF, BLUE, (blue_x, blue_y, tank_width, tank_height))
    pygame.draw.rect(DISPLAYSURF, RED, (red_x, red_y, tank_width, tank_height))

    #Draw Bullets
    pygame.draw.rect(DISPLAYSURF, RED, (red_b_x, red_b_y, 10, 10))
    pygame.draw.rect(DISPLAYSURF, BLUE, (blue_b_x, blue_b_y, 10, 10))

    #Draws Line
    pygame.draw.rect(DISPLAYSURF, WHITE, (0, 200, 600, 3))

    

    #Assign Keys
    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_blue_left = True
            elif event.key == K_RIGHT:
                move_blue_right = True
            elif event.key == K_RETURN:
                fire_blue = True
            
            elif event.key == K_a:
                move_red_left = True
            elif event.key == K_d:
                move_red_right = True
            elif event.key == K_SPACE:
                fire_red = True 
                
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                 move_blue_left = False
            elif event.key == K_RIGHT:
                move_blue_right = False
            elif event.key == K_RETURN:
                fire_blue = False

            elif event.key == K_a:
                move_red_left = False
            elif event.key == K_d:
                move_red_right = False
            elif event.key == K_SPACE:
                fire_red = False 

    # Move Blue Tank
    if move_blue_left == True:
        blue_x = blue_x - 10
    if move_blue_right == True:
        blue_x = blue_x + 10

    if blue_x < 0:
        blue_x = 0
    if blue_x > 600 - tank_width:
        blue_x = 600 - tank_width

    # Move Red Tank
    if move_red_left == True:
        red_x = red_x - 10
    if move_red_right == True:
        red_x = red_x + 10

    if red_x < 0:
        red_x = 0
    if red_x > 600 - tank_width:
        red_x = 600 - tank_width

    #Blue Tank Bullets
    #set bullets to center of tank
    if fire_blue == True:
        blue_b_y = blue_y
        blue_b_x = blue_x + tank_width/2 - 5

    #Red Tank Bullets
    #set bullets to center of tank
    if fire_red == True:
        red_b_y = red_y + tank_height
        red_b_x = red_x + tank_width/2 - 5

    # Move Bullets
    red_b_y = red_b_y - bull_speed
    blue_b_y = blue_b_y + bull_speed

    # Check if bullet hit red
    if red_x < blue_b_x + 5 < red_x + tank_width:
        if red_y < blue_b_y + 5 < red_y + tank_height:
            blue_b_x = 800 

    # Red Health
            if blue_b_x == 800:
                red_health = red_health - 1
                print ('red health:',red_health)
                
    # Check if bullet hit blue
    if blue_x < red_b_x + 5 < blue_x + tank_width:
        if blue_y < red_b_y + 5 < blue_y + tank_height:
            red_b_x = 900
            
    # Red Health
            if red_b_x == 900:
                blue_health = blue_health - 1
                print ('blue health:',blue_health)
 
    # Win
    if red_health <= 0:

        print ('Blue Wins! Exit out of shell and restart to play again.')
        break

    if blue_health <= 0:
        
        print ('Red Wins! Exit out of shell and restart to play again.')
        break

   # Update the screen
    pygame.display.update()
    fpsClock.tick(FPS)

#Work Cited:
#pygame.org
#https://www.pygame.org/docs/
