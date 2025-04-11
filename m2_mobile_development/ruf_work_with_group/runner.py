from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout

class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)


    def __init__(self):
        pass

    def start(self):
        pass

    def next(self, widget, step):
        pass