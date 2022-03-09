# 计算1~100的累加和（包含1和100）
sum=0;
i=1
while i<=100:
    sum+=i
    i+=1
print(sum)
print('\n')
# 计算1~100之间偶数的累加和（包含1和100）
sum=0
i=0
while i<=100:
    if i%2==0:
        sum+=i
    i+=1
print(sum)
print('\n')
# 打印三角形
i=1
while i<=5:
    j = 1
    while j<=i:
        j += 1
        print("*",end=' ')

    print('\n')
    i+=1