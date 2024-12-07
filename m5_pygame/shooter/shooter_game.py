from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    """класс-родитель для спрайтов"""

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        """конструктор класса"""
        super().__init__()
        # каждый спрайт хранит изображение image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
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

    def update(self):
        """перемещение игрока клавишами"""
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        """стрельба"""
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    """класс-наследник для спрайта-противника (перемещается автоматически вниз)"""

    def update(self):
        """перемещение автоматически - координата rect.y постоянно растёт"""
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            # если противник достигает нижней границы экрана, lost увеличивается на 0, а противник перемещается вверх
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1


class Bullet(GameSprite):
    """класс спрайта-пули"""

    def update(self):
        """перемещается автоматически снизу вверх (координата Y уменьшается)"""
        self.rect.y += self.speed
        # пуля исчезнет, если дойдёт до края экрана
        if self.rect.y < 0:
            self.kill()


# создаём окно игры
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Космический шутер")
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

# фоновая музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')  # звук выстрела

# шрифты
font.init()
font1 = font.Font(None, 80)  # объект класса "надпись" для отображения победы и поражения
font2 = font.Font(None, 36)  # объект класса "надпись" для счётчиков кораблей

score = 0  # сбито кораблей
lost = 0  # пропущено кораблей
max_lost = 3  # допустимое количество пропущенных кораблей
goal = 30  # цель - сбить столько кораблей

win = font1.render('ПОБЕДА!!!', True, 'cornsilk1')  # победа
lose = font1.render('ПОРАЖЕНИЕ', True, 'crimson')  # поражение
restart = font1.render('ПЕРЕЗАПУСК ИГРЫ...', True, 'cadetblue3')  # перезапуск игры

# спрайты игры
ship = Player('rocket.png', 5, win_height - 110, 80, 100, 10)

bullets = sprite.Group()
monsters = sprite.Group()
for i in range(5):
    # создаём несколько противников, помещаем каждого в группу monsters
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

# переменные для игрового цикла
finish = False
game = True

# игровой цикл
while game:
    for e in event.get():
        # обработка нажатия на кнопку ЗАКРЫТЬ
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            # нажали пробел - выстрел
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()

    if not finish:
        # если finish == False, обновляем экран и включаем движение спрайтов
        window.blit(background, (0, 0))
        ship.update()
        monsters.update()
        bullets.update()

        # проверка столкновения пуль и монстров (и пуля, и монстр при касании исчезают)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        # collides - словарь, хранящий все столкновения пуль и монстров
        for c in collides:
            # увеличиваем счётчик сбитых врагов на 1
            score += 1
            # создаём нового противника
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
        # ПОРАЖЕНИЕ - пропустили слишком много противников или столкнулись с одним из них
        if lost >= max_lost or sprite.spritecollide(ship, monsters, False):
            finish = True
            window.blit(lose, (200, 200))

        # ПОБЕДА - сбили требуемое количество противников
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        # создаём счётчики сбитых и пропущенных кораблей, отображаем их на экране
        text = font2.render(f'Счёт: {str(score)}', 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render(f'Пропущено: {str(lost)}', 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        display.update()
    else:
        time.delay(3000)
        # когда игра заканчивается, уничтожаем все объекты игры, обнуляем счётчики
        finish = False
        # window.blit(restart, (200, 200))
        score = 0
        lost = 0
        for b in bullets:
            b.kill()

        for m in monsters:
            m.kill()

        # делаем паузу в 3 секунды

        for i in range(5):
            # создаём несколько противников, помещаем каждого в группу monsters
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

    time.delay(50)
    # 1000мс / 50мс = 20 кадров в сек.
