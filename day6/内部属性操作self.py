class Dog(object):
    # self 作为类中方法的第一个形参，不选哟手动传递实参值，
    # 解释器自动调用该方法的对象传递给self，所以self代表的是对象
    # self是默认形参名，可以修改成别的名字，一般建议不修改
    #   def play(my_self):
    def play(self):
        print(f'self:{id(self)}')
        # 调用外部添加的属性 使用self
        print(f'name:{self.name}')  # name:大黄


dog = Dog()
dog.name = '大黄'
dog.play()
