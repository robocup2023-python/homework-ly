num = [1,2,3,5,7,11,13]
x=int(input('请输入一个数字'))
if x<13:
    i=0
    while x>=num[i]:
        i+=1
    num.insert(i,x)
print(num)

