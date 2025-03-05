from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView


class ScrButton(Button):
    """класс-наследник кнопки для создания кнопки-переключателя
    на другой экран"""

    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        """переключает пользователя на другой экран"""
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.curren = self.goal


class MainScr(Screen):
    """наследник класса Screen. Главный экран, с него переключаемся на все остальные"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        hl = BoxLayout()  # главный лэйаут
        txt = Label(text='Выбери экран')
        # создаём кнопки ScrButton
        btn1 = ScrButton(self, direction='down', goal='first', text='1')
        btn2 = ScrButton(self, direction='left', goal='second', text='2')
        btn3 = ScrButton(self, direction='up', goal='third', text='3')
        btn4 = ScrButton(self, direction='right', goal='fourth', text='4')
        # добавляем их на вертикальную линию
        vl.add_widget(btn1)
        vl.add_widget(btn2)
        vl.add_widget(btn3)
        vl.add_widget(btn4)
        # добавляем всё на главную линию
        hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)


class FirstScr(Screen):
    """наследник класса Screen"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn = Button(text='Выбор: 1', size_hint=(.5, 1), pos_hint={'left': 0})
        btn_back = ScrButton(self, direction='Up', goal='main', text='Назад', size_hint=(.5, 1), pos_hint={'right': 1})
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)


class SecondScr(Screen):
    """наследник класса Screen"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ThirdScr(Screen):
    """наследник класса Screen"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        pass


class FourthScr(Screen):
    """наследник класса Screen"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        pass


class MyApp(App):
    """наследник класса App, экземпляр приложения на который мы добавляем все виджеты (экраны)"""

    def build(self):
        # добавляем экраны
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        return sm


app = MyApp()
app.run()
