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


class Wall(sprite.Sprite):
    """класс для стен-препятствий"""

    def __init__(self, wall_color, wall_x, wall_y, wall_width, wall_height):
        """конструктор класса"""
        super().__init__()
        self.wall_color = wall_color
        self.width = wall_width
        self.height = wall_height
        # картинка стены - прямоугольник определённого размера и цвета
        self.image = Surface((self.width, self.height))
        self.image.fill(wall_color)
        # каждый спрайт - это прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        """нарисовать стену"""
        window.blit(self.image, (self.rect.x, self.rect.y))

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

w1 = Wall('chartreuse3', 100, 20, 450, 10)
w2 = Wall('chartreuse3', 100, 480, 350, 10)
w3 = Wall('chartreuse3', 100, 20, 10, 380)

# переменные для работы игрового цикла
game = True
finish = False
clock = time.Clock()
FPS = 60

# музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

# шрифты
font.init()
font = font.Font(None, 70)
win = font.render('ПОБЕДА', True, 'darkgoldenrod1')
lose = font.render('ВЫ ПРОИГРАЛИ', True, 'crimson')

# игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

        player.move()
        monster.move()

        # победа - столкновение игрока и сокровища
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

        # поражение - столкновение игрока и противника, или игрока и любой из стен
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1)\
                or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()

    display.update()
    clock.tick(FPS)
