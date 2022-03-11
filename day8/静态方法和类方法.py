'''
实例方法：类中默认定义的方法，就是实例方法

类方法：使用@classmethod 装饰的方法，称为类方法，第一个参数是cls,代表的是类对象
什么情况定义为实例方法，什么情况定义为类方法？
1、如果在方法中使用了实例属性，那么该方法必须定义为实例方法
2、前提:不需要使用实例属性，需要使用类属性，可以将这个方法定义为类方法

'''

class Dog(object):
    class_name='狗类'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def play(self): # 实例方法
        print(f'小狗{self.name}在快乐的玩耍。。。')

    # def get_class_name(self):   #实例方法，因为没有使用到实例属性，可以定义为类属性
    #     return self.class_name
    @classmethod
    def get_class_name(cls):
        return cls.class_name

dog=Dog('大黄',2)
dog.play()
print(dog.get_class_name())

print(Dog.get_class_name())

'''静态方法'''
# 需要通过修饰器 @staticmethod 修饰，静态方法不需要定义参数，可以通过对象和类来访问
# 不需要使用实例属性，也不需要使用类属性，此时可以将该方法定义为静态方法
class People(object):
    country='china'

    @staticmethod
    def get_country():  # 定义静态方法
        return People.country

p=People()
# 通过实例对象访问
print(p.get_country())
# 通过类访问
print(People.get_country())




