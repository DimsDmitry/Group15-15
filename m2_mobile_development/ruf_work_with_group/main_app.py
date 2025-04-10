from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test
from seconds import Seconds
from sits import Sits

age = 7
name = ''

p1, p2, p3 = 0, 0, 0

win_color = (0.6, 0.18, 0.75, 0.8)
Window.clearcolor = win_color  # Назначаем цвет экрана.
btn_color = (0.89, 0.2, 0.54, 1)  # Цвет кнопки. Применим отдельно к каждой кнопке

def check_int(str_num):
    """возвращает число или False, если строка не конвертируется в число"""
    try:
        return int(str_num)
    except ValueError:
        return False


class InstrScreen(Screen):
    """главный экран с инструкцией, запрашивает имя и возраст"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # виджеты экрана:
        instr = Label(text=txt_instruction)
        lbl1 = Label(text='Введите имя:', halign='right')
        lbl2 = Label(text='Введите возраст:', halign='right')
        self.in_name = TextInput(multiline=False)
        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Начать:', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color  # Цвет кнопки.
        # привязываем к кнопке метод, переключающий на след. экран
        self.btn.on_press = self.next
        # размещаем виджеты на линиях (лэйаутах)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        # главный вертикальный лэйаут
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        # добавляем главный лэйаут на экран
        self.add_widget(outer)

    def next(self):
        """описывает нажатие на кнопку"""
        global name, age
        # получаем переменные name, age и переключаемся на следующий экран
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if not age or age < 7:
            # проверяем, ввели ли мы возраст верно - это должно быть число не меньше 7
            age = 7
            self.in_age.text = str(age)
        else:
            # если ввели верно - переход на след. экран
            self.manager.current = 'pulse1'


class PulseScr(Screen):
    """2-й экран, запрашивает пульс перед началом упражнения"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # виджеты экрана:
        self.next_screen = False
        instr = Label(text=txt_test1)
        # таймер, привязка к логическому свойству
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        # кнопки, окна для ввода текста
        lbl_result = Label(text='Введите результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        # выключим окно для ввода текста пока не прошел таймер
        self.in_result.set_disabled(True)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color  # Цвет кнопки.

        self.btn.on_press = self.next
        # размещаем виджеты на линиях (лэйаутах)
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        # главный вертикальный лэйаут
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        # добавляем главный лэйаут на экран
        self.add_widget(outer)

    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'


    def next(self):
        """описывает нажатие на кнопку"""
        if not self.next_screen:
            # блокируем кнопку пока не прошёл таймер
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            # таймер окончил работу - получаем значения пульса и идём на след. экран
            global p1
            # получаем переменную p1
            p1 = check_int(self.in_result.text)
            if not p1 or p1 <= 0:
                # проверяем, ввели ли мы пульс верно - это должно быть число больше 0
                p1 = 0
                self.in_result.text = str(p1)
            else:
                # если ввели верно - переход на след. экран
                self.manager.current = 'sits'


class CheckSits(Screen):
    """3-й экран, отвечает за приседания"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # виджеты экрана:
        instr = Label(text=txt_sits)
        self.lbl_sits = Sits(30)  # счётчик приседаний
        self.btn = Button(text='Продолжить:', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color  # Цвет кнопки.
        self.btn.on_press = self.next
        # размещаем виджеты на линиях (лэйаутах)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(self.lbl_sits)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        """переключаемся на следующий экран"""
        self.manager.current = 'pulse2'


class PulseScr2(Screen):
    """4-й экран, запрашивает пульс после приседаний и после отдыха"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stage = 0  # СТАДИЯ ТАЙМЕРА
        self.next_screen = False  # флаг переключения экрана
        # виджеты экрана:
        instr = Label(text=txt_test3)
        lbl_result1 = Label(text='Результат:', halign='right')
        lbl_result2 = Label(text='Результат после отдыха:', halign='right')
        self.lbl_sec = Seconds(15)  # таймер
        self.lbl_sec.bind(done=self.sec_finished)  # связываем с логическим свойством
        self.lbl1 = Label(text='Считайте пульс')
        self.in_result1 = TextInput(text='0', multiline=False)
        self.in_result2 = TextInput(text='0', multiline=False)
        # блокируем окна ввода
        self.in_result1.set_disabled(True)
        self.in_result2.set_disabled(True)

        self.btn = Button(text='Начать:', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color  # Цвет кнопки.
        self.btn.on_press = self.next
        # размещаем виджеты на линиях (лэйаутах)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)
        # главный вертикальный лэйаут
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl1)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        # добавляем главный лэйаут на экран
        self.add_widget(outer)

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            # закончился очередной отсчёт таймера - проверяем какая сейчас стадия
            if self.stage == 0:
                # закончили первый подсчёт, отдыхаем
                self.stage = 1
                self.lbl1.text = 'Отдыхайте'
                # перезапускаем таймер, открываем первое окно для ввода
                self.lbl_sec.restart(30)
                self.in_result1.set_disabled(False)
            elif self.stage == 1:
                # закончили отдых в 30 сек, считаем пульс снова
                self.stage = 2
                self.lbl1.text = 'Считайте пульс'
                self.lbl_sec.restart(15)  # запускаем повторный подсчёт пульса
            elif self.stage == 2:
                # финал подсчёта, переключаем на след. экран
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False) # разблокируем второе окно ввода и кнопку
                self.btn.text = 'Завершить'
                self.next_screen = True

    def next(self):
        """описывает нажатие на кнопку"""
        if not self.next_screen:
            # блокируем кнопку пока не прошёл таймер
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2, p3
            # получаем переменные p2, p3, проверяем чтобы они были числом больше 0
            # и переключаемся на следующий экран
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)
            if not p2:
                p2 = 0
                self.in_result1.text = str(p2)
            elif not p3:
                p3 = 0
                self.in_result2.text = str(p3)
            else:
                # если ввели верно - переход на след. экран
                self.manager.current = 'result'


class Result(Screen):
    """5-й экран, выводит результат тестирования"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = Label(text='')
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        # при открытии экрана вызываем метод self.before
        self.on_enter = self.before

    def before(self):
        """вызывает функцию для подсчёта индекса Руфье и выводит результат"""
        self.instr.text = name + '\n' + test(p1, p2, p3, age)


class HeartCheck(App):
    """приложение Тест Руфье, класс-наследник от App"""

    def build(self):
        sm = ScreenManager()
        # создаём менеджер экранов, добавляем все экраны
        sm.add_widget(InstrScreen(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm


# создаём экземпляр приложения, запускаем его
app = HeartCheck()
app.run()
