# 字符串下标支持正数（从0开始） 也支持负数（从-1开始）
string="hello world"
print(string)
print(string[4])    # o

# len() 函数可以得到字符串的长度
print(len(string))  # 11

# 字符串切片 [start:end:steplen] 包含start，不包含end
print(string[3:8:2])    # l o

# find()函数 返回正下标，没有返回-1
# index()函数 会返回正下标，不存在时报错
# rindex()函数 会从后往前查找 不存在报错
print(string.index("d"))   #10
print(string.rindex("d"))  #10