from turtle import *


class Sprite(Turtle):
    # класс-наследник черепашки
    def __init__(self, x, y, step, shape, color):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
        self.points = 0
    # движение черепашки:
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())


player = Sprite(0, -100, 10, 'circle', 'orange')

scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_down, 'Down')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')



