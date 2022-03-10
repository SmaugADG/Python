def my_cal(a,b,func):
    '''
    进行四则运算
    :param a:第一个数
    :param b: 第二各数据
    :param func: 函数进行计算
    :return: 运算结果
    '''
    num=func(a,b)
    print(num)
def add(a,b):
    return a+b
#调用
my_cal(10,20,add)

my_cal(10,20,lambda  a,b:a+b)  # 匿名函数
# sort(key=lambda 形参：（排序规则1，排序规则2.。。）
# 当第一个规则相同，按照第二个规则排序


list2=['ef','bdc','ghlj','df','a','a']
# 匿名函数中的参数就式列表中的每一各数据
list2.sort(key=lambda x:(len(x),x[0]))

print(list2)