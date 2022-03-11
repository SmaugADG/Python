# python中，一种以两个下划线开始和结束的方法，
# 在满足某种特定条件的情况下自动调用程为魔法方法

# __init__()
#   调用时机：在创建按对象后，会立即调用
#   作用：1.用来给对象添加属性，给对象属性添加方法(构造方法)
#   2.代码的业务需求，没创建一个对象需要执行的业务可以写在里面

class Dog(object):
    def __init__(self,name,age):
        # print(f'__str__():调用')
        self.age=age
        self.name=name

    def __str__(self):
        # print(f'__str__():调用')
        # 必须返回一个字符串
        return f'name:{self.name}'

    def __repr__(self):
        return f'{self.name}'

    def __del__(self):
        print(f'__del__():调用')


# 创建对象时传实参
dog=Dog('大黄',5)   # __init__():调用
print(dog.name) # 大黄


# __str__()
#   调用时机：1.print(对象)，会自动调用该方法；
#   2.str(对象) 类型转换，将自定义对象转换为字符串的时候，会嗲用该方法
#   应用：1.打印对象的时候，会输出一些方法
#   2.需要将对象转换成字符串类型的时候
#   注意：方法必须返回一个字符串，只有self一个参数

print(dog) # 如果没有定义__str__()方法，print(对象)默认输出对象的引用地址
# str_dog=str(dog) # 没有定义，强转也是输出对象的引用地址


#  __del__()    析构函数
#  调用时机：对象在内存中被销毁删除的时候
#  1.程序代码运行结束
#  2.使用 'del 变量', 将这个对象的引用计数变为0，会调用
#  引用计数：是python内存管理的一种机制，指的是一块内存一共有多少个变量在引用
#  应用：

dog2=dog    # 计数器为2
del dog     # 计数器为1，不执行__del__()
del dog2    # 计数器为0，执行__del__()

# __repr__() 与str方法类型，必须返回一个字符串
my_list1=[Dog('大黄',2),Dog('小白',3),Dog('阿花',1)]
print(my_list1)
