class Position(object):
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def position(self) -> dict:
        return dict(x=self.x, y=self.y)


class WinPosition(Position):
    __slots__ = ['x', 'y', 'height', 'width']

    def __init__(self, x, y, width=0, height=0):
        super(WinPosition, self).__init__(x, y)
        self.width = width
        self.height = height

    def __call__(self, *args, **kwargs) -> dict:
        return dict(x=self.x, y=self.y, width=self.width, height=self.height)
