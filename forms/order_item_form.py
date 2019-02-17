from pywindow.utils.position import WinPosition
from pywindow.widgets import TextField
from pywindow.widgets.containter import Container
from pywindow.widgets.text_field import FloatField, IntegerField


class OrderItemForm(Container):
    name = TextField(WinPosition(0, 16), required=True, width=120, height=30)
    code = TextField(WinPosition(160, 16), required=True, width=120, height=30)
    price = FloatField(WinPosition(320, 16), required=True, width=120, height=30)
    quantity = FloatField(WinPosition(480, 16), required=True, width=120, height=30)
    points = IntegerField(WinPosition(634, 16), required=True, width=120, height=30)

    class Meta:
        width = 754
        height = 48
        x_offset = 10
        y_offset = 10
        styles = dict()

    def get_data(self):
        data = dict()
        has_error = False
        for field in [self.name, self.code, self.price, self.quantity, self.points]:
            data.update({field.name: field.text})
            has_error = has_error or not field.is_valid
        return data, has_error
