import time
import os

# 定以一个列表，存放学生信息
info_list = []


# 菜单
def print_menu():
    print("--------------------------------------")
    print("     学生管理系统 v1.0")
    print("1:添加学生")
    print("2:删除学生")
    print("3:修改学生")
    print("4:查询学生")
    print("5:显示学生")
    print("6:退出系统")
    print("---------------------------------------")


# 新增
def stu_add():
    global info_list
    new_name = input("姓名：")
    new_gender = input("性别：")
    new_grade = input("年级：")

    for tmp_info in info_list:
        if tmp_info['name'] == new_name:
            print('此用户名已存在，请重新输入')
    info = {}
    info['name'] = new_name
    info['gender'] = new_gender
    info['grade'] = int(new_grade)

    info_list.append(info)
    return


def stu_del():
    global info_list
    del_num = int(input("输入序号："))
    while del_num >= 0:
        del_num = int(input("输入序号："))
        if 0 <= del_num <= len(info_list):
            del info_list[del_num]
        else:
            print("编号不存在，重新输入，退出请输入-1！")
    return


def stu_mod():
    global info_list
    mod_num = int(input('请输入序号：'))
    if 0 <= mod_num < len(info_list):
        info_list[mod_num]['name'] = input('姓名：')
        info_list[mod_num]['gender'] = input('性别：')
        info_list[mod_num]['grade'] = int(input('年级:'))

    else:
        print('输入序号有误')

    return


def stu_ser():
    stu_name = input('请输入姓名：')
    for tmp_info in info_list:
        if tmp_info['name'] == stu_name:
            print("姓名\t\t性别\t\t年级")
            print("%s\t%s\t%d\t" % (tmp_info['name'], tmp_info['gender'], tmp_info['grade']))
            break
        else:
            print('未查到信息。。。')
    return


def stu_cat():
    print("序号\t姓名\t\t性别\t\t年级")
    i = 0
    for tmp in info_list:
        print("%d\t%s\t%s\t%d\t" % (i, tmp['name'], tmp['gender'], tmp['grade']))
        i += 1


# 函数入口
def main():
    while True:
        print_menu()
        ch = input("请输入你的选择：")
        if ch == '1':
            stu_add()
        elif ch == '2':
            stu_del()
        elif ch == '3':
            stu_mod()
        elif ch == '4':
            stu_ser()
        elif ch == '5':
            stu_cat()
        elif ch == '6':
            break
        else:
            print("输入错误")

        # input("\n按回车继续。。。")
        # os.system("clear")

#程序入口
main()
