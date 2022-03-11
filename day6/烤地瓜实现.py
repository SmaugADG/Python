class Potato(object):
    def __init__(self):
        self.status = '生的'
        self.total_time = 0
        self.name_list = []

    def cook(self, time):
        self.total_time += time
        if self.total_time < 3:
            self.status = '生的'
        elif self.total_time < 6:
            self.status = '半生不熟'
        elif self.total_time < 8:
            self.status = '熟了'
        else:
            self.status = '烤糊了'

    def add(self, name):
        self.name_list.append(name)

    def __str__(self):
        buf = ','.join(self.name_list)
        if self.name_list:
            return f'地瓜：{self.status},调料：{buf}'
        else:
            return f'地瓜：{self.status}'


potato = Potato()
print(potato)
potato.add('孜然')
potato.cook(4)
print(potato)
potato.cook(3)
potato.add('辣椒')
print(potato)
