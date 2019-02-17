class Adapter(object):

    def __init__(self, list_field, pk, data=[]):
        assert list_field and pk
        self.list_field = list_field
        self.pk = pk
        self.data = data
        self._item_list = list()
        self.get_items()

    def get_items(self):
        for item in self.data:
            self._item_list.append(item.get(self.list_field))

    @property
    def item_list(self) -> list:
        return self._item_list

    def get_pk(self, index):
        item = self.data[index]
        return item.get(self.pk)
