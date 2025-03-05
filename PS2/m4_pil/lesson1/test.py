from PIL import *

with Image.open('original.jpg') as pic_original:
    print('Размер:', pic_original.size)
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode)
    pic_original.show()
    pic_gray = pic_original.convert('L')
    pic_gray.show()