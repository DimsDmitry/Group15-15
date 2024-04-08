from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *


def show_result():
    # показать панель ответов
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')


def show_question():
    # показать панель вопросов
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    # разблокируем кнопки, сбросим значения после каждого ответа на вопрос
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    # и заблокируем обратно
    RadioGroup.setExclusive(True)


def test():
    # временная функция, которая определяет, какой метод вызывать,
    # в зависимости от текста на кнопке
    if btn_ok.text() == 'Ответить':
        show_result()
    else:
        show_question()


def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_question.setText(question)
    lb_Correct.setText(right_answer)
    show_question()

# создаём приложение, главное окно
app = QApplication([])
window = QWidget()
window.resize(400, 400)
window.setWindowTitle('MemoryCard')

# интерфейс
lb_question = QLabel('В каком году основана Москва?')
btn_ok = QPushButton('Ответить')

# группа на экране с переключателем ответов
RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn1 = QRadioButton('1350')
rbtn2 = QRadioButton('1147')
rbtn3 = QRadioButton('1861')
rbtn4 = QRadioButton('925')
# поместим все кнопки в список для более удобного управления
answers = [rbtn1, rbtn2, rbtn3, rbtn4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
# окно, всплывающее после выбора варианта ответа:
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет здесь')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)

# размещаем виджеты на линиях
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
# кнопки размещаем на двух вертикальных линиях
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
# вертикальные линии размещаем на горизонтальной
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
# горизонтальную линию закрепляем в группе кнопок
RadioGroupBox.setLayout(layout_ans1)

'''панель с ответом'''
layout_line1 = QHBoxLayout()  # вопрос
layout_line2 = QHBoxLayout()  # варианты ответов/результат теста
layout_line3 = QHBoxLayout()  # кнопка "ответить"

layout_line1.addWidget(lb_question, alignment=Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()  # главный вертикальный лэйаут
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_line3.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_line3.addStretch(1)
layout_card.setSpacing(5)  # добавить пробелы между содержимым
# подключим кнопку:
btn_ok.clicked.connect(test)

window.setLayout(layout_card)
window.show()
app.exec()
