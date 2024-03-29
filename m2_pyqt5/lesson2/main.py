from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def show_win():
    # победа
    victory_win = QMessageBox()
    victory_win.setText('Верно!\nВы выиграли iphone 15')
    victory_win.exec()


def show_lose():
    # проигрыш
    lose_win = QMessageBox()
    lose_win.setText('Неправильно! Материков 6!')
    lose_win.exec()


# создаём приложение, окно
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Викторина')
main_win.resize(400, 200)

# создаём виджеты
question = QLabel('Сколько материков на планете Земля?')
btn1 = QRadioButton('7')
btn2 = QRadioButton('6')
btn3 = QRadioButton('8')
btn4 = QRadioButton('5')

# создаём лэйауты, размещаем виджеты
layout_main = QVBoxLayout()
layH1 = QHBoxLayout()
layH2 = QHBoxLayout()
layH3 = QHBoxLayout()

layH1.addWidget(question, alignment=Qt.AlignCenter)
layH2.addWidget(btn1, alignment=Qt.AlignCenter)
layH2.addWidget(btn2, alignment=Qt.AlignCenter)
layH3.addWidget(btn3, alignment=Qt.AlignCenter)
layH3.addWidget(btn4, alignment=Qt.AlignCenter)

layout_main.addLayout(layH1)
layout_main.addLayout(layH2)
layout_main.addLayout(layH3)
main_win.setLayout(layout_main)

# привязываем кнопки к методам
btn1.clicked.connect(show_lose)
btn2.clicked.connect(show_win)
btn3.clicked.connect(show_lose)
btn4.clicked.connect(show_lose)

main_win.show()
app.exec_()
