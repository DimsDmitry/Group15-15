from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

# объект класса application
app = QApplication([])

# главное окно
my_win = QWidget()
my_win.setWindowTitle('Рандомайзер')
my_win.resize(400, 200)
my_win.move(100, 100)

# виджеты окна: кнопка и надпись
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')

# расположение
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
my_win.setLayout(line)


def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель')


# обработка нажатия на кнопку
button.clicked.connect(show_winner)

my_win.show()
app.exec()
