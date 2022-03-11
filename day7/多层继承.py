class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"

    def make_cake(self):
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)


class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

class Prentice(School, Master):  # 多继承，继承了多个父类
    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"
        self.money = 10000  # 亿美金

    def make_cake(self):
        self.__init__() # 执行本类的__init__方法，做属性初始化 self.kongfu = "猫氏...."
        print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

        Master.__init__(self)  # 调用了父类Master的__init__方法 self.kongfu = "古法...."
        Master.make_cake(self)  # 调用了父类Master的实例方法

        School.__init__(self)  # 调用了父类School的__init__方法 self.kongfu = "现代...."
        School.make_cake(self)  # 调用父类School的实例方法，

'''多层继承'''
# 继承自Prentice，既包含了继承自Prentice自身，还有Master和School的
class PresentPrentice(Prentice):
    pass

pp=PresentPrentice()
pp.make_cake()

print(pp.money)