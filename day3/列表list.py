#encoding-utf-8
import random

offices=[[],[],[]]
names=['A','B','C','D','E','F','G','H']

for name in names:
    index=random.randint(0,2)
    offices[index].append(name)

i=1
for tmp_name in offices:
    print('办公室%d的人数为：%d'%(i,len(tmp_name)))
    i+=1
    for name in tmp_name:
        print(name,end=' ')
    print('\n')