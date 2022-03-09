import random
# 1(拳头) 2 (剪刀) 3(布)

user = int(input("请输入："))
while user: # 输入0结束循环
    machine=random.randint(1,3) # 随机产生1-3之间的数
    if (user==1 and machine==3) or (user==2 and machine==1) or (user==3 and machine==1):
        print("user win")
    elif user==machine:
        print("peace")
    else:
        print("machine win")
    user = int(input("请输入："))