from constants import *
from components.player import Player
from components.ball import Ball
from components.brick import Brick
from pygame.font import Font, SysFont
from pygame import Surface, display, init, quit as pygame_quit, event as pygame_event, QUIT
from pygame.sprite import Group, collide_rect, spritecollide
from pygame.time import Clock
import sys 

class Game(): 
    def create_bricks(self, group: Group) -> None:
        for row in range(ROWS):
            for col in range(COLUMNS):
                Brick(BRICK_WIDTH * col + 10, 30 + row * BRICK_HEIGHT, group)

    def draw_text(self, surface, text, color, x, y):
        font: Font = SysFont(None, 30)
        img: Surface = font.render(text, True, color)
        surface.blit(img, (x, y))

    def init_screen(self) -> None: 
        screen_size : Tuple = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen: Surface = display.set_mode(screen_size)
        display.set_caption(GAME_TITLE)

    def __init__(self) -> None:
        init()
        self.init_screen()
        self.clock: Clock = Clock()

        self.all_sprites: Group = Group()
        self.bricks: Group = Group()

        self.player: Player = Player(self.all_sprites)
        self.ball: Ball = Ball(self.all_sprites)
        self.create_bricks(self.bricks)
        self.all_sprites.add(self.bricks)

        self.lives: int = GAME_LIVES
        self.running: bool = True
    
    def play(self): 
        while self.running:
            self.clock.tick(60)

            for event in pygame_event.get():
                if event.type == QUIT:
                    pygame_quit()
                    sys.exit()

            self.all_sprites.update()

            # Sudar lopte i paddle-a
            if collide_rect(self.ball, self.player):
                self.ball.bounce()

            # Sudar lopte i cigli
            hits = spritecollide(self.ball, self.bricks, True)
            if hits:
                self.ball.bounce()

            # Ako lopta padne
            if self.ball.rect.bottom >= SCREEN_HEIGHT:
                self.lives -= 1
                if self.lives == 0:
                    print(GAME_OVER)
                    self.running = False
                else:
                    self.ball.reset_position()

            # Pobeda
            if len(self.bricks) == 0:
                print(GAME_WIN)
                self.running = False

            # Crtanje
            self.screen.fill(COLOR_BACKGROUND)
            self.all_sprites.draw(self.screen)
            self.draw_text(self.screen, f"Lives: {self.lives}", COLOR_BLACK, 10, 10)
            display.flip()

if __name__ == "__main__":
    game = Game()
    game.play()