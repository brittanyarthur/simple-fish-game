# 1 - Import library
import pygame
from pygame.locals import *
 
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
# 3 - Load images
background = pygame.image.load("resources/images/underwater.jpg")
player = pygame.image.load("resources/images/red_fish.png")

# variables
playerpos=[100,100]

#built in game constants, assign to more intuitive variables
left = K_a
right = K_s
up = K_w
down = K_d

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background, (0, 0))
    screen.blit(player, playerpos)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        #check if key down was pressed, going left
        if event.type == pygame.KEYDOWN and event.key == left:
            playerpos[0] -= 5
        if event.type == pygame.KEYDOWN and event.key == right:
            playerpos[0] += 5

        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)