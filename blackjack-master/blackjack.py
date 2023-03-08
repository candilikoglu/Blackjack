#!/usr/bin/env python
"""
This is a gui based blackjack game using pygame

Copyright (C) Torbjorn Hedqvist - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license. See LICENSE file in the project
root for full license information.

"""

# Standard imports
import time

# Local imports
from includes.blackjackfsm import *

# Specialized imports from lib. Add lib to path
# import os
# import sys
# MAIN_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.insert(1, os.path.join(MAIN_DIR, 'lib'))
__name__ = "__mainMenu__"
class mainMenu():

    pygame.display.set_caption("Main Menu")
    pygame.font.init()
    import pygame 
    pygame.init()

    screen = pygame.display.set_mode(GAME_BOARD_SIZE)
    # white color
    color = (255,255,255)
    # light shade of the button
    color_light = (170,170,170)
    # dark shade of the button
    color_dark = (100,100,100)
    # stores the width of the
    # screen into a variable
    width = screen.get_width()
    # stores the height of the
    # screen into a variable
    height = screen.get_height()

    # defining a font
    smallfont = pygame.font.SysFont('Corbel',35)

    text = smallfont.render('START GAME' , True , color)
    pygame.display.set_mode((GAME_BOARD_SIZE))
    # light shade of the button
    color_light = (170,170,170)
    color = (255,255,255)
    # dark shade of the button
    color_dark = (100,100,100)
    smallfont = pygame.font.SysFont('Corbel',35)

    text = smallfont.render('START GAME' , True , color)
    
    running  = True
    while running:            
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False 
                pygame.quit()     
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse is clicked on the
                # button the game is terminated
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                    running = False
                    __name__ = "__main__"
                    
        # fills the screen with a color
        screen.fill((60,25,60))
        
        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        
        # if mouse is hovered on a button it
        # changes to lighter shade 
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
            
        else:
            pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
        
        # superimposing the text onto our button
        screen.blit(text , (width/2+50,height/2))
        
        # updates the frames of the game
        pygame.display.update()

class BlackJack(object):
    """
    Main game class

    It contains a main loop and from inside that loop the whole game
    consists of various states in a finite state machine.
    The game will continue in this loop until the player are out of
    money or the player hits the exit of the main window.

    """

    # Initialize pygame hooks
    pygame.init()
    pygame.display.set_caption("Black Ace's Black Jack")
    pygame.font.init()
    clock = pygame.time.Clock()

    # Instantiate the common variable singleton objects
    common_vars = CommonVariables.get_instance()
    button_status = ButtonStatus.get_instance()
    image_db = ImageDB.get_instance()

    #background 
    #background = pygame.image.load('game_board_blackjack.png')
    # Populate the needed common variables with initial values
    common_vars.done = False
    common_vars.screen = pygame.display.set_mode(GAME_BOARD_SIZE)
    common_vars.player_cash = DEFAULT_PLAYER_BALANCE
    common_vars.game_rounds = 0
    common_vars.pause_time = 0
    common_vars.dealer_last_hand = 0
    common_vars.player_hands = []
    common_vars.button_image_width = image_db.get_image(IMAGE_PATH_BUTTONS + HIT_BUTTON_FILENAME_ON).get_width()
    common_vars.button_image_height = image_db.get_image(IMAGE_PATH_BUTTONS + HIT_BUTTON_FILENAME_ON).get_height()
    common_vars.chips_image_width = image_db.get_image(IMAGE_PATH_CHIPS + CHIP_5_FILENAME_ON).get_width()
    common_vars.chips_image_height = image_db.get_image(IMAGE_PATH_CHIPS + CHIP_5_FILENAME_ON).get_height()

    common_vars.text_font = pygame.font.SysFont('Courier New', 25, bold=True)  # bold=True
    value_of_players_hand_font = pygame.font.SysFont('Courier New', 25, bold=True)

    current_state = InitialState()

    # Main game loop
    while not common_vars.done:
        # Plot the base table
        common_vars.screen.fill(GAME_BOARD_COLOR)
        #background image
        common_vars.screen.blit(image_db.get_image(IMAGE_PATH + 'game_board.xcf'), (0, 0))
        # TODO: Can handle scaling much better to be prepared for other board sizes.
        x_pos = int(GAME_BOARD_X_SIZE * 0.10)
        y_pos = GAME_BOARD_Y_SIZE - 250
        common_vars.screen.blit(image_db.get_image(IMAGE_PATH + 'yellow_box_179_120.png'), (x_pos + 35, y_pos - 150)) 
        x_pos = int((GAME_BOARD_X_SIZE - image_db.get_image(IMAGE_PATH + "bj_banner_yellow2.png").get_width()) / 2)
        y_pos = GAME_BOARD_Y_SIZE - 700
        common_vars.screen.blit(image_db.get_image(IMAGE_PATH + "bj_banner_yellow2.png"), (x_pos, y_pos))

        if COUNTING_HELP:
            # Plot the value of the current hand
            x_pos = 22 #22
            for hand in common_vars.player_hands:
                count = get_value_of_players_hand(hand)
                if count:
                    message = value_of_players_hand_font.render('{0}'.format(count), False, YELLOW_COLOR)
                    common_vars.screen.blit(message, (x_pos + 325, GAME_BOARD_Y_SIZE - 810)) #270
                x_pos += GAP_BETWEEN_SPLIT

        # Plot the players current credits and number of played rounds.
        x_pos, y_pos = STATUS_START_POS
        message1 = common_vars.text_font.render('[Credit: ${0}]'.format(
            common_vars.player_cash, common_vars.game_rounds), False, YELLOW_COLOR)
        common_vars.screen.blit(message1, (x_pos, y_pos))

        message2 = common_vars.text_font.render('[Hands played: {1} ]'.format(
            common_vars.player_cash, common_vars.game_rounds), False, YELLOW_COLOR)
        common_vars.screen.blit(message2, (x_pos, y_pos + 25))

        message3 = common_vars.text_font.render('[Dealers last hand: {0} ]'.format(
            common_vars.dealer_last_hand), False, YELLOW_COLOR)
        common_vars.screen.blit(message3, (x_pos, y_pos + 50))

        message4 = common_vars.text_font.render('[Players Current Hand:   ]', False, YELLOW_COLOR)
        common_vars.screen.blit(message4, (x_pos, y_pos + 75))

        # Go to current state
        current_state(common_vars, button_status)

        # Update the content of the display
        pygame.display.flip()

        # Insert a pause (Note! locking for input or updates during this period)
        if common_vars.pause_time:
            time.sleep(common_vars.pause_time)
            common_vars.pause_time = 0  # Reset

        # Set the frame rate fps for window update
        clock.tick(10)


if __name__ == '__main__':
    MY_GAME = BlackJack()
