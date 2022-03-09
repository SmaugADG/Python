age = 13


def fun_name():
    name = "alan"
    global age
    age=14
    print("%s,%d" % (name, age))


fun_name()
print(age)  # 局部变量不会修改全局变量的值 要改变全局变量的值需要添加global

# 组包 将多个数据值，组成元组，给一个变量
a=1,2,3
print(a)    # (1,2,3)
# 拆包 将容器中的数据分别给到多个变量，需要注意：数据的个数和变量的个数要保持一致
c,d,e=a
print(d)

# 引用 可以使用id()查看变量的引用，可以将id值认为是内存地址的别名
# python中数据值的传递的是引用
# 赋值运算符可以改变变量的引用

a=1
print(id(a))
a+=1
print(id(a))
a=a+1
print(id(a))