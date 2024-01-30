import pygame

pygame.init()

racket_x = 200
racket_y = 500

back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()


class Area:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def colliderect(self, x, y):
        return self.rect.colliderect(x, y)


class Label(Area):
    def set_text(self, text, fsize, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', 200, 330, 100, 30)

start_x = 5
start_y = 5
count = 10
monsters = []

for j in range(4):
    y = start_y + (45 * j)
    x = start_x + (22.5 * j)
    for i in range(count):
        d = Picture('enemy.png', x, y, 40, 40)
        monsters.append(d)
        x += 45
    count -= 1

game_over = False

move_right = False
move_left = False
move_down = False
move_up = False

dx = 3
dy = 3

while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_UP:
                move_up = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_UP:
                move_up = False

    if move_right:
        platform.rect.x += 5
    if move_left:
        platform.rect.x -= 5
    if move_down:
        platform.rect.y += 5
    if move_up:
        platform.rect.y -= 5

    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.colliderect(platform.rect):
        dy *= -1

    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1

    if ball.rect.y < 0:
        dy *= -1

    if ball.rect.y > racket_y + 5:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('ТЫ ПРОИГРАЛ', 60, (255, 0, 0))
        time_text.draw(10, 10)
        game_over = True

    if len(monsters) == 0:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('ПОБЕДА', 60, (3, 198, 18))
        time_text.draw(10, 10)
        game_over = True

    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            dy *= -1
    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)