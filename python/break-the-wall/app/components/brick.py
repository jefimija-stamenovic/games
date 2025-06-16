from pygame.sprite import Sprite
from pygame import Surface, Rect
from constants import *

class Brick(Sprite):
    def __init__(self, x: int, y: int, *groups) -> None:
        super().__init__(*groups)
        self.image = Surface((75, 20))
        self.image.fill(COLOR_ORANGE)
        self.rect: Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y