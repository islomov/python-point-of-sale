from utils.adapter import Adapter
from ..utils.position import WinPosition
from .base import Widget
import tkinter as tk


class ListBox(Widget):
    __slots__ = ['position', 'width', 'height', '_items', 'adapter']

    def __init__(self, position: WinPosition, *args, width=150, height=250, **kwargs):
        assert isinstance(position, WinPosition)
        self.position = position
        self.position.width = width
        self._items = []
        self.position.height = height
        self.adapter = None

    def on_create(self, *args, **kwargs):
        frame = tk.Frame(self.frame)
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        frame.place(**self.position())
        return listbox

    def insert(self, text):
        listbox: tk.Listbox = getattr(self.frame, self._widget_name)
        listbox.insert(tk.END, text)
        self._items.append(text)

    def delete(self, at_index=tk.END):
        if at_index == -1:
            return
        listbox: tk.Listbox = getattr(self.frame, self._widget_name)
        listbox.delete(at_index)
        self._items.pop(at_index)

    def clear(self):
        listbox: tk.Listbox = getattr(self.frame, self._widget_name)
        listbox.delete(0, tk.END)
        self._items.clear()

    @property
    def selected(self) -> int:
        listbox: tk.Listbox = getattr(self.frame, self._widget_name)
        indexes = listbox.curselection()
        if indexes:
            return indexes[0]
        return -1

    @property
    def items(self):
        return self._items

    def populate(self, adapter: Adapter):
        self.clear()
        self.adapter = adapter
        listbox: tk.Listbox = getattr(self.frame, self._widget_name)
        self._items = adapter.item_list
        for item in self._items:
            listbox.insert(tk.END, item)
