from copy import deepcopy

from pywindow.utils.position import WinPosition
from pywindow.widgets.base import Widget
import tkinter as tk


class Container(object):
    __slots__ = ['position', 'master', 'frame', '__has_error', 'bg', '_fields']

    def __init__(self, master, *_, bg='#ECECEC', position: WinPosition = None, **__):
        assert isinstance(position, WinPosition)
        self.bg = bg
        self.master = master
        self.position = position
        self.__has_error = False
        self.frame = tk.Frame(master, bg=self.bg)

    @classmethod
    def get_instance(cls, root, position: WinPosition, place=False):
        frame = cls(root, position=position)
        if frame.is_valid():
            frame.create_widgets()
            frame.on_bind()
            if place:
                frame.place()
            return frame
        return None

    def place(self):
        self.frame.place(**self.position())

    def is_valid(self):
        return True

    def on_bind(self):
        pass

    def create_widgets(self):
        self.__get_widgets()
        self.__create_widgets()

    def __get_widgets(self):
        widgets = dict()
        for key, widget in self.__class__.__dict__.items():
            if isinstance(widget, Widget):
                widget_instance = deepcopy(widget)
                widgets.update({key: widget_instance})
                setattr(self, key, widget_instance)
        self._fields = widgets

    def __create_widgets(self):
        for key, value in self.fields.items():
            style = self.Meta.styles.get(value.type, None)
            value(key, self.frame, style=style)

    @property
    def fields(self) -> dict:
        return self._fields

    class Meta:
        width = 500
        height = 500
        x_offset = 10
        y_offset = 10
        styles = dict()
