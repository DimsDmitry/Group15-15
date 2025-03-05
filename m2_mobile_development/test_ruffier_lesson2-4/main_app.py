from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

age = 7
name = ''
p1, p2, p3 = 0, 0, 0


class InstrScr(Screen):
    """Начальный экран - выводится краткая информация о тесте, запрашивается возраст и имя"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        lbl1 = Label(text='Введите имя:')
        lbl2 = Label(text='Введите возраст:')
        self.in_name = TextInput(multiline=False)
        self.in_age = TextInput(multiline=False)
        self.btn = Button(text='Начать', size_hint=(.3, .2), pos_hint={'center_x': 0.5})
        # Создаём лэйауты, размещаем виджеты
        # по горизонтали:
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        # по вертикали:
        main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)
        # не забываем подключить кнопку:
        self.btn.on_press = self.next

    def next(self):
        """при нажатии на кнопку считываем значение имени и возраста, переключаем на след. экран"""
        global name
        name = self.in_name.text
        self.manager.current = 'pulse1'


class PulseScr(Screen):
    """Экран 2 - запрашивается пульс в покое"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test1)
        lbl_result = Label(text='Введите результат:')
        self.btn = Button(text='Продолжить', size_hint=(.3, .2), pos_hint={'center_x': 0.5})
        self.in_result = TextInput(text='0', multiline=False)
        # Создаём лэйауты, размещаем виджеты
        # по горизонтали:
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        # по вертикали:
        main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(line)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)
        # не забываем подключить кнопку:
        self.btn.on_press = self.next

    def next(self):
        """при нажатии на кнопку считываем значение пульса p1, переключаем на след. экран"""
        global p1
        p1 = int(self.in_result.text)
        self.manager.current = 'sits'


class CheckSits(Screen):
    """Экран 3 - пользователю предлагается выполнить приседания"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)
        self.btn = Button(text='Продолжить', size_hint=(.3, .2), pos_hint={'center_x': 0.5})
        # Создаём лэйауты, размещаем виджеты
        main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)
        # не забываем подключить кнопку:
        self.btn.on_press = self.next

    def next(self):
        """при нажатии на кнопку переключаем на след. экран"""
        self.manager.current = 'pulse2'


class PulseScr2(Screen):
    """Экран 4 - запрашивается пульс после приседания, затем - пульс после отдыха"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3)
        lbl_result1 = Label(text='Результат:')
        lbl_result2 = Label(text='Результат после отдыха:')
        self.in_result1 = TextInput(text='0', multiline=False)
        self.in_result2 = TextInput(text='0', multiline=False)
        self.btn = Button(text='Завершить', size_hint=(.3, .2), pos_hint={'center_x': 0.5})
        # Создаём лэйауты, размещаем виджеты
        # по горизонтали:
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)
        # по вертикали:
        main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        main_line.add_widget(instr)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)
        # не забываем подключить кнопку:
        self.btn.on_press = self.next

    def next(self):
        """при нажатии на кнопку считываем значение пульса p2 и p3, переключаем на след. экран"""
        global p2, p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
        self.manager.current = 'result'


class Result(Screen):
    """Экран 5 - выводится результат исследования"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Создаём лэйауты, создаём и размещаем виджеты
        self.main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = Label(text='')
        self.main_line.add_widget(self.instr)
        self.add_widget(self.main_line)
        # при запуске будет вызываться метод test(), считаться индекс и выводиться вся информация
        self.on_enter = self.calculator

    def calculator(self):
        global name
        self.instr.text = name + '\n' + test(p1, p2, p3, age)


class HeartCheck(App):
    """Наследник класса App - приложение HeartCheck"""

    def build(self):
        """создаём Screen Manager, объединяем в него все экраны"""
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm


app = HeartCheck()
app.run()
