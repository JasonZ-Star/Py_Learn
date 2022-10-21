# Owner Feng
# Time 2022/10/21 10:20


class Record:
    def __init__(self, data, order_id, money, province):
        self.data = data
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f'{self.data}, {self.data}, {self.money}, {self.province}'