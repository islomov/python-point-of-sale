from ..utils.position import WinPosition
from .base import Widget
import tkinter as tk


class Button(Widget):
    __slots__ = ['text', 'func', 'position']
    type = 'button'

    def __init__(self, text, func, position: WinPosition, *args, style=None, width=150, height=28, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.text = text
        self.func = func
        self.style = style
        assert isinstance(position, WinPosition)
        position.width = width
        position.height = height
        self.position = position

    def on_create(self, *args, **kwargs):
        button = tk.Button(self.frame)
        button['text'] = self.text
        func = getattr(self.frame, self.func, None)
        assert func, f'Function {self.func} is not defined in window'
        button['command'] = func
        button.place(**self.position())
        return button

    def change_position(self, x, y):
        widget: tk.Button = getattr(self.frame, self._widget_name)
        widget.place(**dict(x=x, y=y))
