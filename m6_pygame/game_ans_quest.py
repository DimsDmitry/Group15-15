import pygame
from random import randint

pygame.init()

# создание окна игры
clock = pygame.time.Clock()
mw = pygame.display.set_mode((500, 500))
back = (189, 236, 255)  # цвет фона
mw.fill(back)
# цвета
LIGHT_BLUE = (185, 192, 255)
BLACK = (0, 0, 0)


# класс для создания прямоугольника с текстом
class TextArea:
    def __init__(self, x, y, width, height, color):
        # создаём прямоугольник
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
        # список с надписями
        self.titles = list()

    def add_text(self, text):
        self.titles.append(text)

    def set_text(self, number, fsize, text_color=BLACK):
        # установить текст
        self.text = self.titles[number]
        self.image = pygame.font.Font(None, fsize).render(self.text, True, text_color)

    def draw(self, shift_x, shift_y):
        # отрисовать прямоугольник с текстом
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


# создание карточек
quest_card = TextArea(120, 100, 290, 70, LIGHT_BLUE)
ans_card = TextArea(120, 240, 290, 70, LIGHT_BLUE)
quest_card.add_text('Вопрос')
ans_card.add_text('Ответ')

quest_card.add_text('Что изучаешь в Алгоритмике?')
quest_card.add_text('На каком языке говорят во Франции?')
quest_card.add_text('Что растёт на яблоне?')

ans_card.add_text('Python')
ans_card.add_text('Французский')
ans_card.add_text('Яблоки')

quest_card.set_text(0, 75)
ans_card.set_text(0, 75)

quest_card.draw(10, 10)
ans_card.draw(10, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint(1, len(quest_card.titles) - 1)
                quest_card.set_text(num, 25)
                quest_card.draw(10, 25)

            if event.key == pygame.K_a:
                num = randint(1, len(ans_card.titles) - 1)
                ans_card.set_text(num, 25)
                ans_card.draw(10, 25)
    pygame.display.update()
    clock.tick(40)
