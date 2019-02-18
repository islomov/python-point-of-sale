from tkinter import messagebox

from forms.checque_form import ChequeForm
from forms.order_item_form import OrderItemForm
from pywindow.frames.base import BaseFrame
from pywindow.utils.position import WinPosition
from pywindow.widgets import Label, TextField, Button


class MainForm(BaseFrame):
    title = Label('Welcome to Store Management System', WinPosition(162, 40, 500, 29))
    staff_name = TextField(WinPosition(30, 100), required=True, caption='Staff name:', width=290, height=30)
    customer_id = TextField(WinPosition(30, 145), required=True, caption='Customer ID:', width=290, height=30)
    adding_label = Label('Add more products', WinPosition(30, 200, 145, 30))
    product_adding_button = Button('+', 'add_product', WinPosition(190, 200), width=60, height=30)
    product_name_label = Label('Product Name', WinPosition(30, 245, 120, 30))
    product_code_label = Label('Product Code', WinPosition(190, 245, 120, 30))
    price_label = Label('Price($)', WinPosition(350, 245, 120, 30))
    quantity_label = Label('Quantity', WinPosition(510, 245, 120, 30))
    points_label = Label('Points', WinPosition(665, 245, 120, 30))
    print_button = Button('Print', 'print_order', WinPosition(30, 286), width=90, height=30)
    close_button = Button('Close', 'close', WinPosition(145, 286), width=90, height=30)

    __stack_point = 285
    __order_items = list()

    def add_product(self):
        order_item = OrderItemForm.get_instance(self, WinPosition(30, self.__stack_point, 754, 62))
        order_item.place()
        self.__order_items.append(order_item)
        self.print_button.change_position(30, self.__stack_point + 83)
        self.close_button.change_position(145, self.__stack_point + 83)
        self.__stack_point += 62

    def print_order(self):
        order_items = list()
        has_errors = list()
        staff_name = self.staff_name.text
        customer_id = self.customer_id.text
        has_errors += [not self.staff_name.is_valid, not self.customer_id.is_valid]
        for order_item in self.__order_items:
            order_item, has_error = order_item.get_data()
            order_items.append(order_item)
            has_errors.append(has_error)
        if any(has_errors):
            messagebox.showerror('Error', 'There are some errors on filling fields')
        else:
            # TODO: SARDOR, order_items should be passed
            cheque_form = ChequeForm.get_instance('Cheque', True)
            cheque_form.show_frame(staff_name=staff_name, customer_id=customer_id, order_items=order_items)

    def close(self):
        self.quit()

    class Meta:
        width = 800
        height = 600
        x_offset = 10
        y_offset = 10
        styles = dict()
