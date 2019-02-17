def get_line_equation(beginning_point, ending_point):
    """
    Y = Slope*X + b
    get_slope -> Slope
    get_b -> b
    """

    def get_slope():
        return (beginning_point.y - ending_point.y) / (beginning_point.x - ending_point.x)

    def get_b(s):
        return beginning_point.y - beginning_point.x * s

    slope = get_slope()
    b = get_b(slope)
    return slope, b


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return self.x, self.y

    def __str__(self):
        return '{},{}'.format(self.x, self.y)

    def __repr__(self):
        return '{},{}'.format(self.x, self.y)
