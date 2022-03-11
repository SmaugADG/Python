# 定义类
class Dog(object):
    def play(self):
        print('小狗拆家')
    pass


# 创建对象 变量=类名()
dog=Dog()
# 从外部给对象添加属性
dog.name='大黄'
dog.age=2

print(dog.name)

# 修改属性值，存在就修改，不存在就添加
dog.name='阿黄'
print(dog.name)