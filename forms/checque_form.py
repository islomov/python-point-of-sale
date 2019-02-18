from forms.cheque_order_item import ChequeOrderItem
from pywindow.frames.base import BaseFrame
from pywindow.utils.position import WinPosition
from pywindow.widgets import Label, Button


class ChequeForm(BaseFrame):
    pass
    title = Label('Welcome to Store management system', WinPosition(40, 16, 449, 30))
    staff_name = Label('Staff name', WinPosition(26, 59, 224, 30))
    customer_id = Label('Customer id', WinPosition(27, 102, 224, 30))
    product_name = Label('Product name', WinPosition(27, 183, 128, 30))
    product_code = Label('Product code', WinPosition(165, 183, 128, 30))
    product_price = Label('Price($)', WinPosition(304, 183, 128, 30))
    product_quantity = Label('Quantity', WinPosition(443, 183, 128, 30))
    total = Label('Total:', WinPosition(26, 0, 178, 30))
    total_items = Label('Total Items:', WinPosition(26, 0, 178, 30))
    total_points = Label('Points:', WinPosition(26, 0, 178, 30))
    close_button = Button('Close', 'close', WinPosition(145, 286), width=90, height=30)

    def init(self):
        super(ChequeForm, self).init()

        self.customer_id.set(f"Customer id: {self.data['customer_id']}")
        self.staff_name.set(f"Staff name: {self.data['staff_name']}")

        y_position = 210
        total_items = 0
        points = 0
        total_price = 0
        for order_item in self.data['order_items']:
            form = ChequeOrderItem.get_instance(self, WinPosition(27, y_position, 544, 56))
            form.name.set(order_item['name'])
            form.code.set(order_item['code'])
            form.price.set(order_item['price'])
            form.quantity.set(order_item['quantity'])
            total_items += order_item['quantity']
            points += order_item['points']
            total_price += (order_item['quantity'] * order_item['price'])
            form.place()
            y_position += 56
        self.total.change_position(10, y_position)
        self.total.set(f'Total: {total_price}$')

        y_position += 40
        self.total_items.change_position(10, y_position)
        self.total_items.set(f'Total Items: {total_items}')
        y_position += 40
        self.total_points.change_position(10, y_position)
        self.total_points.set(f'Total points: {points}')
        y_position += 40
        self.close_button.change_position(500, y_position)

    def close(self):
        self.master.destroy()

    class Meta:
        width = 600
        height = 700
        x_offset = 10
        y_offset = 10
        styles = dict()
