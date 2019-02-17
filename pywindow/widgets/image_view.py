import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

from pywindow.utils.position import WinPosition
from .base import Widget
import cv2


class ImageView(Widget):
    __slots__ = ['position', 'height', 'width']
    type = 'image_view'

    def __init__(self, position: WinPosition, *args, width=100, height=100, **kwargs):
        assert isinstance(position, WinPosition)
        position.width = width
        position.height = height
        self.position = position
        self.height = height
        self.width = width

    def on_create(self, *args, **kwargs):
        image_view = tk.Label(self.frame)
        image_view.place(**self.position())
        return image_view

    def load_image(self, image):
        image = cv2.resize(image, (self.width, self.height))
        image = ImageTk.PhotoImage(Image.fromarray(image))
        image_view: tk.Label = getattr(self.frame, self._widget_name)
        image_view.configure(image=image)
        image_view.image = image
