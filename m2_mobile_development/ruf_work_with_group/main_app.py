from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

age = 7
name = ''

p1, p2, p3 = 0, 0, 0


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
        self.manager.current = 'pulse1'


class PulseScr(Screen):
    """2-й экран, запрашивает пульс перед началом упражнения"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # виджеты экрана:
        instr = Label(text=txt_test1)
        lbl_result = Label(text='Введите результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        self.btn = Button(text='Продолжить:', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        # размещаем виджеты на линиях (лэйаутах)
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        # главный вертикальный лэйаут
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        # добавляем главный лэйаут на экран
        self.add_widget(outer)

    def next(self):
        """описывает нажатие на кнопку"""
        global p1
        # получаем переменные name, age и переключаемся на следующий экран
        p1 = int(self.in_result.text)
        self.manager.current = 'sits'


class CheckSits(Screen):
    """3-й экран, отвечает за приседания"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # виджеты экрана:
        instr = Label(text=txt_sits)
        self.btn = Button(text='Продолжить:', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        # размещаем виджеты на линиях (лэйаутах)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
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
        # виджеты экрана:
        instr = Label(text=txt_test3)
        lbl_result1 = Label(text='Результат:', halign='right')
        lbl_result2 = Label(text='Результат после отдыха:', halign='right')

        self.in_result1 = TextInput(text='0', multiline=False)
        self.in_result2 = TextInput(text='0', multiline=False)

        self.btn = Button(text='Продолжить:', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
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
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        # добавляем главный лэйаут на экран
        self.add_widget(outer)

    def next(self):
        """описывает нажатие на кнопку"""
        global p2, p3
        # получаем переменные p2, p3 и переключаемся на следующий экран
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
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