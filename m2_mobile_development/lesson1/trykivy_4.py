# обработка события "нажали на кнопку"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


def tst():
    print('KUKU!')


class MyApp(App):
    def build(self):
        txt = Label(text='Это надпись')
        btn = Button(text='Это кнопка')
        btn.on_press = tst
        # метод on_press объекта btn стал равен функции tst
        # то есть вызов bts
        # метод с именем on_press вызывается автоматически при нажатии на кнопку

        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout


MyApp().run()  # программа отслеживает нажатие на кнопку и печатает соотв. текст.
