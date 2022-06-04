from pygame import *

class GamePlayer(sprite.Sprite):
    def __init__(self, img, width, height, x, y, step):
        super().__init__()
        self.image = transform.scale(
            image.load(img),
            (width, height)
            )
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.step = step 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class LeftPlayer(GamePlayer):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.step
        elif keys[K_s] and self.rect.y < 500 - self.height:
            self.rect.y += self.step

class RightPlayer(GamePlayer):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.step
        elif keys[K_DOWN] and self.rect.y < 500 - self.height:
            self.rect.y += self.step

window = display.set_mode((800, 500))
background = transform.scale(
    image.load('pingpong_table.jpg'),
    (800, 500)
)
fps = 60
clock = time.Clock()
game = True

player_1 = LeftPlayer('pingpong_rocket.png', 10, 65, 40, 215, 10)
player_2 = RightPlayer('pingpong_rocket.png', 10, 65, 750, 215, 10)
ball = GamePlayer('pingpong_ball.png', 20, 20, 400, 250, 20)
dx = 3
dy = 3

player_2.image = transform.rotate(player_2.image, 180)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if ball.rect.x >= 780 or ball.rect.x <= 0:
        dx *= -1
    if ball.rect.y >= 480 or ball.rect.y <= 0:
        dy *= -1
    ball.rect.x += dx
    ball.rect.y += dy
    window.blit(background, (0, 0))
    player_1.update()
    player_1.reset()
    player_2.update()
    player_2.reset()
    ball.reset()
    display.update()
    clock.tick(fps)