# 定义家具类
class Furniture(object):
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return f'类型：{self.name},占地面积：{self.area}'

# 定义房子类
class House(object):
    def __init__(self,address,area):
        self.address=address
        self.h_area=area
        self.furnit_list=[]
        self.free_area=area

    def add_furnit(self,obj_funit):
        if self.free_area>obj_funit.area:
            self.furnit_list.append(obj_funit)
            self.free_area-=obj_funit.area
            print(f'家具:{obj_funit.name} 添加成功')
        else:
            print('添加失败')
    def __str__(self):
        buf_list=[obj.name for obj in self.furnit_list]
        buf=','.join(buf_list)
        if self.furnit_list:
            return f'房子地址：{self.address},占地面积：{self.h_area}' \
                   f',剩余面积{self.free_area},家具：{buf}'
        else:
            return f'房子地址：{self.address},占地面积：{self.h_area}' \
                   f',剩余面积{self.free_area}'
# 创建家具类
bed=Furniture('豪华大床',15)
# print(bed)
# 创建房子类
house=House('澳洲农场',100)
print(house)
house.add_furnit(bed)
print(house)

computer=Furniture('电脑',10)
house.add_furnit(computer)
print(house)