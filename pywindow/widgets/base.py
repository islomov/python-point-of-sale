class Widget(object):
    __slots__ = ['frame', 'name', 'style', '_widget_name']
    type = 'widget'

    class Listeners:
        on_select = '<ButtonRelease>'
        on_select_double_click = '<Double-Button>'

    def __call__(self, name, frame, *args, style=None, **kwargs):
        self.frame = frame
        self.name = name
        self._widget_name = f'widget_{name}'
        self.style = style
        widget = self.on_create(*args, **kwargs)
        if getattr(self, 'style') and isinstance(style, dict):
            self.set_style(widget)
        self.on_widget_created(widget, *args, **kwargs)

    def set_style(self, widget):
        pass

    def bind(self, action: str, func, **kwargs):
        widget = getattr(self.frame, self._widget_name)
        widget.bind(action, lambda x: func(self, **kwargs))

    def change_position(self, x, y):
        raise NotImplemented

    def on_create(self, *args, **kwargs):
        raise NotImplemented

    def on_widget_created(self, widget, *args, **kwargs):
        setattr(self.frame, self._widget_name, widget)
