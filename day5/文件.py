# 打开文件
#  open(file,mode='r',encoding=)
# mode:w-写入文件，不存在会先创建，不存在先清空再写入；r-只读；a-追加打开
# encoding常用两种：utf-8,gbk
# 返回值为为文件对象，后续所有文件操作，都需要通过这个文件
# 写数据
f=open('test.txt','w',encoding='utf-8')
f.write('hello,world,i am here!文件测试')
f.close()

# 读数据
f=open('test.txt','r',encoding='utf-8')
content=f.read()
print(content)
f.close()