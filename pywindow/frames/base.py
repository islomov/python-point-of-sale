import tkinter as tk
from copy import deepcopy
from tkinter import ttk

from pywindow import root
from pywindow.widgets.base import Widget


class BaseFrame(ttk.Frame):
    __slots__ = ['_fields', 'data']

    def __init__(self, master, *args, title=None, **kwargs):
        super().__init__(master)
        master.geometry(f'{self.Meta.width}x{self.Meta.height}+{self.Meta.x_offset}+{self.Meta.y_offset}')
        self.master = master
        self.place(x=0, y=0, width=self.Meta.width, height=self.Meta.height)
        if title:
            self.master.title(title)
        else:
            self.master.title('Form')
        self.pack(fill=tk.BOTH, expand=1)
        self.data = dict()

    @classmethod
    def get_instance(cls, title=None, in_new_screen=False):
        if in_new_screen:
            frame = cls(tk.Tk(), title=title)
        else:
            frame = cls(root, title=title)
        if frame.is_valid():
            frame.set_styles()
            frame.create_widgets()
            frame.on_bind()
            return frame
        return None

    def is_valid(self):
        return True

    def on_bind(self):
        pass

    def init(self):
        pass

    def set_styles(self):
        styles = getattr(self, 'styles', dict())
        self.Meta.styles = styles

    def __get_widgets(self):
        widgets = dict()
        for key, widget in self.__class__.__dict__.items():
            if isinstance(widget, Widget):
                widget_instance = deepcopy(widget)
                widgets.update({key: widget_instance})
                setattr(self, key, widget_instance)
        self._fields = widgets

    def create_widgets(self):
        self.__get_widgets()
        self.__create_widgets()

    def __create_widgets(self):
        for key, value in self.fields.items():
            style = self.Meta.styles.get(value.type, None)
            value(key, self, style=style)

    @property
    def fields(self) -> dict:
        return self._fields

    def show_frame(self, **kwargs):
        self.data = kwargs
        self.place(x=0, y=0, width=self.Meta.width, height=self.Meta.height)
        self.tkraise()
        self.init()

    class Meta:
        width = 500
        height = 500
        x_offset = 10
        y_offset = 10
        styles = dict()
