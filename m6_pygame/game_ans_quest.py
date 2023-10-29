import pygame
from random import randint


pygame.init()

# создание окна игры
clock = pygame.time.Clock()
mw = pygame.display.set_mode((500, 500))
back = (189, 236, 255) # цвет фона
mw.fill(back)
#цвета
LIGHT_BLUE = (185, 192, 255)
BLACK = (0, 0, 0)


# класс для создания прямоугольника с текстом
class TextArea():
    def __init__(self, x, y, width, height, color):
        # создаём прямоугольник
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def set_text(self, text, fsize, text_color=BLACK):
        # установить текст
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        # отрисовать прямоугольник с текстом
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


# создание карточек
quest_card = TextArea(120, 100, 290, 70, LIGHT_BLUE)
ans_card = TextArea(120, 240, 290, 70, LIGHT_BLUE)
quest_card.set_text('Вопрос', 75)
ans_card.set_text('Ответ', 75)

quest_card.draw(10, 10)
ans_card.draw(10, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint(1, 3)
                if num == 1:
                    question = 'Что изучаешь в Алгоритмике?'
                if num == 2:
                    question = 'На каком языке говорят во Франции?'
                if num == 3:
                    question = 'Что растёт на яблоне?'
                quest_card.set_text(question, 25)
                quest_card.draw(10, 25)

            if event.key == pygame.K_a:
                num = randint(1, 3)
                if num == 1:
                    answer = 'Python'
                if num == 2:
                    answer = 'Французский'
                if num == 3:
                    answer = 'Яблоки'
                ans_card.set_text(answer, 35)
                ans_card.draw(10, 25)
    pygame.display.update()
    clock.tick(40)