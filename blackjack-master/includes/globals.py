#!/usr/bin/env python
"""
All global constants and variables used in the blackjack game.

Copyright (C) Torbjorn Hedqvist - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license. See LICENSE file in the project
root for full license information.

"""

# Standard imports
# import inspect  # To be used to print function name in log statements
import logging

# Set log level
logging.basicConfig(
    # filename='blackjack_debug.log',
    # filemode='w',  # overwrite previous logs
    # level=logging.DEBUG,
    # level=logging.INFO,
    # level=logging.WARNING,
    format="%(asctime)s:%(levelname)s:%(module)s:%(lineno)d:%(message)s"
    )

####################
# Global constants #
####################

# Paths
IMAGE_PATH = 'images/'
IMAGE_PATH_CARDS = 'images/cards/'
IMAGE_PATH_CHIPS = 'images/casino_chips/'
IMAGE_PATH_BUTTONS = 'images/buttons/'
SOUND_PATH = 'sounds/'
# previously using IMAGE_PATH = "./images/" which works as well

# The card back image used to print the dealers initial hidden card
CARDBACK_FILENAME = "cardback1.png"

# All button images
START_BUTTON = "start_button.xcf"
PLAY_BUTTON_FILENAME_ON = "play_button_blue.xcf"
PLAY_BUTTON_FILENAME_OFF = "play_button_blue_fade.xcf"
HIT_BUTTON_FILENAME_ON = "hit_button_blue.xcf"
HIT_BUTTON_FILENAME_OFF = "hit_button_blue_fade.xcf"
STAND_BUTTON_FILENAME_ON = "stand_button_blue.xcf"
STAND_BUTTON_FILENAME_OFF = "stand_button_blue_fade.xcf"
SPLIT_BUTTON_FILENAME_ON = "split_button_blue.xcf"
SPLIT_BUTTON_FILENAME_OFF = "split_button_blue_fade.xcf"
DOUBLE_DOWN_BUTTON_FILENAME_ON = "doubledown_button_blue.xcf"
DOUBLE_DOWN_BUTTON_FILENAME_OFF = "doubledown_button_blue_fade.xcf"
UNDO_BET_BUTTON_FILENAME_ON = "undobet_button_blue.xcf"
UNDO_BET_BUTTON_FILENAME_OFF = "undobet_button_blue_fade.xcf"

# All chips images
CHIP_5_FILENAME_ON = "chip_5_w85h85.xcf"
CHIP_5_FILENAME_OFF = "chip_5_w85h85_fade.xcf"
CHIP_10_FILENAME_ON = "chip_10_w85h85.xcf"
CHIP_10_FILENAME_OFF = "chip_10_w85h85_fade.xcf"
CHIP_50_FILENAME_ON = "chip_50_w85h85.xcf"
CHIP_50_FILENAME_OFF = "chip_50_w85h85_fade.xcf"
CHIP_100_FILENAME_ON = "chip_100_w85h85.xcf"
CHIP_100_FILENAME_OFF = "chip_100_w85h85_fade.xcf"

# Colors
GAME_BOARD_COLOR = (34, 139,  34)  # Nice TexasHoldem table color 34
GOLD_COLOR = (255, 215, 0)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)
YELLOW_COLOR = (255, 255, 0)

# Size, positions and gaps between objects on the game board
GAME_BOARD_SIZE = (1400, 900)
GAME_BOARD_X_SIZE = GAME_BOARD_SIZE[0]#0
GAME_BOARD_Y_SIZE = GAME_BOARD_SIZE[1]#1
PLAYER_CARD_START_POS = (175, 500)
DEALER_CARD_START_POS = (int(GAME_BOARD_X_SIZE * 0.75), 200)
CHIPS_START_POS = (1050, 500) #570, 360
BUTTONS_START_POS = (330, 800) #70, 555
STATUS_START_POS = (10, 15) #480, 15
GAP_BETWEEN_CARDS = 20
GAP_BETWEEN_CHIPS = 40
GAP_BETWEEN_BUTTONS = 130
GAP_BETWEEN_SPLIT = 190

# Timers in seconds
PAUSE_TIMER1 = 0.5
PAUSE_TIMER2 = 1
PAUSE_TIMER3 = 3

# Misc
NUM_OF_DECKS = 4
LOWEST_BET = 5
DEFAULT_PLAYER_BALANCE = 5000
COUNTING_HELP = True
