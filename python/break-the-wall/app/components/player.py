from pygame.sprite import Sprite
from pygame import Surface, Rect, key, K_LEFT, K_RIGHT
from constants import *

class Player(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Surface((100, 10))
        self.image.fill(COLOR_BLACK)
        self.rect: Rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 30
        self.speed = 5 

    def update(self) -> None:
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed