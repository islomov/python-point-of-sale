from pywindow.utils.position import WinPosition
from pywindow.widgets import TextField, Label
from pywindow.widgets.containter import Container
from pywindow.widgets.text_field import FloatField, IntegerField


class ChequeOrderItem(Container):
    name = Label('a', WinPosition(0, 13, 120, 30))
    code = Label('a', WinPosition(140, 13, 120, 30))
    price = Label('a', WinPosition(278, 13, 120, 30))
    quantity = Label('a', WinPosition(417, 13, 120, 30))

    class Meta:
        width = 544
        height = 56
        x_offset = 10
        y_offset = 10
        styles = dict()
