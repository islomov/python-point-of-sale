import tkinter as tk
from .base import Widget
from ..utils.position import WinPosition


class Label(Widget):
    __slots__ = ['text', 'position', 'style', 'bg']
    type = 'label'

    def __init__(self, text, position: WinPosition, *args, bg='#ECECEC', **kwargs):
        super(Label, self).__init__(*args, **kwargs)
        self.text = text
        self.bg = bg
        assert isinstance(position, WinPosition)
        self.position = position

    def on_create(self, *args, **kwargs):
        label = tk.Label(self.frame, bg=self.bg)
        label['text'] = self.text
        label.place(**self.position())
        return label

    def set_style(self, widget):
        for key, value in self.style.items():
            widget[key] = value

    def set(self, text):
        label = getattr(self.frame, self._widget_name)
        label.config(text=text)

    def change_position(self, x, y):
        widget: tk.Label = getattr(self.frame, self._widget_name)
        widget.place(**dict(x=x, y=y))
