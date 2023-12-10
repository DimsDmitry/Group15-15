import pygame
pygame.init()

# координаты платформы
racket_x = 200
racket_y = 330

back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

# класс из предыдущего проекта для создания спрайтов
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # прямоугольник
        self.fill_color = back

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, x, y):
        return self.rect.colliderect(rect)



# класс для объектов-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        # загружаем картинку в переменную
        self.image = pygame.image.load(filename)

    def draw(self):
        # отрисовываем картинку
        mw.blit(self.image, (self.rect.x, self.rect.y))


# создание мяча и платформы
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)

# создание врагов
start_x = 5
start_y = 5 # координаты создания 1го монстра
count = 9 # кол-во монстров в 1м ряду
monsters = [] # список для хранения монстров

for j in range(3):
    y = start_y + (55 * j) # по y смещаем на 55 с каждым столбцом
    x = start_x + (27.5 * j) # и 27.5 x
    for i in range(count): # цикл по строкам создаёт count монстров
        d = Picture('enemy.png', x, y, 50, 50)
        monsters.append(d) # создаём монстра и добавляем в список
        x += 55
    count -= 1

# флаг окончания игры
game_over = False

# игровой цикл
while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # отрисовываем всех монстров из списка
    for m in monsters:
        m.draw()

    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)