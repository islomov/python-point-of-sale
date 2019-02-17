from ..utils.position import WinPosition
from .base import Widget
import tkinter as tk


class TextField(Widget):
    __slots__ = ['position', 'caption', 'show', '__has_error', 'bg', 'inner_frame', 'required']
    type = 'text_field'

    def __init__(self, position: WinPosition, *args, required=False, caption=None, bg='#ECECEC',
                 style=None, width=150, height=28, show=None, **kwargs):
        assert isinstance(position, WinPosition)
        self.bg = bg
        self.position = position
        self.required = required
        self.style = style
        self.caption = caption
        self.position.height = height
        self.position.width = width
        self.show = show
        self.__has_error = False
        self.inner_frame = NotImplemented

    def set_style(self, widget):
        widget['border_width'] = 2

    def on_create(self, *args, **kwargs):
        self.inner_frame = tk.Frame(self.frame, bg=self.bg)
        if self.caption:
            label = tk.Label(self.inner_frame, text=self.caption, bg=self.bg)
            label.pack(side=tk.LEFT)
        text = tk.Entry(self.inner_frame)
        if self.show:
            text.configure(show=self.show)
        text.pack(side=tk.RIGHT)
        self.inner_frame.place(**self.position())
        return text

    @property
    def is_valid(self):
        return not self.__has_error

    @property
    def text(self):
        widget: tk.Entry = getattr(self.frame, self._widget_name)
        value = widget.get()
        value, self.__has_error = self.validate(value)
        if not self.is_valid:
            widget.config(highlightbackground='red')
        else:
            widget.config(highlightbackground='white')
        return value

    def validate(self, value):
        if self.required:
            return value, not bool(value)
        return value, False

    def insert(self, text):
        widget: tk.Entry = getattr(self.frame, self._widget_name)
        widget.delete(0, tk.END)
        widget.insert(0, text)

    def clear(self):
        widget: tk.Entry = getattr(self.frame, self._widget_name)
        widget.delete(0, tk.END)

    def change_position(self, x, y):
        self.inner_frame.place(x, y)


class IntegerField(TextField):
    def validate(self, value):
        try:
            value = int(value)
            if self.required:
                return value, not bool(value)
            return value, False
        except ValueError:
            return value, True


class FloatField(TextField):
    def validate(self, value):
        try:
            float(value)
            float(value)
            value = float(value)
            if self.required:
                return value, not bool(value)
            return value, False
        except ValueError:
            return value, True
