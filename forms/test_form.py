from pywindow.frames.base import BaseFrame
from pywindow.utils.position import WinPosition
from pywindow.widgets import Button
from pywindow.widgets.text_field import IntegerField


class Frame(BaseFrame):
    integer_field = IntegerField(WinPosition(0, 0), caption='Username:', width=200)
    check_button = Button('Check', 'check', WinPosition(0, 20))

    def check(self):
        print(self.integer_field.text)
