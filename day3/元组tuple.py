# 元组使用小括号，元素不能修改和删除，其他类似与列表
my_tulpe=(2,3,6,5)
# 支持下标和切片操作
print(my_tulpe[1])
# 定义空元组,没有意义
my_tulpe1=()
my_tulpe3=tuple()
print(type(my_tulpe1))  # <class 'tuple'>

# 定义一个元素的元组
my_tulpe3=(3)   # <class 'int'>
my_tulpe4=(3,)  # # <class 'tuple'> 需要加一个逗号

