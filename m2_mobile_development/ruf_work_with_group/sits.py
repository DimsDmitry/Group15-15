from kivy.uix.label import Label


class Sits(Label):
    """класс для счётчика приседаний, наследник Label"""
    def __init__(self, total, **kwargs):
        self.total = total  # общее кол-во приседаний
        self.current = 0  # кол-во сделанных приседаний
        my_text = 'Осталось приседаний:' + str(self.total)
        super().__init__(text=my_text, **kwargs)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        my_text = 'Осталось приседаний:' + str(remain)
        self.text = my_text
