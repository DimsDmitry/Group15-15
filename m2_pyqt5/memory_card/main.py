from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *


class Question:
    # класс для хранения вопроса
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


# создаём вопросы, оформляем их в список
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский')
q2 = Question('Какого цвета нет на флаге России?', 'Зелёный', 'Белый', 'Синий', 'Красный')
q3 = Question('Какой рукой мешают чай?', 'Ложкой', 'Левой', 'Правой', 'Двумя')
q4 = Question('Год основания Москвы', '1147', '889', '1251', '955')

question_list = [q1, q2, q3, q4]


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


def ask(q: Question):
    '''записывает значения вопроса и ответов в нужные виджеты, перемешивает ответы'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    '''установим текст в надпись "результат" и покажем нужную панель'''
    lb_Result.setText(res)
    show_result()


def check_answer():
    """проверяет вариант ответа, показывает панель ответов"""
    if answers[0].isChecked():
        # правильный ответ
        show_correct('Правильно!')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')


def next_question():
    """задаёт следующий вопрос из списка"""
    window.cur_question += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0  # если список вопросов кончился - идём сначала
    q = question_list[window.cur_question]  # берём вопрос
    ask(q)  # задаём его


def click_OK():
    """определяет, надо показать другой вопрос или проверить ответ на этот"""
    if btn_ok.text() == 'Ответить':
        check_answer()  # проверка ответа
    else:
        next_question()  # следующий вопрос


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
rbtn1 = QRadioButton('Вариант 1')
rbtn2 = QRadioButton('Вариант 2')
rbtn3 = QRadioButton('Вариант 3')
rbtn4 = QRadioButton('Вариант 4')
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

window.cur_question = -1
# подключим кнопку:
btn_ok.clicked.connect(click_OK)
next_question()

window.setLayout(layout_card)
window.show()
app.exec()
