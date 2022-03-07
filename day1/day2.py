#  类型转换
# 1 转换为int
# 1.1 float 转换成 int
pi=3.14
num=int(3.14)
print(type(pi))  # float
print(type(num))    # int
# 1.2 整数类型的字符串 "10"
my_str='10'
num1=int(my_str)
print(type(num1))   # int

# 2 转换为 float
#2.1 int--->float
num2=10
num3=float(num2)
print(type(num3))   # float

#eval() 函数 可以去掉"" 还原成原来的值
num4=input("please input num:")
print(type(eval(num4))) # 如果输入str类型的会报错

