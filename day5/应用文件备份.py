# 提示输入文件
old_file_name = input("请输入要拷贝的文件名：")
# 以读的方式打开文件
old_file=open(old_file_name,'rb')
# 提取文件的后缀
fil_flag_num=old_file_name.rfind('.')   # 使用rfind()，避免带多个.的文件名造成的错误
if fil_flag_num>0:
    file_flag=old_file_name[fil_flag_num:]
# 组织新的文件名
new_file_name=old_file_name[:fil_flag_num]+'[复件]'+file_flag
# 创建新文件
new_file=open(new_file_name,'wb')
#把旧文件中的数据，一行一行的进行复制到新文件
for live_content in old_file.readlines():
    new_file.write(live_content)
# 关闭文件
old_file.close()
new_file.close()
