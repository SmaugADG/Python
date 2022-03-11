# 定义父类
class Master(object):
    def __init__(self):
        self.kongfu='古法煎饼果子配方'
    def make_pai(self):
        print('[古法]按照%s制作了一份煎饼果子'%self.kongfu)

class School(object):
    def __init__(self):
        self.kongfu='现代煎饼果子配方'
    def make_pai(self):
        print('[现代]按照%s制作了一份煎饼果子'%self.kongfu)

# 单继承
# 定义子类
class Prentice(Master):
    pass

laoli=Master()
print(laoli.kongfu)
laoli.make_pai()

damao=Prentice()
print(damao.kongfu)
damao.make_pai()

# 多继承
# 1
class Prentice2(School,Master):
    pass

xiaomao=Prentice2()
print(xiaomao.kongfu)
xiaomao.make_pai()

# 2
class Prentice2(Master,School):
    pass

xiaomao=Prentice2()
print(xiaomao.kongfu)
xiaomao.make_pai()

# 如果多个父类拥有同名的属性和方法，则默认使用第一个父类的属性和方法（根据魔法属性mro的顺序来查找）
# 多个父类中不重名的属性和方法，不会有任何影响


'''子类重写父类的同名属性和方法'''
class Prentice3(School,Master):
    # 重写配方
    def __init__(self):
        self.kongfu='猫氏煎饼果子配方'
    # 重写方法
    def make_pai(self):
        print('按照%s制作了一份煎饼果子'%self.kongfu)

sanmao=Prentice3()
print(sanmao.kongfu)
sanmao.make_pai()


'''子类调用父类的方法'''
class Prentice(Master,School):
    # 重写配方
    def __init__(self):
        self.kongfu='猫氏煎饼果子配方'
    # 重写方法
    def make_pai(self):
        print('按照%s制作了一份煎饼果子'%self.kongfu)
# 方法一：父类名.方法名（self,其他参数）
# 如果通过 实例对象.方法名（） ，不需要给self传递实参值
# python解释器会自动将对象作为实参值传递给self形参，
# 如果通过类名.方法名()，python解释器不会自动传递实参值，需要手动给self形参传递实参值
        Master.__init__(self)   # 调用init方法可以调用父类的属性，self就指向了父类
        Master.make_pai(self)
# 方法二:使用super(当前类，self).方法名（参数），会调用当前类的父类中的方法
        School.__init__(self)
        # super()指向第一个父类Master，不会调用School的make_pai()方法
        # super(Prentice, self).make_pai()
        School.make_pai(self)
# 方法三：是方法二的简写 super().方法名（参数）==>super(当前类，self).方法名（参数）
        super().make_pai()  # 多继承的，super() 默认指向第一个父类

damao=Prentice()
print(damao.kongfu)
damao.make_pai()
# 子类的魔法属性__mro__决定了属性和方法的查找顺序,super()默认指向第一个父类,通常用于单继承的多层继承
print(Prentice.__mro__)

