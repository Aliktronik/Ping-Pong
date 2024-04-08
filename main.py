import pygame as pg
from settings import *
pg.init()

class GameSprite(pg.sprite.Sprite):
    def __init__(self, filename, size, coords):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords

    def reset(self, window):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self, filename, size, coords, speed=5): 
        super().__init__(filename, size, coords)
        self.speed = speed

    def update(self, key_up=pg.K_w, key_down=pg.K_s):
        keys = pg.key.get_pressed()
        if keys[key_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[key_down] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed

mw = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

player_left = Player(LEFT_PLAYER_IMG, (60, 120), (0, HEIGHT / 2))
player_right = Player(RIGHT_PLAYER_IMG, (60, 120), (WIDTH-30, HEIGHT / 2))

def game_loop():
    game = True
    finish = False
    while game:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                game = False
        
        if not finish:
            mw.fill(BG_COLOR)
            player_left.update(key_up=pg.K_w, key_down=pg.K_s)
            player_right.update(key_up=pg.K_UP, key_down=pg.K_DOWN)
            player_left.reset(mw)
            player_right.reset(mw)
        
        pg.display.update()
        clock.tick(FPS) 

if __name__ == "__main__":
    game_loop()

