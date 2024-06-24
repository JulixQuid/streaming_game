#!/usr/bin/env python
import pygame
import cv2
import numpy as np
from scripts.sprite_loader import SpriteLoader
import random
import os 

"""
Characters randomly waandering around doing random actions.

"""


# Import Modules
import os
import pygame as pg


#Loading Background
def main():
    pygame.init()
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    assets_dir = os.path.join(main_dir, "assets")

    # pygame setup
    characters = SpriteLoader.load_all_characters(assets_dir)
    print(characters)
    r_choice = random.choice(list(characters.keys()))
    a_choice = random.choice(list(characters[r_choice].keys()))
    image_sprites = characters[r_choice][a_choice]
    
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    value = 0
    dt = 0
    run = True
    #Game running routine
    while run:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with background to wipe away anything from last frame
        
        clock.tick(5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            r_choice = random.choice(list(characters.keys()))
            a_choice = random.choice(list(characters[r_choice].keys()))
            image_sprites = characters[r_choice][a_choice]
 
        
        # flip() the display to put your work on screen
        #pygame.display.flip()
        screen.fill("purple")
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        #window = pygame.display.set_mode((600, 600))

        # Setting 0 in value variable if its
        # value is greater than the length
        # of our sprite list
        value = (value + 1) % len(image_sprites)
    
        # Storing the sprite image in an
        # image variable
        image = image_sprites[value]
        # Creating a variable to store the starting
        # x and y coordinate
        x = 150
    
        # Changing the y coordinate
        # according the value stored
        # in our value variable
        y = 200
    
        # Displaying the image in our game window
        screen.blit(image, (x, y))
    
        # Updating the display surface
        pygame.display.update()
    
        # Filling the window with black color
    
        # Increasing the value of value variable by 1
        # after every iteration
        
    pygame.quit()


if __name__ == '__main__':

    if not pg.font:
        print("Warning, fonts disabled")
    if not pg.mixer:
        print("Warning, sound disabled")

    
    main()