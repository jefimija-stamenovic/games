from typing import Final
from pygame import Color
from typing import Tuple 

SCREEN_WIDTH: Final = 820
SCREEN_HEIGHT: Final = 600
COLOR_WHITE: Final = Color("white")
COLOR_BACKGROUND: Final = Color("azure1")
COLOR_BLACK: Final = Color("black")

COLOR_RED: Final = Color("red")
COLOR_YELLOW: Final = Color("yellow")
COLOR_ORANGE: Final = Color("orange")

COLUMNS: Final = 10
ROWS: Final = 5
FRAMES_PER_SECOND: Final = 60
BRICK_WIDTH: Final = 80
BRICK_HEIGHT: Final = 30
SCREEN_SIZE: Final = (SCREEN_WIDTH, SCREEN_HEIGHT)
GAME_TITLE: Final = "Break the wall!"
GAME_WIN: Final = "YOU WIN!"
GAME_OVER: Final = "GAME OVER"
GAME_LIVES: int = 3

PLAYER_WIDTH: Final = 150
PLAYER_HEIGHT: Final = 10
PLAYER_COORDINATE_X: Final = 350
PLAYER_COORDINATE_Y: Final = 560

BALL_WIDTH: Final = 15
BALL_HEIGHT: Final = 15
BALL_COORDINATE_X: Final = 345
BALL_COORDINATE_Y: Final = 195

COLORS: Tuple[Color, Color, Color] = (COLOR_RED, COLOR_ORANGE, COLOR_YELLOW)
