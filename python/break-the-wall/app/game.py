from components.brick import Brick
from components.ball import Ball
from components.player import Player
from pygame.sprite import spritecollide, collide_mask
from pygame import init, display, Surface, quit as pygame_quit, event as pygame_event, QUIT, key
from pygame import K_LEFT, K_RIGHT
from pygame import draw
from pygame.sprite import Group
from pygame.time import Clock
from constants import *
from random import randint
from pygame.font import Font 

class Game: 
    def __init__(self) -> None: 
        self.points: int = 0
        self.lives: int = GAME_LIVES
        self.y_coordinate: int = 60
        self.playGame: bool = True 

        init()
        self.__init_components()

    def __init_components(self) -> None: 
        self.screen: Surface = display.set_mode(SCREEN_SIZE)
        display.set_caption(GAME_TITLE)
        self.clock: Clock = Clock()
        self.components: Group = Group()
        self.bricks: Group = Group()
        self.__init_player()
        self.__init_ball()
        self.__init_wall()

    def __init_player(self) -> None: 
        self.player: Player = Player(COLOR_WHITE, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.player.rect.x = PLAYER_COORDINATE_X
        self.player.rect.y = PLAYER_COORDINATE_Y
        self.components.add(self.player)

    def __init_ball(self) -> None: 
        self.ball: Ball = Ball(COLOR_WHITE, 
                               (BALL_WIDTH, BALL_HEIGHT), 
                               (-7, 7))
        self.ball.rect.x = BALL_COORDINATE_X
        self.ball.rect.y = BALL_COORDINATE_Y
        self.components.add(self.ball)

    def __init_wall(self) -> None:
        for i in range(ROWS): 
            for j in range(COLUMNS): 
                brick_color: Color = COLORS[randint(0, len(COLORS))]
                brick: Brick = Brick(brick_color, (BLOCK_WIDTH, BLOCK_HEIGHT))
                brick.rect.x = 60 + j*100
                brick.rect.y = self.y_coordinate
                self.components.add(brick)
                self.bricks.add(brick)
            self.y_coordinate += 40

    def __handle_events(self) -> None: 
        for event in pygame_event.get(): 
            if event.type == QUIT: 
                self.playGame = False 
        keys = key.get_pressed()
        if keys[K_LEFT]: 
            self.player.move_left(5)
        elif keys[K_RIGHT]: 
            self.player.move_right(5)
    
    def __update(self) -> None: 
        if self.components.update()

        # kretanje lopte 
        if self.ball.rect.x >= SCREEN_WIDTH-10 or self.ball.rect.x <= 0: 
            self.ball.speed[0] = -self.ball.speed[0]
        if self.ball.rect.y < 40: 
            self.ball.speed[1] = -self.ball.speed[1]
        if self.ball.rect.y > SCREEN_HEIGHT - 10: 
            self.ball.speed[1] = -self.ball.speed[1]
            self.lives -= 1
            if not self.lives: 
                self.show_message("GAME OVER")
                self.playGame = False 

        # Sudar lopte i igrača
        if collide_mask(self.ball, self.player):
            self.ball.rect.x -= self.ball.speed[0]
            self.ball.rect.y -= self.ball.speed[1]
            self.ball.bounce()

        # Sudar lopte i cigli
        brick_collision_list = spritecollide(self.ball, self.bricks, False)
        for brick in brick_collision_list:
            self.ball.bounce()
            self.points += 1
            brick.kill()
            if len(self.bricks) == 0:
                self.show_message("YOU WON!")
                self.playGame = False

    def __render(self):
        self.screen.fill(COLOR_BACKGROUND)
        draw.line(self.screen, WHITE, [0, 38], [800, 38], 2)

        font = pygame.font.Font(None, 34)
        points_text = font.render(f"Points: {self.points}", 1, WHITE)
        lives_text = font.render(f"Lives: {self.lives}", 1, WHITE)
        self.screen.blit(points_text, (20, 10))
        self.screen.blit(lives_text, (650, 10))

        self.components.draw(self.screen)
        pygame.display.flip()

    def show_message(self, message: str):
        font = pygame.font.Font(None, 74)
        text = font.render(message, 1, WHITE)
        self.screen.blit(text, (200, 300))
        pygame.display.flip()
        pygame.time.wait(3000)


    def run(self) -> None: 
        
        while self.playGame: 
            self.__handle_events()
            self.__update()
            self.__render()
        
        pygame_quit()

