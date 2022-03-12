# # 使用try...except捕获异常
import time

try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:  # finally中的信息无论是否有异常都会被执行
        f.close()
        print('关闭文件')
except(IOError, NameError) as result:  # 捕获这两个异常，将异常信息存放到result中
    print(result)
    print('没有这个文件')

'''抛出自定义异常'''
# 可以使用raise语句来英法一个异常。异
# 常/错误对象必须有一个名字，但是他们必须是Error或者Exception类的子类
class ShortInputException(Exception):
    '''自定义异常类'''
    def __init__(self,length,atleast):
        # 如果重写了父类的__init__方法，最好是先调用父类的这个方法，然后再添加自己的功能
        super().__init__()
        self.length=length
        self.atleast=atleast


def main():
    try:
        s=input('请输入->')
        if len(s)<3:
            #raise引发一个异常
            raise ShortInputException(len(3),3)
    except ShortInputException as result:
        print(f'ShortInputException:输入长度是{result.length},'
              f'长度至少是{result.atleast}')
    else:
        print('没有异常')


