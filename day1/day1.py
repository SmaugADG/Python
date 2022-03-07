# 1 注释
print("hello python")
#单行注释
'''
多行注释
'''
# 2 变量
"""
变量依据存放的值的类型自动确定
Number：int float complex(复数) long(python3不再支持，统一为int)
使用type()函数来确认数据类型
"""
num1 = 1
num2 = 2
result = num1 + num2
print(result)
print(type(result))  #<class 'int'>

num3 = 1.5
result +=num3
print(result)   #<4.5>
print(type(result))  #<class 'float'>
#字符串单双引号都可以用
string="hello"
print(type(string))  #<class 'str'>

# 3  格式化输出
name="Alan"
age = 12
print("My name is %s,I am %d years old"%(name,age))
# 如果需要输出% 则需要使用两个%才可以
print("占比%%%d"%50)
# python3.6开始支持f-string ,使用{}来占位
print(f"My name is {name},I am {age} years old") #注意不要忘记f,可以写成F
# 换行，可以使用'\n'
print('\n-------------------------------------------------')
# 取消换行 end(' ')
print("hello",end=' ')
print('world')  # hello world

# 4 输入
'''
input('提示信息')函数，得到用户输入的内容，遇到回车结束，得到的数据都是字符串类型
'''
input('请输入：')

# 练习：从键盘上录入苹果的价格 、重量 ，输出: 苹果单价 9.00 元／⽄，购买了 5.00 ⽄，需要⽀付 45.00 元.
price=input('单价：')
weight=input('重量：')
sum=float(price)*float(weight) # input()接收偶的值为str 需要强转后才能计算
print(f'共需要支付{sum}元')
