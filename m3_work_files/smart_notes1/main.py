from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json

# работа с json-файлом
notes = {
    'Добро пожаловать!': {
        'текст': 'Это самое лучшее приложение для заметок в мире!',
        'теги': ['добро', 'инструкция']
    }
}

with open('notes_data.json', 'w') as file:
    json.dump(notes, file)

app = QApplication([])
# интерфейс приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600)

# виджеты окна приложения
field_text = QTextEdit()

list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')

button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')

list_tags_label = QLabel('Список тегов')
list_tags = QListWidget()
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')

button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')

# расположение виджетов по лэйаутам
layout_notes = QHBoxLayout()
# главный лэйаут делится на два:
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(field_text)

col2.addWidget(list_notes_label)
col2.addWidget(list_notes)

row1 = QHBoxLayout()
row1.addWidget(button_note_create)
row1.addWidget(button_note_del)

row2 = QHBoxLayout()
row2.addWidget(button_note_save)

col2.addLayout(row1)
col2.addLayout(row2)

col2.addWidget(list_tags_label)
col2.addWidget(list_tags)
col2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_4 = QHBoxLayout()

row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4.addWidget(button_tag_search)

col2.addLayout(row_3)
col2.addLayout(row_4)
# устанавливаем главную линию на окно
layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)
notes_win.setLayout(layout_notes)

#запуск приложения
notes_win.show()
app.exec()