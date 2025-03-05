from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import *

import os


class ImageProcessor:
    # класс-обработчик картинки
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'

    def load_image(self, directory, filename):
        # запоминает путь и имя файла при загрузке
        self.dir = directory
        self.filename = filename
        image_path = os.path.join(directory, filename)
        self.image = Image.open(image_path)

    def show_image(self, path):
        # показать картинку в приложении
        lb_image.hide()
        pixmap_image = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        # встроим картинку в приложение, сохранив соотношение сторон
        pixmap_image = pixmap_image.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmap_image)
        # покажем картинку
        lb_image.show()

    def save_image(self):
        """сохранить копию файла в подпапке"""
        path = os.path.join(self.dir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):
        """ЧБ фильтр"""
        self.image = self.image.convert('L')
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_flip(self):
        """отразить фото зеркально"""
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_sharpen(self):
        """добавить резкости"""
        self.image = self.image.filter(SHARPEN)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_left(self):
        """повернуть влево"""
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_right(self):
        """повернуть вправо"""
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)


def show_chosen_image():
    # показать ВЫБРАННУЮ картинку
    if lw_files.currentRow() >= 0:
        # если выбран какой-то файл - получаем его название, ищем и отображаем
        filename = lw_files.currentItem().text()
        workimage.load_image(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.show_image(image_path)


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

# создаём объект класса ImageProcessor- обработчик картинки
workimage = ImageProcessor()
lw_files.currentRowChanged.connect(show_chosen_image)
# привяжем функции к кнопкам
btn_dir.clicked.connect(showFilenamesList)

btn_bw.clicked.connect(workimage.do_bw)
btn_flip.clicked.connect(workimage.do_flip)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)

win.show()
app.exec()
