from pygame import *


class GameSprite(sprite.Sprite):
    """класс-родитель для спрайтов"""

    def __init__(self, player_image, player_x, player_y, player_speed, weight, height):
        """конструктор класса"""
        super().__init__()
        # каждый спрайт хранит изображение image
        self.image = transform.scale(image.load(player_image), (weight, height))
        self.speed = player_speed
        # каждый спрайт - это прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        """отобразить персонажа"""
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    """класс-наследник для ракетки (управляется стрелками или WS)"""

    def move_left(self):
        """перемещение левой ракетки клавишами"""
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def move_right(self):
        """перемещение правой ракетки стрелками"""
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


# игровая сцена
back = 'darkslategray1'  # цвет фона
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))  # окно
window.fill(back)

# персонажи игры
racket1 = Player('racket.png', 30, 200, 4, 60, 150)
racket2 = Player('racket.png', 520, 200, 4, 60, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 30, 30)

# флаги игры
game = True
finish = False
clock = time.Clock()
FPS = 60

# шрифты
font.init()
font_sample = font.Font(None, 35)
lose1 = font_sample.render('ИГРОК 1 ПРОИГРАЛ', True, 'brown1')
lose2 = font_sample.render('ИГРОК 2 ПРОИГРАЛ', True, 'brown1')

# переменные, отвечающие за перемещение мяча по X и Y
speed_x = 3
speed_y = 3

# игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)

        # столкновение мяча и платформы:
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        # если мяч касается верхней или нижней стены:
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        # если мяч улетел дальше левой ракетки - проиграл первый
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        # если мяч улетел дальше правой ракетки - проиграл второй
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.move_left()
        racket2.move_right()

        # добавляем мячу постоянную скорость
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
