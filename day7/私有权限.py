'''
私有权限：在属性名和方法名 前面 加上两个下划线 __
类的私有属性 和 私有方法，都不能通过对象直接访问，但是可以在本类内部访问；
类的私有属性 和 私有方法，都不会被子类继承，子类也无法访问；
私有属性 和 私有方法 往往用来处理类的内部事情，不通过对象处理，起到安全作用。
'''
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


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"
        # 私有属性，可以在类内部通过self调用，但不能通过对象访问
        self.__money = 10000

    # 私有方法，可以在类内部通过self调用，但不能通过对象访问
    def __print_info(self):
        print(self.kongfu)
        print(self.__money)

        Master.__init__(self)
        Master.make_cake(self)

        School.__init__(self)
        School.make_cake(self)
    def get_money(self):
        return self.__money
    def set_money(self,num):
        self.__money=num

class PresentPrentice(Prentice):
    pass

damao=Prentice()
# 对象不能访问私有权限的属性和方法
# print(damao.__money)
# damao.__print_info()


pp=PresentPrentice()
# 子类不能继承父类私有权限的属性和方法
# print(pp.__money)
# pp.__print_info()

'''修改私有属性的值'''
# 如果要修改对象的属性值，有两种方法
# 对象名.属性名 = 数据 ----> 直接修改
# 对象名.方法名() ----> 间接修改
# 私有属性不能直接访问，所以无法通过第一种方式修改，
# 一般的通过第二种方式修改私有属性的值：定义一个可以调用的公有方法，
# 在这个公有方法内访问修改。

# 可以通过访问公有方法set_money()来修改私有属性的值
damao.set_money(100)
# 可以通过访问公有方法get_money()来获取私有属性的值
print(damao.get_money())


