# set 使用{}定义
# 结合中的数据必须是不可变类型
# 集合是可变类型
# 集合是无序的（数据的添加顺序和输出顺序不一致为无序）
# 集合中的数据没有重复数据（可以用于去重）
my_set={1,3.14,True,'hello',(1,2)}
print(my_set)

my_set.remove(3.14)
print(my_set)