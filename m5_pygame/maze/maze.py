from pygame import *


class GameSprite(sprite.Sprite):
    """класс-родитель для спрайтов"""

    def __init__(self, player_image, player_x, player_y, player_speed):
        """конструктор класса"""
        super().__init__()
        # каждый спрайт хранит изображение image
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        # каждый спрайт - это прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        """отобразить персонажа"""
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    """класс-наследник для спрайта-игрока (управляется стрелками)"""

    def move(self):
        """перемещение игрока клавишами"""
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Enemy(GameSprite):
    """класс-наследник для спрайта-врага (перемещается сам)"""
    direction = 'left'

    def move(self):
        """перемещение влево-вправо"""
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        # в зависимости от значения переменной direction перемещаем персонажа влево-вправо
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


# игровая сцена
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
# заголовок
display.set_caption('Maze')
# загружаем картинку на фон
background = transform.scale(image.load('background.jpg'), (win_width, win_height))

# персонажи игры
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

# переменные для работы игрового цикла
game = True
clock = time.Clock()
FPS = 60

# музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

# игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    player.reset()
    monster.reset()
    final.reset()

    player.move()
    monster.move()

    display.update()
    clock.tick(FPS)
