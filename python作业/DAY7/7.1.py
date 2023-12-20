import random
path='data.txt'
file=open(path,'w')
for i in range(1,11):
    file.write(str(random.randint(1,10))+','+str(random.randint(1,10))+','+str(random.randint(1,10))+'\n')
file.close()
f=open(path,'r')
r=str(f.readlines()[1])
r=r.rstrip('\n')
n=r.split(',')
a=float(n[0])
b=float(n[1])
c=float(n[2])
avg=(a+b+c)/3
list=[a,b,c]
list.sort()
max=list[2]
min=list[0]
mid=list[1]
print(avg)
print(max)
print(min)
print(mid)