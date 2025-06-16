# Ball klasa
from pygame.sprite import Sprite
from pygame import Surface, draw, SRCALPHA, Rect
from random import choice
from constants import * 

class Ball(Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.image = Surface((15, 15), SRCALPHA)
        draw.circle(self.image, COLOR_RED, (7, 7), 7)
        self.rect: Rect = self.image.get_rect()
        self.reset_position()
        self.speed_x: int = choice([-4, 4])
        self.speed_y: int = -4

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Odbijanje od zidova
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

    def bounce(self):
        self.speed_y *= -1

    def reset_position(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x= choice([-4, 4])
        self.speed_y = -4
