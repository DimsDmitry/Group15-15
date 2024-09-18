from PyQt5.QtWidgets import *
import os


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
    # показать список файлов, выбрать из них картинки
    extensions = '.jpg .jpeg .png .gif .bmp'.split()
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)


def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.lower().endswith(ext):
                result.append(filename)
    return result


# создаём приложение, окно
app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')

# создаём виджеты
btn_dir = QPushButton('Папка')
lw_files = QListWidget()
lb_image = QLabel('Картинка')

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_flip = QPushButton('Зеркало')
btn_sharp = QPushButton('Резкость')
btn_bw = QPushButton('Ч/Б')

# создаём лэйауты, размещаем виджеты
row = QHBoxLayout()  # основная строка
col1 = QVBoxLayout()  # делится на два столбца
col2 = QVBoxLayout()
# в первом - кнопка выбора папки и список файлов
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
# во втором - картинка и строка кнопок
col2.addWidget(lb_image, 95)
row_tools = QHBoxLayout()  # строка кнопок
# добавляем на неё кнопки:
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)
# добавляем всё на главную линию
row.addLayout(col1, 20)
row.addLayout(col2, 20)
win.setLayout(row)

btn_dir.clicked.connect(showFilenamesList)
win.show()
app.exec()
